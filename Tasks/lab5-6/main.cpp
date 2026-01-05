#include <SFML/Graphics.hpp>
#include <iostream>
#include "GameView.h"
#include "GameScene.h"
using namespace std;
using namespace sf;

int main()
{
    try {
        GameView* gameView = NewGameView(Vector2i(1920, 1080));
        GameScene* gameScene = NewGameScene();

        EnterGameLoop(*gameView, &UpdateGameScene, &DrawGameScene, gameScene);
    }
    catch (const std::exception& ex) {
        cerr << ex.what() << endl;
        return 1;
    }

    return 0;
}