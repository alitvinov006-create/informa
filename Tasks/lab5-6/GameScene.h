#pragma once
#include "TmxLevel.h"
#include "GameView.h"
#include <vector>
using namespace std;
using namespace sf;

struct GameScene {
	TmxLevel level;
	TmxObject player;
	vector<TmxObject> blocks;
	vector<TmxObject> coins;
	vector<TmxObject> enemies;
	Vector2f startPosition;
};

GameScene* NewGameScene();
void DestroyGameScene(GameScene*& pScene);
void DrawGameScene(void* pData, GameView& view);
void UpdateGameScene(void* pData, GameView& view, float deltaSec);