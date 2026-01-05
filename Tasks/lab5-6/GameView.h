#pragma once
#include <SFML/Graphics.hpp>
using namespace std;
using namespace sf;

struct GameView {
	Vector2i windowSize;
	RenderWindow window;
	Clock clock;
	View camera;
};

using OnUpdate = void (void*, GameView&, float);
using OnDraw = void (void*, GameView&);
void EnterGameLoop(GameView& view, OnUpdate onUpdate, OnDraw onDraw, void* pData);
GameView* NewGameView(const Vector2i& windowSize);
void SetCameraCenter(GameView& view, const sf::Vector2f& center);
void DestroyGameView(GameView*& pView);