class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.size();
        int counter = 0;

        for(int i = n-1; i >=0 ; i--){
            if (s[i] != ' '){
                n = i+1;
                break;
            }
        }
        for(int i = n-1; i >=0 ; i--){
            if (s[i] == ' '){
                return counter;
            }
            else{

                counter++;
            }
        }
        return counter;
    }
};
