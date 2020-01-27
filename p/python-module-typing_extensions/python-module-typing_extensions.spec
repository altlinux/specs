%def_without check
%def_with python3
%def_without python2

%define modulename typing_extensions
Name: python-module-typing_extensions
Version: 3.7.4.1
Release: alt1

Summary: Backported and Experimental Type Hints for Python 3.5+

Url: https://github.com/python/typing
License: Python license
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/t/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%if_with python2
BuildRequires: python-dev python-module-setuptools
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Backported and Experimental Type Hints for Python 3.5+.

%package -n python3-module-typing_extensions
Summary: Backported and Experimental Type Hints for Python 3.5+
Group: Development/Python3

%description -n python3-module-typing_extensions
Backported and Experimental Type Hints for Python 3.5+.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with python2
%files
%doc README.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-typing_extensions
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 3.7.4.1-alt1
- initial build for ALT Sisyphus

