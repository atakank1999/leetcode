class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        int m = strs[0].size();
        for(int i = 0; i< m ; i++){
            char c = strs[0][i];
            for(int j =0; j < n; j++){
                if(strs[j][i] != c || i == strs[j].size()){
                    return strs[0].substr(0,i);
                }
            }
        }
        return strs[0];

    }
};
