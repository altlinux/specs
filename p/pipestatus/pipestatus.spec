Name: pipestatus
Version: 0.7.0
Release: alt2

Summary: UNIX/POSIX shell helper for running pipes safely
License: Unlicense
Group: Development/Other

Url: http://pipestatus.sourceforge.net/
Source: %name-%version.tar.gz
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: mk-configure >= 0.34.2-alt4
BuildRequires: rpm-macros-mk-configure

# For testing
BuildRequires: zsh mksh pdksh ash sh4 oksh

%description
pipestatus - source file for UNIX/POSIX shell that allows
to obtain an exit status of every program in a pipe.

%prep
%setup

%build
%mkc_env
%mkcmake_configure
%mkcmake_build

%check
%mkc_env
%mkcmake -j1 test_all NAMES='sh4 pdksh ksh mksh ash sh bash zsh oksh'

%install
%mkc_env
%mkcmake_install

%files
%doc NEWS README pipestatus_demo
%_bindir/*

%changelog
* Sun Jan 10 2021 Aleksey Cheusov <cheusov@altlinux.org> 0.7.0-alt2
- Fix License

* Fri Jan 08 2021 Aleksey Cheusov <cheusov@altlinux.org> 0.7.0-alt1
- 0.7.0

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.6.0-alt1
- Initial version for AltLinux
