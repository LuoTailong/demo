# coding:utf-8


class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


# node = Node(100)
class SingleLinkList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self._head = None
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素 param:pos 从0开始"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            pre = self._head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环推出后pre指向pos-1的位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                # break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self._head
        if cur.elem == item:
            return True
        else:
            cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    print(ll.is_empty())
    print(ll.length())
    ll.travel()

    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 18)
    ll.travel()
    ll.insert(10, 100)
    ll.travel()

    ll.remove(2)
    ll.travel()
    ll.remove(100)
    ll.travel()
