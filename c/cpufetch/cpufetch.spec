%define _unpackaged_files_terminate_build 1

Name: cpufetch
Version: 1.06
Release: alt1

Summary: Simple yet fancy CPU architecture fetching tool
License: GPL-2.0
Group: Monitoring
Url: https://github.com/Dr-Noob/cpufetch
Source: %name-%version.tar
Patch1: alt-fix-format-and-path-for-doc.patch

%description
cpufetch is a command-line tool written in C that displays
the CPU information in a clean and beautiful way.

%description -l ru_RU.UTF-8
cpufetch — это инструмент командной строки, написанный на C, который отображает
информацию о процессоре в чистом и красивом виде.

%prep
%setup
%patch1 -p1

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.*

%doc README.md LICENSE

%changelog
* Mon Aug 19 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.06-alt1
- Updated to version 1.06.

* Wed May 08 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.05-alt1
- Initial build for ALT.
