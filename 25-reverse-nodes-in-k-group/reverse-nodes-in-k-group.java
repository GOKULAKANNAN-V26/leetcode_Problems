class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevGroup = dummy;

        while (true) {
            // Check if k nodes exist
            ListNode kth = prevGroup;
            for (int i = 0; i < k; i++) {
                kth = kth.next;
                if (kth == null) return dummy.next;
            }

            ListNode groupStart = prevGroup.next;
            ListNode nextGroup = kth.next;

            // Reverse k nodes
            ListNode prev = nextGroup;
            ListNode curr = groupStart;

            while (curr != nextGroup) {
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }

            // Connect with previous part
            prevGroup.next = kth;
            prevGroup = groupStart;
        }
    }
}