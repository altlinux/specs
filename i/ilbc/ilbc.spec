
Name: ilbc
Version: 1.1.1
Release: alt2
%define sover 100
%define libilbc libilbc%sover

Group: System/Libraries
Summary: Internet Low Bitrate Codec (iLBC)
Url: https://github.com/dekkers/libilbc/
License: BSD

Source: %name-%version.tar
# FC
Patch1: ilbc-0001-Don-t-build-silently.patch
# ALT
Patch100: alt-soname.patch

# Automatically added by buildreq on Thu Sep 25 2014 (-bi)
# optimized out: elfutils libcloog-isl4 pkg-config python-base ruby ruby-stdlibs
#BuildRequires: glibc-devel-static rpm-build-ruby
BuildRequires: glibc-devel

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.

%package devel
Summary: development files for %name
Group: Development/C
Conflicts: libilbc1-devel libilbc-devel
%description devel
Additional header files for development with %name.

%package -n %libilbc
Group: System/Libraries
Summary: Internet Low Bitrate Codec (iLBC) library
%description -n %libilbc
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.

%prep
%setup -q
%patch1 -p1
%patch100 -p1
%autoreconf

%build
%add_optflags %optflags_shared
%configure --disable-static
%make_build

%install
%make install DESTDIR=%buildroot

# make compat symlinks
cd %buildroot/%_pkgconfigdir && ln -s libilbc.pc ilbc.pc
cd %buildroot/%_includedir
ln -s ilbc.h iLBC_decode.h
ln -s ilbc.h iLBC_define.h
ln -s ilbc.h iLBC_encode.h

%files -n %libilbc
%doc README COPYING
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files devel
%_includedir/ilbc.h
%_includedir/iLBC_*.h
%_libdir/pkgconfig/*ilbc.pc
%_libdir/lib%name.so

%changelog
* Fri Oct 03 2014 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt2
- update package description

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- initial build (ALT#30353)

