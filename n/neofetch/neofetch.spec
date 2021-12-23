%define _unpackaged_files_terminate_build 1

Name: neofetch
Version: 7.1.0
Release: alt2
Summary: A command-line system information tool
License: MIT
Group: Monitoring
Url: https://github.com/dylanaraps/neofetch
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
%filter_from_requires /mate-terminal/d
%filter_from_requires /terminology/d
%filter_from_requires /kitty/d

%description
Neofetch is a command-line system information tool written in bash 3.2+.
Neofetch displays information about your operating system, software and
hardware in an aesthetic and visually pleasing way.

%prep
%setup

%build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1.xz

%changelog
* Thu Dec 23 2021 Alexander Makeenkov <amakeenk@altlinux.org> 7.1.0-alt2
- Filter requires (closes: #41612)

* Sat Jan 09 2021 Alexander Makeenkov <amakeenk@altlinux.org> 7.1.0-alt1
- Updated to version 7.1.0

* Sun Mar 08 2020 Alexander Makeenkov <amakeenk@altlinux.org> 7.0.0-alt1
- New version

* Sat Aug 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 6.1.0-alt1
- New version

* Sun Mar 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 6.0.0-alt1
- Initial build for ALT

