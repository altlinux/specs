%def_with python3

%define modulename Automat
Name: python-module-automat
Version: 0.6.0
Release: alt1

Summary: Self-service finite-state machines for the programmer on the go

Url: https://github.com/glyph/Automat
License: MIT
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>


# Source-url: https://pypi.io/packages/source/A/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools python-module-docutils
BuildRequires: python-module-mistune python-module-m2r python-module-setuptools_scm

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-docutils
BuildRequires: python3-module-mistune python3-module-m2r python3-module-setuptools_scm
%endif

#setup_python_module %modulename

%description
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).


%package -n python3-module-automat
Summary: Tool and library for manipulating LiautomatPond files
Group: Development/Python3

%description -n python3-module-automat
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).


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
rm -f %buildroot%python_sitelibdir/automat/_test/test_visualize.*
rm -f %buildroot%python_sitelibdir/automat/_visualize.*

%if_with python3
pushd ../python3
%python3_install
rm -f %buildroot%python3_sitelibdir/automat/_test/test_visualize.*
rm -f %buildroot%python3_sitelibdir/automat/_visualize.*
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-automat
# TODO: tools
#_bindir/automat-visualize
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for ALT Sisyphus

