Name: wavpack
Version: 4.60.1
Release: alt1

Summary: Open audio compression codec
License: BSD
Group: Sound
Url: http://www.wavpack.com/
# http://www.wavpack.com/%name-%version.tar.bz2
Source: %name-%version.tar
Patch: wavpack-fc-pkgconfig.patch

Requires: lib%name = %version-%release
BuildRequires: gcc-c++

%def_disable static

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode.  Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer
unparalleled performance and functionality.

%package -n lib%name
Summary: WavPack library
Group: System/Libraries

%description -n lib%name
This package contains WavPack shared library.

%package -n lib%name-devel
Summary: Development files for WavPack library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains development files for WavPack library.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 license.txt ChangeLog doc/* %buildroot%docdir/

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/lib*.so.*
%dir %docdir/
%docdir/license.txt

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/wavpack/
%_pkgconfigdir/*.pc
%docdir/
%exclude %docdir/license.txt

%changelog
* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 4.60.1-alt1
- Updated to 4.60.1.
- Packaged documentation.
- Cleaned up specfile.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 4.50.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 4.50.1-alt1
- new version 4.50 (with rpmrb script)

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 4.41.0-alt1
- new version 4.41.0 (with rpmrb script)

* Mon Jan 15 2007 Vitaly Lipatov <lav@altlinux.ru> 4.40.0-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

