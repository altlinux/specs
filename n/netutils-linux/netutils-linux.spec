Name:    netutils-linux
Version: 2.7.9
Release: alt1

Summary: A suite of utilities simplilfying linux networking stack performance troubleshooting and tuning.
License: MIT
Group:   Development/Python3
URL:     https://github.com/strizhechenko/netutils-linux

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/netutils_linux*


%changelog
* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.7.9-alt1
- Version updated to 2.7.9
- python2 -> python3

* Sun Sep  3 2017 Terechkov Evgenii <evg@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sun Jul 16 2017 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- 2.3.0

* Fri Jul 14 2017 Terechkov Evgenii <evg@altlinux.org> 2.2.4-alt1
- Initial build for ALT Linux Sisyphus
- v2.2.4-10-g3be4091
