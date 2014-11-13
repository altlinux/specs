%define oname moretools

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20141020
Summary: Many more basic tools for python extending itertools, functools, operator, collections
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/moretools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/userzimmermann/python-moretools.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-zetup python-module-six
BuildPreReq: python-module-decorator
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-zetup python3-module-six
BuildPreReq: python3-module-decorator
%endif

%py_provides %oname

%description
Many more basic tools for python 2/3 extending itertools, functools,
operator and collections.

%package -n python3-module-%oname
Summary: Many more basic tools for python extending itertools, functools, operator, collections
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Many more basic tools for python 2/3 extending itertools, functools,
operator and collections.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
#zetup init

%if_with python3
pushd ../python3
#zetup.py3 init
popd
%endif

%install
#zetup init
install -d %buildroot%python_sitelibdir
cp -fR %oname %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
#zetup.py3 init
install -d %buildroot%python3_sitelibdir
cp -fR %oname %buildroot%python3_sitelibdir/
popd
%endif

%check
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20141020
- Initial build for Sisyphus (bootstrap)

