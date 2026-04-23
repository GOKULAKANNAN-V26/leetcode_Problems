import java.util.*;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int a : asteroids) {
            boolean destroyed = false;

            while (!stack.isEmpty() && a < 0 && stack.peek() > 0) {
                if (stack.peek() < -a) {
                    stack.pop(); // destroy smaller
                } else if (stack.peek() == -a) {
                    stack.pop(); // both destroy
                    destroyed = true;
                    break;
                } else {
                    destroyed = true; // current destroyed
                    break;
                }
            }

            if (!destroyed) {
                stack.push(a);
            }
        }

        // Convert stack to array
        int[] res = new int[stack.size()];
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }

        return res;
    }
}