Name: libsbc
Version: 1.2
Release: alt1.1

Summary: Sub Band Codec used by bluetooth A2DP
License: GPLv2 and LGPLv2+
Group: System/Libraries

Url: http://www.bluez.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libsndfile-devel

%description
SBC (Sub Band Codec) is a low-complexity audio codec used in the Advanced Audio
Distribution Profile (A2DP) bluetooth standard but can be used standalone. It
uses 4 or 8 subbands, an adaptive bit allocation algorithm in combination with
an adaptive block PCM quantizers.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with %name

%package -n sbcinfo
Summary: Sub Band Codec analyzer
Group: Sound
Requires: %name = %version-%release

%description -n sbcinfo
Bluetooth low-complexity, Sub Band Codec analyzer.

%prep
%setup
%patch -p1
%ifarch e2k
sed -i -e 's,-fgcse-after-reload,,' -e 's,-funswitch-loops,,' Makefile.am
%endif

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc COPYING AUTHORS ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/sbc
%_pkgconfigdir/*.pc
%_libdir/*.so

%files -n sbcinfo
%_bindir/sbc*

%changelog
* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.2-alt1.1
- E2K: avoid lcc-unsupported options
- minor spec cleanup

* Fri Jan 24 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- 1.2

* Tue Jun 25 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Wed Dec 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- 1.0

