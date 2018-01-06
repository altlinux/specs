Name: libtermkey
Version: 0.20
Release: alt1

Summary: terminal keypress reading library
License: MIT
Group: System/Libraries

Url: http://www.leonerd.org.uk/code/libtermkey/
Source: %name-%version.tar
Packager: Konstantin Artyushkin <akv@altlinux.org>

BuildRequires: libncurses-devel

%description
termkey is a library that allows programs to read and interpret
keypress and other events from a terminal. It understands encoding
schemes used by terminals to encode keypresses, and UTF-8, allowing
it to return events representing key events.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name

%prep
%setup

%build
%make_build PREFIX=%_usr LIBDIR=%_libdir

%install
%makeinstall_std PREFIX=%_usr LIBDIR=%_libdir

%files
%doc LICENSE
%_libdir/*.so.*
%_man3dir/termkey*
%_man7dir/termkey*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-static
%_libdir/%name.a

%changelog
* Sat Jan 06 2018 Michael Shigorin <mike@altlinux.org> 0.20-alt1
- 0.20
  + NB: this library is officially deprecated in vafour of libtickit
- fixed build on non-x86
- minor spec cleanup

* Fri Dec 18 2015 Konstantin Artyushkin <akv@altlinux.org> 0.18-alt1
- initial build for ALT Linux Sisyphus




