%define oname backports.functools_lru_cache

%def_without python3

Name:           python-module-%oname
Version:        1.4
Release:        alt1
Summary:        Backport of functools.lru_cache from Python 3.3 as published at ActiveState.
Group:          Development/Python
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/backports.functools_lru_cache

# https://github.com/jaraco/backports.functools_lru_cache.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(pytest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(pytest)
%endif

%py_requires backports
%py_provides backports.functools_lru_cache

%description
Backport of functools.lru_cache from Python 3.3 as published at ActiveState.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        Backport of functools.lru_cache from Python 3.3 as published at ActiveState.
%py3_provides backports.functools_lru_cache

%description -n python3-module-%oname
Backport of functools.lru_cache from Python 3.3 as published at ActiveState.
%endif

%prep
%setup

# don't use scm to determine version, just substitute it
sed -i \
	-e 's|setuptools_scm|setuptools|g' \
	-e "s|use_scm_version=.*|version='%version',|g" \
	setup.py

%if_with python3
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
rm -f %buildroot%python3_sitelibdir/backports/__init__.py*
popd
%endif

%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

rm -f %buildroot%python_sitelibdir/backports/__init__.py*

%if_with python3
rm -f %buildroot%python3_sitelibdir/backports/__init__.py*
%endif

%check
%if_with python3
pushd ../python3
py.test3
popd
%endif

py.test

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt1
- Initial build for ALT.
