%define github_name m2r
%define commit 871d57941e74e29bb66ae6d65fa0517e6001f62a

%def_without check
%def_with python3

%define modulename m2r
Name: python-module-m2r
Version: 0.1.6
Release: alt1

Summary: Markdown to reStructuredText converter

Url: https://github.com/miyakogi/m2r
License: MIT
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/miyakogi/%{github_name}/archive/%{commit}/%{github_name}-%{commit}.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-docutils
BuildRequires: python-module-mistune
BuildRequires: python-module-Pygments
BuildRequires: python-module-mock


BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-docutils
BuildRequires: python3-module-mistune
BuildRequires: python3-module-Pygments
BuildRequires: python3-module-mock
%endif

%description
M2R converts a markdown file including reST markups to a valid reST format.


%package -n python3-module-m2r
Summary: A featureful, correct URL for Python
Group: Development/Python3

%description -n python3-module-m2r
M2R converts a markdown file including reST markups to a valid reST format.


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
%files -n python3-module-m2r
%_bindir/m2r
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- initial build for ALT Sisyphus

