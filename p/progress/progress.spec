%define _unpackaged_files_terminate_build 1

Name: progress
Version: 0.17
Release: alt1
Summary: Linux tool to show progress for cp, mv, dd, ... (formerly known as cv)
License: GPL-3.0
Group: Other
URL: https://github.com/Xfennec/progress
Source: %name-%version.tar

BuildRequires: libncursesw-devel

%description
This tool can be described as a Tiny, Dirty, Linux-and-OSX-Only C command that looks for
coreutils basic commands (cp, mv, dd, tar, gzip/gunzip, cat, etc.) currently running on
your system and displays the percentage of copied data. It can also show estimated time
and throughput, and provides a "top-like" mode (monitoring).

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
install -m 0755 %name %buildroot%_bindir
install -m 0644 %name.1* %buildroot%_man1dir

%files
%_bindir/%name
%_man1dir/%name.1*
%doc LICENSE

%changelog
* Sat Dec 23 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.17-alt1
- Updated to version 0.17.

* Sat May 28 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.16-alt1.gitceb6e78
- Updated to last upstream git

* Wed Jun 10 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.15-alt1
- Updated to version 0.15

* Tue Mar 19 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.14-alt1
- Initial build for ALT

