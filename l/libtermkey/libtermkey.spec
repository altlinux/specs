Name: libtermkey
Version: 0.18
Release: alt1

Summary: termkey - terminal keypress reading library
License: MIT
Group: System/Libraries
Url: http://www.leonerd.org.uk/code/libtermkey/

Packager: Konstantin Artyushkin <akv@altlinux.org>

BuildRequires: libncurses-devel
Source: %name-%version.tar
Patch: libdir.patch

%description
termkey  is  a  library  that allows programs to read and interpret
keypress and other events from a terminal. It understands encoding
schemes used by terminals to encode keypresses, and UTF-8 , allowing
it to return events representing key events

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
%patch

%build
%make_build PREFIX=/usr

%install
%makeinstall_std PREFIX=/usr

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
* Fri Dec 18 2015 Konstantin Artyushkin <akv@altlinux.org> 0.18-alt1
- initial build for ALT Linux Sisyphus




