Name: python3-module-chacha20poly1305
Version: 0.0.3
Release: alt1

Summary: Python implementation of ChaCha20-Poly1305
License: LGPLv2.1
Group: Development/Python
Url: https://pypi.org/project/chacha20poly1305/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/chacha20poly1305
%python3_sitelibdir/chacha20poly1305-%version.dist-info

%changelog
* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.3-alt1
- 0.0.3 released

