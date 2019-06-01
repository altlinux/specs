%define oname repeated_test

%def_with python2
%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1

Summary: A quick unittest-compatible framework for repeating a test function over many fixtures

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/repeated_test/

# Source-url: https://pypi.io/packages/source/r/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-intro

%if_with python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%endif


%description
A quick unittest-compatible framework for repeating a test function over many fixtures.

%package -n python3-module-%oname
Summary: A quick unittest-compatible framework for repeating a test function over many fixtures
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A quick unittest-compatible framework for repeating a test function over many fixtures.

%prep
%setup
%python3_dirsetup

%build
%if_with python2
%python_build_debug
%endif

%python3_dirbuild_debug

%install
%if_with python2
%python_install
%endif

%python3_dirinstall

%check
%if_with python2
%python_check
%endif
%python3_dircheck

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

