Name: getnf
Version: 0.3.0
Release: alt1
Epoch: 1
Summary: A better way to install NerdFonts
License: GPL-3.0
Group: Other
Url: https://github.com/ronniedroid/getnf
Source: %name-%version.tar

BuildArch: noarch

%description
Easily install Nerd Fonts from the terminal.

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -m 0755 %name %buildroot%_bindir

%files
%_bindir/%name
%doc LICENSE

%changelog
* Fri Jun 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1:0.3.0-alt1
- Updated to version 0.3.0.

* Sat Aug 16 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1:0.2.0-alt1
- Updated to version 0.2.0.

* Mon Jan 01 2024 Alexander Makeenkov <amakeenk@altlinux.org> 20231218-alt1
- Initial build for ALT.
