%define _unpackaged_files_terminate_build 1

Name: admx-msi-setup
Version: 0.1.0
Release: alt2

Summary: ADMX msi file downloader and extractor
License: GPLv2+
Group: Other
Url: https://github.com/altlinux/admx-msi-setup

BuildArch: noarch

Requires: msitools, wget

Source0: %name-%version.tar

%description
Downloads specified ADMX package and extracts it in desired location.

%prep
%setup -q

%install
mkdir -p %buildroot/%_bindir
install -D %name.sh %buildroot/%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Sun Jul 18 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt2
- Build as noarch
- Replace renamed project to github.com/altlinux projects

* Wed Jul 14 2021 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt1
- Initial build

