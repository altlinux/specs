%define oname libnacl
%def_without python3

Summary: This library is used to gain direct access to the functions exposed by Daniel J. Bernstein's nacl library via libsodium or tweetnacl
Name: python-module-%oname
Version: 1.5.0
Release: alt2.1
Url: https://github.com/saltstack/libnacl
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ASL 2.0
Group: Development/Python

Requires: libsodium23

BuildArch: noarch
BuildRequires: python-devel python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
This library is used to gain direct access to the functions exposed by
Daniel J. Bernstein's nacl library via libsodium or tweetnacl. It has
been constructed to maintain extensive documentation on how to use nacl
as well as being completely portable. The file in libnacl/__init__.py
can be pulled out and placed directly in any project to give a single
file binding to all of nacl.

%package -n python3-module-%oname
Summary: Flow Based Programming Automated Reasoning Engine and Automation Operation System
Group: Development/Python3

%description -n python3-module-%oname
This library is used to gain direct access to the functions exposed by 
Daniel J. Bernstein's nacl library via libsodium or tweetnacl. It has 
been constructed to maintain extensive documentation on how to use nacl 
as well as being completely portable. The file in libnacl/__init__.py 
can be pulled out and placed directly in any project to give a single 
file binding to all of nacl.

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
%doc AUTHORS LICENSE MANIFEST.in README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS LICENSE MANIFEST.in README.rst
%python3_sitelibdir/*
%endif


%changelog
* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2.1
- NMU: autorebuild with libsodium-1.0.16 (libsodium23)

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.5.0-alt2
- rebuild with libsodium18

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.0-alt1
- New version

* Fri Jun 24 2016 Lenar Shakirov <snejok@altlinux.ru> 1.4.5-alt2
- Requires: libsodium13 added

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.5-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.2-alt1
- New version

* Thu Feb 12 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.0-alt1
- Initial build for ALT

