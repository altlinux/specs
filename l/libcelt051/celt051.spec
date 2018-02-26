%define oname celt051

Name: libcelt051
Version: 0.5.1.3
Release: alt2
Summary: The CELT Low-Latency Audio Compression Codec

Group: System/Libraries
License: BSD
Url: http://www.celt-codec.org/

Source: %name-%version.tar

BuildRequires: libogg-devel

%description
CELT (Constrained Energy Lapped Transform) is an ultra-low delay audio
codec designed for realtime transmission of high quality speech and audio.
This is meant to close the gap between traditional speech codecs
(such as Speex) and traditional audio codecs (such as Vorbis).

The CELT bitstream format is not yet stable, this package is a special
version of 0.5.1 that has the same bitstream format, but symbols and files
renamed from 'celt*' to 'celt051*' so that it is parallel installable with
the normal celt for packages requiring this particular bitstream format.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %oname-utils
Summary: CELT codec utilities
Group: Sound
Requires: %name = %version-%release

%description -n %oname-utils
Basic utilities for encoding, decoding and manipulating Ogg CELT streams.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install
rm -f %buildroot%_libdir/*.la

%check
%make check

%files
%doc COPYING README TODO
%_libdir/*.so.*

%files devel
%doc COPYING README
%_includedir/celt051
%_pkgconfigdir/*.pc
%_libdir/*.so

%files -n %oname-utils
%_bindir/celt*

%changelog
* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5.1.3-alt2
- rebuild for debuginfo

* Sat Nov 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.1.3-alt1
- initial build for ALT Linux Sisyphus
