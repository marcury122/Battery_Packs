#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define all(x) (x).begin(), (x).end()

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int gen[12] = {0, 0, 0, 2, 5, 6, 10, 4, 3, 0, 0, 0}, bat[12], con[12] = {1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 6}, grid[12];
    int BH = 0;
    int maxBh = 5;
    for (int i = 0; i < 12; i++)
    {

        BH += gen[i] - con[i];
        if (BH < 0)
        {
            grid[i] = -BH;
            BH = 0;
        }
        else if (BH > maxBh)
        {
            grid[i] = maxBh - BH;
            BH = maxBh;
        }
        else
        {
            grid[i] = 0;
        }
        bat[i] = con[i] - gen[i] - grid[i];
    }
    for(int i=0;i<12;i++){
        cout<<bat[i] << " ";
    }
    cout<<endl;

    for(int i=0;i<12;i++){
        cout<<grid[i] << " ";
    }
    cout<<endl;
    return 0;
}