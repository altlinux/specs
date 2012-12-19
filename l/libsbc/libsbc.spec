Name: libsbc
Version: 1.0
Release: alt1
Summary: Sub Band Codec used by bluetooth A2DP
Group: System/Libraries
License: GPLv2 and LGPLv2+
URL: http://www.bluez.org

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
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

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
* Wed Dec 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- 1.0

