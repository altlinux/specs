%define oname pg8000

%def_with python3

Name: python-module-%oname
Version: 1.11.0
Release: alt1.1
Summary: PostgreSQL interface library
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pg8000/

# https://github.com/mfenniak/pg8000.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-pytz
BuildRequires: python-modules-json
BuildRequires: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-pytz
BuildRequires: python3-module-six
%endif

%py_provides %oname

%description
pg8000 is a Pure-Python interface to the PostgreSQL database engine. It
is one of many PostgreSQL interfaces for the Python programming
language. pg8000 is somewhat distinctive in that it is written entirely
in Python and does not rely on any external libraries (such as a
compiled python module, or PostgreSQL's libpq library). pg8000 supports
the standard Python DB-API version 2.0.

pg8000's name comes from the belief that it is probably about the 8000th
PostgreSQL interface for Python.

%if_with python3
%package -n python3-module-%oname
Summary: PostgreSQL interface library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pg8000 is a Pure-Python interface to the PostgreSQL database engine. It
is one of many PostgreSQL interfaces for the Python programming
language. pg8000 is somewhat distinctive in that it is written entirely
in Python and does not rely on any external libraries (such as a
compiled python module, or PostgreSQL's libpq library). pg8000 supports
the standard Python DB-API version 2.0.

pg8000's name comes from the belief that it is probably about the 8000th
PostgreSQL interface for Python.
%endif

%prep
%setup

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
	%oname/_version.py

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc README*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.0-alt1
- Updated to upstream version 1.11.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.2-alt1.git20150629.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1.git20150629.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1.git20150629
- Initial build for Sisyphus

