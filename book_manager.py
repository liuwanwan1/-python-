"""
图书信息管理系统
功能：录入、删除、查询、显示全部图书信息
数据存储：列表（每个元素为字典，代表一本图书）
"""


def print_menu():
    """打印系统主菜单"""
    print("=" * 40)
    print("       图书信息管理系统")
    print("=" * 40)
    print("  1. 录入图书信息")
    print("  2. 删除图书信息")
    print("  3. 查询图书信息")
    print("  4. 显示全部图书信息")
    print("  0. 退出系统")
    print("=" * 40)


def add_book(book_list):
    """
    录入图书信息
    :param book_list: 存储图书信息的列表
    :return: 添加成功返回True，否则返回False
    """
    print("\n--- 录入图书信息 ---")
    
    # 获取用户输入
    book_id = input("请输入图书编号: ").strip()
    
    # 检查编号是否已存在
    for book in book_list:
        if book["编号"] == book_id:
            print("❌ 该编号已存在，请使用其他编号！")
            return False
    
    if not book_id:
        print("❌ 编号不能为空！")
        return False
    
    book_name = input("请输入图书书名: ").strip()
    author = input("请输入作者: ").strip()
    
    # 价格输入验证
    price_str = input("请输入价格: ").strip()
    try:
        price = float(price_str)
        if price < 0:
            print("❌ 价格不能为负数！")
            return False
    except ValueError:
        print("❌ 价格必须是数字！")
        return False
    
    category = input("请输入分类: ").strip()
    
    # 创建图书字典并添加到列表
    book = {
        "编号": book_id,
        "书名": book_name,
        "作者": author,
        "价格": price,
        "分类": category
    }
    book_list.append(book)
    print("✅ 图书信息录入成功！")
    return True


def delete_book(book_list):
    """
    根据编号删除图书信息
    :param book_list: 存储图书信息的列表
    :return: 删除成功返回True，否则返回False
    """
    print("\n--- 删除图书信息 ---")
    
    if not book_list:
        print("⚠️ 图书列表为空，无图书可删除！")
        return False
    
    book_id = input("请输入要删除的图书编号: ").strip()
    
    # 遍历查找并删除
    for index, book in enumerate(book_list):
        if book["编号"] == book_id:
            deleted_book = book_list.pop(index)
            print(f"✅ 已成功删除图书: 《{deleted_book['书名']}》")
            return True
    
    print(f"❌ 未找到编号为 '{book_id}' 的图书！")
    return False


def query_book(book_list):
    """
    根据编号查询单本图书详情
    :param book_list: 存储图书信息的列表
    :return: 查询成功返回True，否则返回False
    """
    print("\n--- 查询图书信息 ---")
    
    if not book_list:
        print("⚠️ 图书列表为空！")
        return False
    
    book_id = input("请输入要查询的图书编号: ").strip()
    
    # 遍历查找
    for book in book_list:
        if book["编号"] == book_id:
            print_book_detail(book)
            return True
    
    print(f"❌ 未找到编号为 '{book_id}' 的图书！")
    return False


def print_book_detail(book):
    """
    格式化输出单本图书详细信息
    :param book: 图书字典
    """
    print("\n" + "-" * 40)
    print(f"  图书编号: {book['编号']}")
    print(f"  图书书名: 《{book['书名']}》")
    print(f"  作    者: {book['作者']}")
    print(f"  价    格: ¥{book['价格']:.2f}")
    print(f"  分    类: {book['分类']}")
    print("-" * 40)


def print_all_books(book_list):
    """
    格式化输出全部图书信息，排版整洁
    :param book_list: 存储图书信息的列表
    """
    print("\n--- 全部图书信息 ---")
    
    if not book_list:
        print("⚠️ 当前没有图书信息！")
        return
    
    # 打印表头
    print("\n" + "=" * 80)
    print(f"{'编号':<12}{'书名':<20}{'作者':<15}{'价格':<12}{'分类':<15}")
    print("-" * 80)
    
    # 打印每本图书信息
    for book in book_list:
        print(f"{book['编号']:<12}"
              f"《{book['书名']}》{'':<{18-len(book['书名'])*2}}"
              f"{book['作者']:<15}"
              f"¥{book['价格']:<10.2f}"
              f"{book['分类']:<15}")
    
    print("=" * 80)
    print(f"共 {len(book_list)} 本图书\n")


def main():
    """主函数，程序入口"""
    # 使用列表存储所有图书数据
    book_list = []
    
    # 预置一些示例数据（方便演示，可选）
    # book_list = [
    #     {"编号": "001", "书名": "Python编程", "作者": "张三", "价格": 59.00, "分类": "计算机"},
    #     {"编号": "002", "书名": "数据结构", "作者": "李四", "价格": 45.50, "分类": "计算机"},
    # ]
    
    while True:
        print_menu()
        choice = input("请选择功能 (0-4): ").strip()
        
        if choice == "1":
            add_book(book_list)
        elif choice == "2":
            delete_book(book_list)
        elif choice == "3":
            query_book(book_list)
        elif choice == "4":
            print_all_books(book_list)
        elif choice == "0":
            print("\n感谢使用图书信息管理系统，再见！")
            break
        else:
            print("❌ 无效的选择，请重新输入！")
        
        # 暂停，等待用户按回车继续
        input("\n按回车键继续...")


# 程序入口
if __name__ == "__main__":
    main()
