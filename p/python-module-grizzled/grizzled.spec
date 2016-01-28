%define oname grizzled

%def_with python3

Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20120525.1
Summary: The Grizzled Python Utility Library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/grizzled-python
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/bmc/grizzled-python.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-enum
#BuildPreReq: python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-enum
%endif

%py_provides %oname
%py_requires enum

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-enum python-module-epydoc python-module-html5lib python-module-nose python-module-pytest python3-module-nose python3-module-pytest rpm-build-python3 time

%description
The Grizzled Utility Library is a general-purpose Python library with a
variety of different modules and packages. It's roughly organized into
subpackages that group different kinds of utility functions and classes.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The Grizzled Utility Library is a general-purpose Python library with a
variety of different modules and packages. It's roughly organized into
subpackages that group different kinds of utility functions and classes.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: The Grizzled Python Utility Library
Group: Development/Python3
%py3_provides %oname
%py3_requires enum

%description -n python3-module-%oname
The Grizzled Utility Library is a general-purpose Python library with a
variety of different modules and packages. It's roughly organized into
subpackages that group different kinds of utility functions and classes.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
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

python run-epydoc.py

%check
nosetests -vv
#if_with python3
%if 0
pushd ../python3
nosetests3 -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/test

%files docs
%doc epydoc/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1.git20120525.1
- NMU: Use buildreq for BR.

* Tue Aug 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20120525
- Initial build for Sisyphus

