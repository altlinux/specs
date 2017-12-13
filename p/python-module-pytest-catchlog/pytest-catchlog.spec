%define _unpackaged_files_terminate_build 1
%define oname pytest-catchlog

%def_with python3

Name: python-module-%oname
Version: 1.2.2
Release: alt1
Summary: py.test plugin to catch log messages. This is a fork of pytest-capturelog.
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-catchlog

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
%endif

%description
Py.test plugin to catch log messages. This is a fork of pytest-capturelog.

%if_with python3
%package -n python3-module-%oname
Summary: py.test plugin to catch log messages. This is a fork of pytest-capturelog.
Group: Development/Python3

%description -n python3-module-%oname
Py.test plugin to catch log messages. This is a fork of pytest-capturelog.
%endif

%prep
%setup

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
* Wed Dec 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1
- Initial build for ALT.
