Name: getnf
Version: 20231218
Release: alt1
Summary: A better way to install NerdFonts
License: GPL-3.0
Group: Other
Url: https://github.com/ronniedroid/getnf
Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -m 0755 %name %buildroot%_bindir

%files
%_bindir/%name

%changelog
* Mon Jan 01 2024 Alexander Makeenkov <amakeenk@altlinux.org> 20231218-alt1
- Initial build for ALT.

