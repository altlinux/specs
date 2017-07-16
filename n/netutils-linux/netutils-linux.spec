Name:    netutils-linux
Version: 2.3.0
Release: alt1

Summary: A suite of utilities simplilfying linux networking stack performance troubleshooting and tuning.
License: MIT
Group:   Development/Python
URL:     https://github.com/strizhechenko/netutils-linux

Packager: Evgenii Terechkov <evg@altlinux.ru>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
%summary

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/netutils_linux*

%changelog
* Sun Jul 16 2017 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- 2.3.0

* Fri Jul 14 2017 Terechkov Evgenii <evg@altlinux.org> 2.2.4-alt1
- Initial build for ALT Linux Sisyphus
- v2.2.4-10-g3be4091
