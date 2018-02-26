Version: 1.9.5
Summary: Cisco-like telnet command-line library
Name: libcli
Release: alt1
License: LGPL
Group: System/Libraries
Source: %name-%version.tar
Url: http://github.com/dparrish/libcli
Packager: Evgenii Terechkov <evg@altlinux.org>

%description
libcli provides a shared library for including a Cisco-like command-line
interface into other software. It's a telnet interface which supports
command-line editing, history, authentication and callbacks for a
user-definable function tree.

%package devel
Group: Development/C
Summary: Header files for developing programs using %name
Requires: %name = %version-%release

%description devel
This package contains the header files needed to develop programs
based on %name

%prep
%setup
sed -i 's|/lib|/%_lib|g' Makefile

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%{_libdir}/*.so.*.*
%doc README

%files devel
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Sun Dec 19 2010 Terechkov Evgenii <evg@altlinux.org> 1.9.5-alt1
- Initial build for ALT Linux Sisyphus
