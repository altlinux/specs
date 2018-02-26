Name: libcue
Version: 1.3.0
Release: alt1

Summary: Cue sheet parser library

Group: System/Libraries
# Files libcue/rem.{c,h} contains a BSD header
License: GPLv2 and BSD
Url: http://libcue.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2

# Automatically added by buildreq on Sat Dec 05 2009
BuildRequires: flex gcc-c++

%description
Libcue is intended for parsing a so-called cue sheet from a char string or
a file pointer. For handling of the parsed data a convenient API is available.

%package devel
Summary: Development files
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for %name.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/libcue.la

%files
%_libdir/%name.so.*
%doc AUTHORS COPYING NEWS

%files devel
%_includedir/%name-1.3/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Sat Dec 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Nov 16 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-2
- Changed %%description a bit
- Corrected license field
- Fixed Source0 value
- Fixed Group tag for main package

* Mon Nov  9 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Initial package for Fedora

