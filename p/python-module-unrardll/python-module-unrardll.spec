#def_without check
%def_with python3

%define modulename unrardll
Name: python-module-unrardll
Version: 0.1.3
Release: alt1

Summary: Python wrapper for the UnRAR DLL

Url: https://github.com/kovidgoyal/unrardll
License: BSD 3-Clause New or Revised License
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kovidgoyal/unrardll/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires: libunrar libunrar-devel
#setup_python_module %modulename

BuildRequires: rpm-build-intro gcc-c++

%description
Python wrapper for the UNRAR DLL.

%if_with python3
%package -n python3-module-%modulename
Summary: Python wrapper for the UNRAR DLL
Group: Development/Python3

%description -n python3-module-%modulename
Python wrapper for the UNRAR DLL.
%endif


%prep
%setup
%__subst "s|unrar/dll.hpp|libunrar/dll.hpp|" src/unrardll/wrapper.cpp

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
# will failed with LANG=C
export LANG=en_US.UTF8
%python_check test

%if_with python3
pushd ../python3
%python3_check test
popd
%endif

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Sisyphus

