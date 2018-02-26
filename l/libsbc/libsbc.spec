%def_disable static
%define snapdate 20070327

Name: libsbc
Version: 0.0
Release: alt0.cvs.%snapdate.1
Summary: subband codec (SBC) library
License: GPL/LGPL
Group: System/Libraries
URL: http://bluetooth-alsa.sourceforge.net

Packager: L.A. Kostis <lakostis@altlinux.ru>

Source: libsbc-%version.tar
Patch: sbcinfo-deb-man.diff

%description
Bluetooth low-complexity, subband codec (SBC) library.

%package devel
Summary: Development files for subband codec (SBC) library
Group: Development/C
Requires: %name = %version-%release
Provides: libsbc-devel

%description devel
Header files for libsbc library.

%package -n sbcinfo
Summary: Subband codec (SBC) analyzer
Group: Sound
Requires: %name = %version-%release

%description -n sbcinfo
Bluetooth low-complexity, subband codec (SBC) analyzer.

%prep
%setup -q
%patch -p1

%build
%__autoreconf
%configure %{subst_enable static}
%make_build

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot%_man1dir
%__install -pm644 debian/*.1 %buildroot%_man1dir/

%files
%doc AUTHORS README COPYING*
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/*
%_datadir/aclocal/*.m4
%_pkgconfigdir/*.pc

%if_enabled static
%_libdir/lib*.a
%endif #static

%files -n sbcinfo
%_bindir/*
%_man1dir/*

%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0.cvs.20070327.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libsbc
  * postun_ldconfig for libsbc

* Sat Mar 31 2007 L.A. Kostis <lakostis@altlinux.ru> 0.0-alt0.cvs.20070327
- initial build for ALTLinux.
- manpage taken from debian libsbc package.

