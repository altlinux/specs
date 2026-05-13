Name: msgextract
Version: 0.5
Release: alt2

Summary: Easily extract the contents of MSG or EML email files

License: GPLv2
Group: File tools
Url: https://altlinux.space/shad/msgextract
Vcs: https://altlinux.space/shad/msgextract

Source: %name-%version.tar

Requires: perl-Email-Outlook-Message-scripts mpack

BuildArch: noarch

%description
A simple script to automate the unpacking of an MSG or EML email message file so that it can be done with one command.

%prep
%setup

%build
%install
install -Dm755 %name.sh %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Thu May 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5-alt2
- changed Url && Vcs

* Mon Jan 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5-alt1
- Added extraction directly from EML file.

* Mon Jul 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4-alt1
- 0.3 -> 0.4

* Fri Mar 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3-alt1
- 0.2 -> 0.3

* Mon Dec 09 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
