%define modulename graph

%def_with python3

Name: python-module-%modulename
Version: 1.8.1
Release: alt1.1.1.1

Summary: library for working with graphs in Python
License: MIT
Group: Development/Python

Url: http://code.google.com/p/python-graph/
BuildArch: noarch

Source: python-module-%modulename-%version.tar

#BuildPreReq: %py_dependencies setuptools
Provides: python-module-pygraph

%setup_python_module %modulename
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
%endif

%description
This software provides a suitable data structure for
representing graphs and a whole set of important algorithms.

%if_with python3
%package -n python3-module-%modulename
Summary: library for working with graphs in Python 3
Group: Development/Python3

%description -n python3-module-%modulename
This software provides a suitable data structure for
representing graphs and a whole set of important algorithms.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
cd core
%python_build
cd ../dot
%python_build
cd ..
%if_with python3
pushd ../python3
pushd core
%python3_build
popd
pushd dot
%python3_build
popd
popd
%endif

%install
cd core
%python_install
cd ../dot
%python_install
cd ..

touch %buildroot%python_sitelibdir/pygraph/__init__.py

%if_with python3
pushd ../python3
pushd core
%python3_install
popd
pushd dot
%python3_install
popd
popd
touch %buildroot%python3_sitelibdir/pygraph/__init__.py
%endif

# TODO: split to subpackages "core" and "dot"

%files
%doc  Changelog README
%python_sitelibdir/pygraph
%python_sitelibdir/*.egg-info
%python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%modulename
%doc  Changelog README
%python3_sitelibdir/pygraph
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.1-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1.1.1
- NMU: Use buildreq for BR.

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8.1-alt1.1
- Rebuild with Python-3.3

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.0-alt2.1
- Rebuild with Python-2.7

* Tue May 18 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7.0-alt2
- Provide python2.6(pygraph).

* Thu May 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.

