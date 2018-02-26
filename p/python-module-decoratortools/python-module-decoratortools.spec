%define modulename decoratortools
%define oname DecoratorTools

Name: python-module-%modulename
Version: 1.8
Release: alt1.1

%setup_python_module %modulename

Summary: Use class and function decorators -- even in Python 2.3
License: PSF or ZPL
Group: Development/Python

Url: http://pypi.python.org/pypi/DecoratorTools

Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
BuildArch: noarch

Source: http://pypi.python.org/packages/source/D/DecoratorTools/%oname-%version.tar

BuildPreReq: %py_dependencies setuptools

Requires: python-module-peak

%description
Want to use decorators, but still need to support Python 2.3? Wish you
could have class decorators, decorate arbitrary assignments, or match
decorated function signatures to their original functions? Want to get
metaclass features without creating metaclasses? How about synchronized
methods?

"DecoratorTools" gets you all of this and more.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/peak/util/decorators*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt1.1
- Rebuild with Python-2.7

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- build new version
- move to build from tarball scheme

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2.1
- Rebuilt with python 2.6

* Mon Apr 06 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7-alt2
- Avoid file conflict with python-module-peak and add dependency on it

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7-alt1
- Initial build for Sisyphus

