#include <SFML/Graphics.hpp>
using namespace sf;
using namespace std;

int main()
{
    RenderWindow window(VideoMode(500, 500), "SFML KINDA WORKS!");
    const int gridSize = 10;
    const int cellSize = 50;
    RectangleShape cells[gridSize][gridSize];

    while (window.isOpen())
    {
        Event event;
        while (window.pollEvent(event))
        {
            if (event.type == Event::Closed)
                window.close();
        }
        window.clear(Color::White);
        for (int i = 0; i < gridSize; ++i) {
            for (int k = 0; k < gridSize; ++k) {
                cells[i][k].setSize(Vector2f(cellSize - 1, cellSize - 1));
                cells[i][k].setPosition(i * cellSize, k * cellSize);
                if (i == gridSize / 2 or k == gridSize / 2) {
                    cells[i][k].setFillColor(Color::Green);
                }
                else {
                    cells[i][k].setFillColor(Color::White);
                }
                cells[i][k].setOutlineColor(Color::Black);
                cells[i][k].setOutlineThickness(1);
                window.draw(cells[i][k]);
            }
        }

        window.display();
    }
    return 0;
}
