'''
メンバーが多重継承先のどのクラスに属するかを判定したい
現在の実装では、以下の問題点あり
  オーバーライドしているかどうかがわからない。
  一番基底クラスで見つけたあとすぐに終了しない <- 再帰呼出しで終了する方法
'''
def inspect_which_base_class_has_the_instance(leaf, attr_name):
    if not len(leaf.__bases__):
        print('Any class dont have')
        return
    for super_class in leaf.__bases__:
        if len(super_class.__bases__):
            inspect_which_base_class_has_the_instance(super_class, attr_name)
        instance = super_class()
        newly_members = set(dir(leaf)) - set(dif(super_class))
        if 'http_method_names' in newly_members:
            print(leaf)
            return
