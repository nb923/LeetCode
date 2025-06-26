class MyStack {
    Queue<Integer> in ;
    Queue<Integer> out;

    public MyStack() {
        in = new LinkedList<>();
        out = new LinkedList<>();

    }

    public void push(int x) {
        in.add(x);

    }

    public int pop() {
        // if(out.isEmpty()){
        //     while(!in.isEmpty()){
        //         out.add(in.remove());
        //     }
        // }
        // return out.remove();

        while(in.size() > 1)
        {
            out.add(in.remove());
        }

        int ret = in.remove();

        while(out.size() != 0)
        {
            in.add(out.remove());
        }

        return ret;
    }

    public int top() {
        // if(out.isEmpty()){
        //     while(!in.isEmpty()){
        //         out.add(in.remove());
        //     }
        // }
        // return out.peek();
        
        while(in.size() > 1)
        {
            out.add(in.remove());
        }

        int ret = in.remove();

        while(out.size() != 0)
        {
            in.add(out.remove());
        }

        in.add(ret);

        return ret;
    }

    public boolean empty() {
        return in.isEmpty() && out.isEmpty();

    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */