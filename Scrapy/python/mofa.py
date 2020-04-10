#!/usr/bin/python3
# _*_ Coding: UTF-8 _*_
from __future__ import division

import collections
import copy
import math
import operator
import pickle
import sys
import asyncio
from typing import Iterable


class MedusaSorcerer:
    instance = 'medusa'

    def __abs__(self):
        """
        >>> abs(MedusaSorcerer())
        返回数字绝对值的方法
        """
        return '__abs__'

    def __add__(self, other):
        """
        >>> MedusaSorcerer() + 123
        实现加法运算
        """
        return '__add__'

    async def __aenter__(self):
        """
        异步上下文管理器是上下文管理器的一种
        它能够在其 __aenter__ 和 __aexit__ 方法中暂停执行

        在语义上类似于 __enter__
        仅有的区别是它必须返回一个 可等待对象

        官方中文文档:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__aenter__#object.__aenter__
        """
        await asyncio.sleep(123)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        异步上下文管理器是上下文管理器的一种
        它能够在其 __aenter__ 和 __aexit__ 方法中暂停执行

        在语义上类似于 __exit__
        仅有的区别是它必须返回一个 可等待对象

        官方中文文档:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__aenter__#object.__aexit__
        """
        await asyncio.sleep(123)

    def __aiter__(self):
        """
        异步迭代器 可以在其 __anext__ 方法中调用异步代码

        返回一个 异步迭代器 对象

        官方中文文档:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__aiter__#object.__aiter__
        """
        return self

    def __and__(self, other):
        """
        >>> MedusaSorcerer() & 123
        实现按位 and 运算
        """
        return '__and__ True'

    def __anext__(self):
        """
        必须返回一个 可迭代对象 输出迭代器的下一结果值
        当迭代结束时应该引发 StopAsyncIteration 错误

        官方中文文档:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__aiter__#object.__anext__
        """
        pass

    def __await__(self):
        """
        返回一个迭代器
        官方中文文档:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__aiter__#object.__await__
        """
        pass

    def __call__(self, *args, **kwargs):
        """
        >>> MedusaSorcerer()()
        调用对象(callable):
            但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象
        如果在类中实现了 __call__ 方法, 那么实例对象也将成为一个可调用对象
        """
        self.params = '__call__'

    def __init__(self, **kwargs):
        """
        >>> MedusaSorcerer(element='__element__')
        构造实例对象后初始化实例属性的方法
        """
        self.params = 'params'
        self.element = kwargs.get('element')

    def __bool__(self):
        """
        >>> if MedusaSorcerer(): print('True')
        布尔值比较时调度该方法
        """
        return True

    def __bytes__(self):
        """
        >>> bytes(MedusaSorcerer())
        返回字节数组调度的方法
        """
        return bytes('123', encoding='UTF-8')

    def __ceil__(self):
        """
        >>> math.ceil(MedusaSorcerer())
        返回最小整数的时候调度该方法
        """
        return '__ceil__'

    def __class_getitem__(cls, item):
        """
        按照 key 参数指定的类型返回一个表示泛型类的专门化对象

        官方中文文档, 或许你还需要查阅 PEP484 和 PEP560:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__class_getitem__#object.__class_getitem__

        PEP560案例和说明:
        https://www.python.org/dev/peps/pep-0560/#class-getitem
        """
        pass

    def __cmp__(self, other):
        """
        >>> sorted(MedusaSorcerer(), MedusaSorcerer())
        在实现我们自定义的排序规则的时候我们需要对实例实现__cmp__方法
        例如我给的例子中:
            如果传递的对象params属性 大于 本身实例对象的params属性: 返回 -1
            如果传递的对象params属性 小于 本身实例对象的params属性: 返回 +1
            如果传递的对象params属性 等于 本身实例对象的params属性: 返回 0
        """
        if self.params < other.params:
            return -1
        elif self.params > other.params:
            return 1
        return 0

    def __coerce__(self, other):
        """
        >>> coerce(MedusaSorcerer(), MedusaSorcerer())
        实现了混合模式运算
        Python3中已经废弃
        """
        pass

    def __complex__(self):
        """
        >>> complex(MedusaSorcerer())
        实现复数转换的时候调度该方法
        """
        return complex(123)

    def __contains__(self, item):
        """
        >>> item not in MedusaSorcerer()
        >>> item in MedusaSorcerer()
        判断是否包含元素时
        """
        return True if item == '123' else False

    def __copy__(self):
        """
        >>> copy.copy(MedusaSorcerer())
        返回浅拷贝对象
        """
        return 123

    def __deepcopy__(self, memodict={}):
        """
        >>> copy.deepcopy(MedusaSorcerer())
        返回深拷贝对象
        """
        return self

    def __del__(self):
        """
        >>> medusa = MedusaSorcerer()
        >>> del medusa
        对象进行垃圾回收时候的行为函数
        """
        print('__del__')

    def __delattr__(self, item):
        """
        >>> del self.params
        实现删除实例属性的时候将会调度该方法
        """
        self.__dict__.pop(item)

    def __delete__(self, instance):
        """
        >>> class Test: medusa = MedusaSorcerer()
        >>> del Test().medusa
        官方: 调用此方法以删除 instance 指定的所有者类的实例的属性
        在其实例拥有者对其进行删除操作的时候调用该方法
        """
        print('__delete__')

    def __delitem__(self, key):
        """
        >>> del MedusaSorcerer()['params']
        使用键值对删除的时候将会调度该方法
        """
        self.__dict__.pop(key)

    def __delslice__(self, i, j):
        """
        __getslice__、__setslice__、__delslice__：用于分片的三个操作
        Python3中已经废弃
        """
        pass

    def __dir__(self) -> Iterable[str]:
        """
        >>> dir(MedusaSorcerer())
        返回所有实例属性和方法
        """
        return super().__dir__()

    def __divmod__(self, other):
        """
        >>> divmod(MedusaSorcerer(), 123)
        返回 (整数, 取余) 的元组数组
        """
        return 123, 123

    def __enter__(self):
        """
        >>> with MedusaSorcerer(): pass
        调度 with 语句块的时候需要实现该方法
        """
        self.enter = '__enter__'

    def __eq__(self, other):
        """
        >>> MedusaSorcerer() == 123
        调度判等条件的时候需要实现的方法
        """
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        >>> with MedusaSorcerer(): pass
        退出 with 语句块的时候将会调度该方法

        退出关联到此对象的运行时上下文
        各个参数描述了导致上下文退出的异常
        如果上下文是无异常地退出的, 三个参数都将为 None
        如果提供了异常并且希望方法屏蔽此异常(即避免其被传播)
        则应当返回真值, 否则的话, 异常将在退出此方法时按正常流程处理
        """
        self.enter = '__exit__'

    def __float__(self):
        """
        >>> float(MedusaSorcerer())
        返回浮点数将会调度该方法
        """
        return float(123)

    def __floor__(self):
        """
        >>> math.floor(MedusaSorcerer())
        返回最大整数的时候调度该方法
        """
        return '__floor__'

    def __floordiv__(self, other):
        """
        >>> MedusaSorcerer() // 123
        进行除法运算的时候将会调度该方法
        """
        return 123.0

    def __format__(self, format_spec):
        """
        >>> format(MedusaSorcerer(), 'self.params = %params%')
        作为格式化字符串将字符串格式化返回
        """
        return format_spec.replace('%params%', self.params)

    def __fspath__(self):
        """
        PEP 519
        返回当前对象的文件系统表示
        这个方法只应该返回一个 str 字符串或 bytes 字节串, 优先选择 str 字符串

        官方中文文档:
        https://docs.python.org/zh-cn/3/library/os.html?highlight=__fspath__#os.PathLike.__fspath__
        https://www.python.org/dev/peps/pep-0519/#protocol
        https://www.python.org/dev/peps/pep-0519/#have-fspath-only-return-strings
        """
        pass

    def __ge__(self, other):
        """
        >>> MedusaSorcerer() >= 123
        调度大于等于条件的时候需要实现的方法
        """
        return True

    def __get__(self, instance, owner):
        """
        >>> class Test: medusa = MedusaSorcerer()
        >>> print(Test().medusa)
        官方: 调用此方法以获取所有者类的属性（类属性访问）或该类的实例的属性（实例属性访问）
        官方: 可选的 owner 参数是所有者类而 instance 是被用来访问属性的实例，如果通过 owner 来访问属性则返回 None
        在其实例拥有者对其进行查询操作的时候调用该方法
        """
        return '__get__'

    def __getattr__(self, item):
        """
        >>> MedusaSorcerer().params_2 = 123
        引用不存在实例属性时将会调度该方法
        __getattr__存在时__getattr__不会被调用, 除非显示调用或引发AttributeError异常
        """
        return f'object has no attribute "{item}"'

    def __getattribute__(self, item):
        """
        >>> MedusaSorcerer().params
        引用存在实例属性时将会调度该方法
        __getattr__存在时__getattr__不会被调用, 除非显示调用或引发AttributeError异常
        """
        return super().__getattribute__(item)

    def __getinitargs__(self):
        """
        >>> pickle.loads(pickle.dumps(MedusaSorcerer()))
        在旧式类中(Python 3.x中默认都是新式类, 经典类被移除)
        当你需要unpickle的时候调度__init__方法, 则需要定义该方法
        并返回__init__所需参数元组
        """
        return '__getinitargs__',

    def __getitem__(self, item):
        """
        >>> MedusaSorcerer()['params']
        实现用键值下表的方式获取数据
        """
        return self.__dict__.get(item)

    def __getnewargs__(self):
        """
        >>> pickle.loads(pickle.dumps(MedusaSorcerer()))
        对新式类来说, 你可以通过这个方法改变类在反pickle时传递给__new__的参数
        这个方法应该返回一个参数元组
        在Python3.6前, 第2、3版协议会调用__getnewargs__, 更高版本协议会调用__getnewargs_ex__

        其实pickle并不直接调用以下几个函数:
            __getnewargs_ex__
            __getnewargs__
            __getstate__
        事实上,, 这几个函数是复制协议的一部分它们实现了__reduce__这一特殊接口
        复制协议提供了统一的接口, 用于在封存或复制对象的过程中取得所需数据
        尽管这个协议功能很强, 但是直接在类中实现__reduce__接口容易产生错误
        因此, 设计类时应当尽可能的使用高级接口, 比如__getnewargs_ex__、__getstate__和__setstate__
        """
        return '__getnewargs__',

    def __getstate__(self):
        """
        >>> pickle.loads(pickle.dumps(MedusaSorcerer()))
        在pickle之前获取对象的状态

        其实pickle并不直接调用以下几个函数:
            __getnewargs_ex__
            __getnewargs__
            __getstate__
        事实上,, 这几个函数是复制协议的一部分它们实现了__reduce__这一特殊接口
        复制协议提供了统一的接口, 用于在封存或复制对象的过程中取得所需数据
        尽管这个协议功能很强, 但是直接在类中实现__reduce__接口容易产生错误
        因此, 设计类时应当尽可能的使用高级接口, 比如__getnewargs_ex__、__getstate__和__setstate__
        """
        return self.__dict__

    def __gt__(self, other):
        """
        >>> MedusaSorcerer() > 123
        调度大于条件的时候需要实现的方法
        """
        return False

    def __hash__(self):
        """
        >>> hash(MedusaSorcerer())
        返回自定义散列值
        """
        return -123

    def __hex__(self):
        """
        __oct__, __hex__: use __index__ in oct() and hex() instead.
        Python3 已经废弃
        官方中文文档:
        https://docs.python.org/zh-cn/3/whatsnew/3.0.html?highlight=__hex__#operators-and-special-methods
        """
        pass

    def __iadd__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa += 123
        实现就地加法运算
        """
        return self.params + f'{str(other)}(__iadd__)'

    def __iand__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa &= 123
        实现就地按位 and 运算
        """
        return '__iand__ True'

    def __idiv__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa /= 123
        实现就地除法运算
        Python3已不再使用该方法, 迁移至__itruediv__
        """
        return '__idiv__'

    def __ifloordiv__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa //= 123
        实现就地整除运算
        """
        return '__ifloordiv__'

    def __ilshift__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa <<= 123
        实现就地左移位赋值运算符
        """
        return 123 << other

    def __imatmul__(self, other):
        """
        查阅 PEP465:
        https://www.python.org/dev/peps/pep-0465/#specification

        官方中文文档 (无说明文档):
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__imatmul__#object.__imatmul__
        """
        pass

    def __imod__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa %= 123
        实现就地取余运算
        """
        return '__imatmul__'

    def __imul__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa *= 123
        实现就地乘法运算
        """
        return '__imul__'

    def __index__(self):
        """
        >>> bin(MedusaSorcerer())
        >>> hex(MedusaSorcerer())
        >>> oct(MedusaSorcerer())
        >>> operator.index(MedusaSorcerer())
        调用此方法以实现operator.index()以及Python需要无损地将数字对象转换为整数对象的场合
        例如切片或是内置的bin(), hex()和oct()函数
        存在此方法表明数字对象属于整数类型, 且必须返回一个整数
        """
        return 123

    def __init_subclass__(cls, **kwargs):
        """
        >>> class Test(MedusaSorcerer, params='class Test'): ...
        >>> print(Test.params)
        当一个类继承其他类时, 那个类的__init_subclass__会被调用
        这样就可以编写能够改变子类行为的类
        __init_subclass__只作用于定义了该方法的类下所派生的子类
        """
        cls.params = '__init_subclass__' if not kwargs.get('params') else kwargs.get('params')
        super().__init_subclass__()

    def __instancecheck__(self, instance):
        """
        >>> class BaseTypeClass(type):
        >>>     def __new__(cls, name, bases, namespace, **kwd): return type.__new__(cls, name, bases, namespace)
        >>>     def __instancecheck__(self, other): return False
        >>> class A(metaclass=BaseTypeClass): ...
        >>> print(isinstance(A(), A))
        控制某个对象是否是该对象的实例

        isinstance函数会进行快速检查
        查看参数提供的实例的类型是否与该类的类型相同
        如果相同则将提早返回结果, 并且不会调用__instancecheck__方法
        这是为了避免不必要时对__instancecheck__进行复杂调用而使用的优化
        """
        pass

    def __int__(self):
        """
        >>> int(MedusaSorcerer())
        转换为数字类型的调度方法
        """
        return 123

    def __invert__(self):
        """
        >>> ~MedusaSorcerer()
        实现一元运算的返回值调度方法
        """
        return ~123

    def __ior__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa |= 123
        实现就地按位 or 操作的方法
        """
        return '__ior__'

    def __ipow__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa **= 123
        实现就地幂算法
        """
        return '__ipow__'

    def __irshift__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa >>= 123
        实现右移位赋值运算符
        """
        return '__irshift__'

    def __isub__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa -= 123
        实现减法赋值操作
        """
        return '__isub__'

    def __iter__(self):
        """
        >>> medusa = iter(MedusaSorcerer())
        >>> next(medusa)
        创建可迭代对象需要实现的方法, 并需要实现__next__方法
        """
        self.integer = 0
        return self

    def __itruediv__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa /= 123
        实现就地除法运算
        Python2中在 from __future__ import division 下才有用
        """
        return '__itruediv__'

    def __ixor__(self, other):
        """
        >>> medusa = MedusaSorcerer()
        >>> medusa ^= 123
        实现就地按位异或运算
        """
        return '__ixor__'

    def __le__(self, other):
        """
        >>> MedusaSorcerer() <= 123
        定义小于等于操作符行为
        """
        return '__le__'

    def __len__(self):
        """
        >>> len(MedusaSorcerer())
        返回容器的长度
        """
        return len(self.params)

    def __long__(self):
        """
        >>> long(MedusaSorcerer)
        Python2需要实现的Long类型转换
        """
        return '__long__'

    def __lshift__(self, other):
        """
        >>> MedusaSorcerer() << 123
        实现左移位运算符
        """
        return '__lshift__'

    def __lt__(self, other):
        """
        >>> MedusaSorcerer() < 123
        定义小于操作符行为
        """
        return '__lt__'

    def __matmul__(self, other):
        """
        查阅 PEP465:
        https://www.python.org/dev/peps/pep-0465/#specification

        官方中文文档 (无说明文档):
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__imatmul__#object.__matmul__
        """
        pass

    def __missing__(self, key):
        """
        >>> class Dict(dict):
        >>>     def __missing__(self, key): return f'__missing__({key})'
        >>> medusa = Dict({'1': 1})
        >>> print(medusa['123'])
        在字典的子类中使用, 访问字典类型的实例中不存在的Key值将会调用该方法
        """
        pass

    def __mod__(self, other):
        """
        >>> MedusaSorcerer() % 123
        实现取余运算操作
        """
        return '__mod__'

    def __mro_entries__(self, bases):
        """
        如果在类定义中出现的基类不是 type 的实例, 则使用 __mro_entries__ 方法对其进行搜索
        当找到结果时, 它会以原始基类元组做参数进行调用
        此方法必须返回类的元组以替代此基类被使用
        元组可以为空, 在此情况下原始基类将被忽略
        具体参阅 PEP560

        官方中文文档:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__imatmul__#resolving-mro-entries
        https://www.python.org/dev/peps/pep-0560/#mro-entries
        """
        pass

    def __mul__(self, other):
        """
        >>> MedusaSorcerer() * 123
        实现乘法运算操作
        """
        return '__mul__'

    def __ne__(self, other):
        """
        >>> MedusaSorcerer() != 123
        定义不等判断行为
        """
        return '__ne__'

    def __neg__(self):
        """
        >>> -MedusaSorcerer()
        实现取负行为的方法
        """
        return '__neg__'

    def __new__(cls, *args, **kwargs):
        """
        >>> MedusaSorcerer()
        类对象实例化时将会首先调度该方法
        """
        if '__getnewargs__' in args: return 123
        return super().__new__(cls)

    def __next__(self):
        """
        >>> medusa = iter(MedusaSorcerer())
        >>> next(medusa)
        创建迭代对象需要实现的方法, 并需要实现__iter__方法
        """
        self.integer += 1
        return self.integer

    def __oct__(self):
        """
        >>> oct(MedusaSorcerer())
        实现八进制数据转换
        此处被__index__方法覆盖
        """
        return '__oct__'

    def __or__(self, other):
        """
        >>> MedusaSorcerer() | 132
        实现按位或运算符
        """
        return '__or__'

    def __pos__(self):
        """
        >>> +MedusaSorcerer()
        实现取正行为的方法
        """
        return '__pos__'

    def __pow__(self, power, modulo=None):
        """
        >>> MedusaSorcerer() ** 123
        实现幂值运算操作
        """
        return '__pow__'

    @classmethod
    def __prepare__(metacls, name, bases):
        """
        >>> MedusaSorcerer()
        __prepare__只在元类中有用, 而且必须声明为类方法
        主要功能是罗列类的属性定义的顺序
        第一个参数是元类, 随后两个参数分别是要构建的类的名称和基类组成的元组, 返回值必须是映射数据
        元类构建新类时, 解释器会先调用__prepare__方法, 使用类定义体中的属性创建映射
        接着把__prepare__方法返回的映射会传给__new__方法的最后一个参数
        然后再传给__init__方法
        此处我们传递的是一个空的OrderedDict实例对象
        """
        return collections.OrderedDict()

    def __radd__(self, other):
        """
        >>> 123 + MedusaSorcerer()
        实现反射加法操作
        """
        return '__radd__'

    def __rand__(self, other):
        """
        >>> 123 & MedusaSorcerer()
        实现反射按位与运算符
        """
        return '__rand__'

    def __rdiv__(self, other):
        """
        >>> 123 / MedusaSorcerer()
        实现反射除法
        Python3 失效
        """
        return '__rdiv__'

    def __rdivmod__(self, other):
        """
        >>> divmod(123, MedusaSorcerer())
        返回反射 (整数, 取余) 的元组数组
        """
        return '__rdivmod__'

    def __reduce__(self):
        """
        >>> pickle.dumps(MedusaSorcerer())
        当定义扩展类型时, 也就是使用Python的C语言API实现的类型
        如果你想pickle它们, 你必须告诉Python如何pickle它们
        __reduce__ 被定义之后, 当对象被Pickle时就会被调用
        它要么返回一个代表全局名称的字符串, Python会查找它并pickle
        要么返回一个元组, 这个元组包含2到5个元素:
            一个可调用的对象, 用于重建对象时调用
            一个参数元素, 供那个可调用对象使用
            被传递给 __setstate__ 的状态(可选)
            一个产生被pickle的列表元素的迭代器(可选)
            一个产生被pickle的字典元素的迭代器选可
        """
        return super().__reduce__()

    def __reduce_ex__(self, protocol):
        """
        >>> pickle.dumps(MedusaSorcerer())
        __reduce_ex__的存在是为了兼容性
        如果它被定义, 在pickle时__reduce_ex__会代替__reduce__被调用
        """
        return super().__reduce_ex__(protocol)

    def __repr__(self):
        """
        >>> repr(MedusaSorcerer())
        返回对象转化为供解释器读取的形式的数据
        """
        return '__repr__'

    def __reversed__(self):
        """
        >>> reversed(MedusaSorcerer())
        返回一个反转的迭代器
        """
        return '__reversed__'

    def __rfloordiv__(self, other):
        """
        >>> 123 // MedusaSorcerer()
        实现反射整除运算
        """
        return '__rfloordiv__'

    def __rlshift__(self, other):
        """
        >>> 123 << MedusaSorcerer()
        实现反射左位移运算
        """
        return '__rlshift__'

    def __rmatmul__(self, other):
        """
        PEP465 (无说明文档)：
        https://www.python.org/dev/peps/pep-0465/#specification
        官方中文文档 (无说明文档):
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__rmatmul__#object.__rmatmul__
        """
        pass

    def __rmod__(self, other):
        """
        >>> 123 % MedusaSorcerer()
        实现反射取余操作符
        """
        return '__rmod__'

    def __rmul__(self, other):
        """
        >>> 123 * MedusaSorcerer()
        实现反射乘法操作
        """
        return '__rmul__'

    def __ror__(self, other):
        """
        >>> 123 | MedusaSorcerer()
        实现反射按位或运算符
        """
        return '__ror__'

    def __round__(self, n=None):
        """
        >>> round(MedusaSorcerer())
        实现浮点数n的四舍五入值
        """
        return '__round__'

    def __rpow__(self, other):
        """
        >>> 123 ** MedusaSorcerer()
        反射幂值运算操作符
        """
        return '__rpow__'

    def __rrshift__(self, other):
        """
        >>> 123 >> MedusaSorcerer()
        实现反射右位移操作
        """
        return '__rrshift__'

    def __rshift__(self, other):
        """
        >>> MedusaSorcerer() >> 123
        实现右位移操作
        """
        return '__rshift__'

    def __rsub__(self, other):
        """
        >>> 123 - MedusaSorcerer()
        实现反射减法操作
        """
        return '__rsub__'

    def __rtruediv__(self, other):
        """
        >>> 123 / MedusaSorcerer()
        实现_true_反射除法
        Python2 这个函数只有使用from __future__ import division时才有作用
        Python3 全局生效
        """
        return '__rtruediv__'

    def __rxor__(self, other):
        """
        >>> 123 ^ MedusaSorcerer()
        实现反射按位异或运算符
        """
        return '__rxor__'

    def __set__(self, instance, value):
        """
        >>> class Test: medusa = MedusaSorcerer()
        >>> Test().medusa = 1
        在其拥有者对其进行修改值的时候调用
        一个类要成为描述器, 必须实现__get__, __set__, __delete__ 中的至少一个方法
        """
        instance.params = value

    def __set_name__(self, owner, name):
        """
        在所有者类 owner 创建时被调用, 描述器会被赋值给 name
        官方中文文档:
        https://docs.python.org/zh-cn/3/reference/datamodel.html?highlight=__set_name__#object.__set_name__
        https://www.python.org/dev/peps/pep-0487/#proposal
        """
        pass

    def __setattr__(self, key, value):
        """
        >>> self.params = 123
        实例对象设置实例属性的时候将会调度该方法
        """
        self.__dict__[key] = value

    def __setitem__(self, key, value):
        """
        >>> MedusaSorcerer()['key'] = 123
        使用键值方式增加元素值
        """
        self.__dict__[key] = value

    def __setslice__(self, i, j, sequence):
        """
        __getslice__、__setslice__、__delslice__：用于分片的三个操作
        Python3中已经废弃
        """
        pass

    def __setstate__(self, state):
        """
        >>> pickle.loads(pickle.dumps(MedusaSorcerer()))
        当一个对象被反pickle时, 如果定义了__setstate__, 对象的状态会传递给这个魔法方法
        而不是直接应用到对象的__dict__属性
        这个魔法方法和__getstate__相互依存
        当这两个方法都被定义时, 你可以在Pickle时使用任何方法保存对象的任何状态

        在 unpickling 之后还原对象的状态
        """
        pass

    def __sizeof__(self):
        """
        >>> sys.getsizeof(MedusaSorcerer())
        返回对象的大小
        """
        return 123

    def __str__(self):
        """
        >>> str(MedusaSorcerer())
        >>> print(MedusaSorcerer())
        返回字符串调度的方法
        """
        return '__str__'

    def __sub__(self, other):
        """
        >>> MedusaSorcerer() - 123
        实现了加号运算
        """
        return '__sub__'

    def __subclasscheck__(self, subclass):
        """
        >>> issubclass(MedusaSorcerer(), MedusaSorcerer)
        对实例使用issubclass(subclass, class)时调用
        它会判断subclass否是该类的子类
        返回会与__instancecheck__一致, 忽略该方法
        """
        pass

    def __truediv__(self, other):
        """
        >>> MedusaSorcerer() // 123
        实现了整除运算
        Python2 只有你声明了from __future__ import division该方法才会生效
        """
        return '__truediv__'

    def __trunc__(self):
        """
        >>> math.trunc(MedusaSorcerer())
        实现了math.trunc(), 向0取整
        """
        return '__trunc__'

    def __unicode__(self):
        """
        >>> unicode(MedusaSorcerer())
        Python2 中实现unicode转码
        """
        pass

    def __xor__(self, other):
        """
        >>> MedusaSorcerer() ^ 123
        实现按位异或运算符
        """
        return '__xor__'

