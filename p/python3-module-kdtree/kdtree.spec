Name: python3-module-kdtree
Version: 0.16
Release: alt2

Summary: A Python implementation of a kd-tree
License: ISC
Group: Development/Python3

Url: https://pypi.org/project/kdtree/
Vcs: https://github.com/stefankoegl/kdtree

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Provides: python3-module-libkdtree++ = %EVR
Obsoletes: python3-module-libkdtree++ < %EVR

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md LICENSE
%python3_sitelibdir/*

%changelog
* Mon Feb 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.16-alt2
- added obsoletes and provides (ALT #52916)

* Tue Jan 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.16-alt1
- Initial build for Sisyphus

