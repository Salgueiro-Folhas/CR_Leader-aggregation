import threading


class OwnerCoreNodeList:

    def __init__(self):
        self.lock = threading.Lock()
        self.list = set()

    def add(self, peer):
        """
        Coreノードをリストに追加する。

        param:
            peer : Coreノードとして格納されるノードの接続情報（IPアドレスとポート番号）
        """
        with self.lock:
            print('Adding Owner peer: ', peer)
            self.list.add((peer))
            print('Current Owner List: '+ str(len(self.list)), self.list)

    def remove(self, peer):
        """
        離脱したと判断されるCoreノードをリストから削除する。

        param:
            peer : 削除するノードの接続先情報（IPアドレスとポート番号）
        """
        with self.lock:
            if peer in self.list:
                print('Removing peer: ', peer)
                self.list.remove(peer)
                print('Current Owner list: '+ str(len(self.list)), self.list)

    def overwrite(self, new_list):
        """
        複数のpeerの生存確認を行った後で一括での上書き処理をしたいような場合はこちら
        """
        with self.lock:
            print('owner node list will be going to overwrite')
            self.list = new_list
            print('Current Owner list: '+ str(len(self.list)), self.list)

    def get_list(self):
        """
        現在接続状態にあるPeerの一覧を返却する
        """
        return self.list

    def get_length(self):
        print("get_length(self):" , len(self.list))
        return len(self.list)

    def get_c_node_info(self):
        """
        リストのトップにあるPeerを返却する
        """
        return list(self.list)[0]

    def has_this_peer(self, peer):
        """
        与えられたpeerがリストに含まれているか？をチェックする

            param:
                peer : IPアドレスとポート番号のタプル
            return:
                True or False
        """
        return peer in self.list
