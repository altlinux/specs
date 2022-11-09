Name: python3-module-chacha20poly1305-reuseable
Version: 0.0.4
Release: alt1

Summary: ChaCha20Poly1305 that is reuseable for asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/chacha20poly1305-reuseable/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/chacha20poly1305_reuseable
%python3_sitelibdir/chacha20poly1305_reuseable-%version.dist-info

%changelog
* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.4-alt1
- 0.0.4 released

