%define oname llist

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.git20130101.1
Summary: Linked list data structures for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/llist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ajakubek/python-llist.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-pluggy python-module-py python-module-setuptools python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-pytest python3-devel rpm-build-python3 time python3-module-pytest

%description
llist is an extension module for CPython providing basic linked list
data structures. Collections implemented in the llist module perform
well in problems which rely on fast insertions and/or deletions of
elements in the middle of a sequence. For this kind of workload, they
can be significantly faster than collections.deque or standard Python
lists.

%package -n python3-module-%oname
Summary: Linked list data structures for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
llist is an extension module for CPython providing basic linked list
data structures. Collections implemented in the llist module perform
well in problems which rely on fast insertions and/or deletions of
elements in the middle of a sequence. For this kind of workload, they
can be significantly faster than collections.deque or standard Python
lists.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
#if_with python3
%if 0
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
popd
%endif

%files
%doc CHANGES README docs/*.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20130101.1
- NMU: Use buildreq for BR.

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20130101
- Initial build for Sisyphus

