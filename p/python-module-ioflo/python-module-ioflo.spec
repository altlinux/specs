%define oname ioflo
%def_without python3

Summary: Flow Based Programming Automated Reasoning Engine and Automation Operation System
Name: python-module-%oname
Version: 1.0.2
Release: alt1
Url: https://github.com/ioflo/ioflo.git
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ASL 2.0
Group: Development/Python

BuildArch: noarch
BuildRequires: python-dev python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
IoFlo is configured in a convenient user friendly scripting language
called FloScript.

%package -n python3-module-%oname
Summary: Flow Based Programming Automated Reasoning Engine and Automation Operation System
Group: Development/Python3

%description -n python3-module-%oname
IoFlo is configured in a convenient user friendly scripting language
called FloScript.


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif


%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_build_install --prefix=/usr

%if_with python3
pushd ../python3
%python3_install
popd
%endif



%files
%doc ChangeLog.md LEGAL LICENSE LICENSE-2.0.txt README.md
%python_sitelibdir/*
%_bindir/ioflo

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog.md LEGAL LICENSE LICENSE-2.0.txt README.md
%python3_sitelibdir/*
%_bindir/ioflo
%endif


%changelog
* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.2-alt1
- Initial build for ALT

