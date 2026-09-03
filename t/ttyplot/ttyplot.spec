%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: ttyplot
Version: 1.7.6
Release: alt1

Summary: Realtime plotting utility for text mode consoles and terminals
License: Apache-2.0
Group: Monitoring
Url: https://github.com/tenox7/ttyplot
Vcs: https://github.com/tenox7/ttyplot.git

Source: %name-%version.tar

BuildRequires: libncursesw-devel

%description
ttyplot is a realtime plotting utility for text mode consoles and terminals
that reads data from standard input or a Unix pipeline.

%prep
%setup

%build
CPPFLAGS="-D_FILE_OFFSET_BITS=64" CFLAGS="%optflags" %make_build

%install
%makeinstall_std PREFIX=%prefix MANPREFIX=%_mandir

%files
%doc README.md LICENSE
%_bindir/ttyplot
%_mandir/man1/ttyplot.1*

%changelog
* Fri Aug 07 2026 Georgij Tsarin <crystarm@altlinux.org> 1.7.6-alt1
- Initial build for ALT Sisyphus.
