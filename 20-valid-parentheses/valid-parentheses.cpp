class Solution {
public:
    bool isValid(string s) {
        int n = s.size();
        // allocate dynamic memory for stack
        char* stack = new char[n];
        int top = -1;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                stack[++top] = c; // push
            } else {
                if (top == -1) { // stack empty
                    delete[] stack;
                    return false;
                }
                char t = stack[top--]; // pop
                if ((c == ')' && t != '(') ||
                    (c == ']' && t != '[') ||
                    (c == '}' && t != '{')) {
                    delete[] stack;
                    return false;
                }
            }
        }

        bool isValid = (top == -1);
        delete[] stack; // free memory
        return isValid;
    }
};
