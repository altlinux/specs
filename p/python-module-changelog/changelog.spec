%define _unpackaged_files_terminate_build 1
%define oname changelog

%def_with python3

Name: python-module-%oname
Version: 0.3.5
Release: alt2.1
Summary: Provides simple Sphinx markup to render changelog displays
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/changelog/

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sphinx
%endif

%py_provides %oname

%description
A Sphinx extension to generate changelog files.

This is an experimental, possibly-not-useful extension that's used by
the SQLAlchemy project and related projects.

%if_with python3
%package -n python3-module-%oname
Summary: Provides simple Sphinx markup to render changelog displays
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Sphinx extension to generate changelog files.

This is an experimental, possibly-not-useful extension that's used by
the SQLAlchemy project and related projects.
%endif

%prep
%setup -n %{oname}-%{version}

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.5-alt2
- Enabled build for python-3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1
- automated PyPI update

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

