%global pkgname jsonpath-rw
%def_with python3

Name: python-module-%pkgname
Version: 1.4.0
Release: alt1.1.1
Summary: Extended implementation of JSONPath for Python
Group: Development/Python

License: ASL 2.0
Url: https://github.com/kennknowles/python-jsonpath-rw
Source: %name-%version.tar

BuildArch: noarch
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-ply
#BuildRequires: python-module-decorator
#BuildRequires: python-module-six

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-ply
#BuildRequires: python3-module-decorator
#BuildRequires: python3-module-six
%endif

%description
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming. It is tested with
Python 2.6, 2.7, 3.2, 3.3, and PyPy.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%if_with python3
%package -n python3-module-%pkgname
Summary: Extended implementation of JSONPath for Python
Group: Development/Python3

%description -n python3-module-%pkgname
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming. It is tested with
Python 2.6, 2.7, 3.2, 3.3, and PyPy.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%endif

%package doc
Summary: Documentation for %name
Group:  Development/Documentation

%description doc
Documentation for %name.

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/jsonpath.py %buildroot%_bindir/python3-jsonpath.py
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/*
%_bindir/jsonpath.py

%if_with python3
%files -n python3-module-%pkgname
%doc README.rst
%python3_sitelibdir/*
%_bindir/python3-jsonpath.py
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0
- cleanup spec
- delete tests from package

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2.3-alt1
- First build for ALT (based on Fedora 1.2.3-4.fc21.src)

