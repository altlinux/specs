%def_without check
%def_with python3

%define modulename hyperlink
Name: python-module-hyperlink
Version: 17.1.1
Release: alt1

Summary: A featureful, correct URL for Python

Url: https://github.com/mahmoud/hyperlink
License: BSD
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/h/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
The humble, but powerful, URL runs everything around us. Chances
are you've used several just to read this text.

Hyperlink is a featureful, pure-Python implementation of the URL, with
an emphasis on correctness.


%package -n python3-module-hyperlink
Summary: A featureful, correct URL for Python
Group: Development/Python3

%description -n python3-module-hyperlink
The humble, but powerful, URL runs everything around us. Chances
are you've used several just to read this text.

Hyperlink is a featureful, pure-Python implementation of the URL, with
an emphasis on correctness.


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

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-hyperlink
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 17.1.1-alt1
- initial build for ALT Sisyphus

