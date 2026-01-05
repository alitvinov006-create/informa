#include "GameView.h"
#include <SFML/Graphics.hpp>
using namespace std;
using namespace sf; // ??? ??????? ?????


GameView *NewGameView(const Vector2i &windowSize)
{
    GameView *pView = new GameView;
    pView->windowSize = windowSize;

    ContextSettings settings;
    settings.antialiasingLevel = 8;
    pView->window.create(VideoMode(windowSize.x, windowSize.y), "ITS ME", Style::Close, settings);
    pView->window.setFramerateLimit(144); // true gamingz

    pView->camera.reset(FloatRect(0.0f, 0.0f, windowSize.x, windowSize.y));
    pView->camera.setViewport(FloatRect(0.0f, 0.0f, 2.0f, 2.0f));

    return pView;
}

void EnterGameLoop(GameView &view, OnUpdate onUpdate, OnDraw onDraw, void *pData)
{
    while (view.window.isOpen())
    {
        Event event;
        while (view.window.pollEvent(event))
        {
            if (event.type == Event::Closed)
            {
                view.window.close();
                break;
            }
        }

        const Time elapsedTime = view.clock.getElapsedTime();
        view.clock.restart();
        onUpdate(pData, view, elapsedTime.asSeconds());

        view.window.clear();
        onDraw(pData, view);
        view.window.display();
    }
}

void DestroyGameView(GameView *&pView)
{
    delete pView;
    pView = nullptr;
}

void SetCameraCenter(GameView &view, const Vector2f &center)
{
    view.camera.setCenter(center.x, center.y);
    view.window.setView(view.camera);
}
