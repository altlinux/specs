Name: libsmf
Version: 1.3
Release: alt1

Summary: Standard MIDI File format library
License: BSD-2-Clause
Group: System/Libraries
Url: https://github.com/stump/libsmf

Source: %name-%version.tar

BuildRequires: pkgconfig(glib-2.0)

%package devel
Summary: Standard MIDI File format library
Group: Development/C

%description
libsmf is C library for reading and writing Standard MIDI Files (*.mid).
It transparently handles conversions between time and pulses, tempo maps,
and more.

%description devel
libsmf is C library for reading and writing Standard MIDI Files (*.mid).
It transparently handles conversions between time and pulses, tempo maps,
and more.
This package provides development part of libsmf.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
rm %buildroot/{%_bindir/smfsh,%_man1dir/smfsh*}

%files
%doc COPYING README*
%_libdir/libsmf.so.*

%files devel
%_includedir/smf.h
%_libdir/libsmf.so
%_pkgconfigdir/smf.pc

%changelog
* Thu Nov 28 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3-alt1
- 1.3 released
