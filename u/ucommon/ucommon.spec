Name: ucommon
Version: 7.0.0
Release: alt1

%define sover 8
%define libcommoncpp libcommoncpp%sover
%define libucommon libucommon%sover
%define libusecure libusecure%sover

Summary: Portable C++ framework for threads and sockets

Group: System/Libraries
Url: http://www.gnu.org/software/commoncpp
License: LGPLv3+

# Source-url: https://mirror.tochlab.net/pub/gnu/commoncpp/ucommon-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Wed Sep 24 2014 (-bi)
# optimized out: cmake-modules elfutils fontconfig fonts-bitmap-misc libcanberra-devel libcloog-isl4 libcom_err-devel libdrm-devel libgmp-devel libgpg-error-devel libjpeg-devel libkrb5-devel libncurses-devel libpng-devel libpopt-devel libsndfile-devel libssl-devel libstdc++-devel libtinfo-devel libunixODBC-devel libverto-devel libwayland-client libwayland-client-devel libwayland-server pkg-config python-base rpm-build-ruby ruby ruby-stdlibs wayland-devel zlib-devel
#BuildRequires: binutils-devel bzlib-devel cmake doxygen ebook-tools-devel firebird-devel flex fonts-bitmap-terminus fonts-otf-stix fonts-ttf-dejavu fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-type1-urw frei0r-devel gcc-c++ grantlee-devel graphviz id3lib-devel ladspa_sdk libGeoIP-devel libarchive-devel libassuan-devel libaudiofile-devel libaudit-devel libcaca-devel libcanberra-gtk-common-devel libcdparanoia-devel libcheck-devel libchromaprint-devel libclapack-devel libclucene-core-devel libcryptsetup-devel libdb4-devel libdca-devel libdmtx-devel libexpat-devel libfaad-devel libffi-devel libfftw3-devel libfreetds-devel libgadu-devel libgbm-devel libgcrypt-devel libgeos-devel libgif-devel libgpgme-devel libgpm-devel libgps-devel libgsm-devel libhdf5-devel libical-devel libidn-devel libjbig-devel libkmod-devel libksba-devel liblcms2-devel libldap-devel libltdl7-devel liblzma-devel libmad-devel libmicrohttpd-devel libmng-devel libmpeg4ip-devel libmpfr-devel libmtp-devel libnetpbm-devel libomniORB-devel libopenconnect-devel libopenjpeg-devel libopenslp-devel libproxy-devel libpth-devel libqrencode-devel librcc-devel libruby-devel libsamplerate-devel libsox-devel libsqlite-devel libsqlite3-devel libtasn1-devel libtidy-devel libtiff-devel libudev-devel libusb-compat-devel libusbmuxd-devel libutempter-devel libv4l-devel libwayland-cursor-devel libwayland-server-devel libwrap-devel libx264-devel libxapian-devel libxvba-devel libxvid-devel libyaml-devel smokegen-devel swig
BuildRequires: doxygen graphviz libssl-devel cmake gcc-c++

%description
GNU uCommon C++ is a lightweight library to facilitate using C++ design
patterns even for very deeply embedded applications, such as for systems using
uclibc along with POSIX threading support. For this reason, uCommon disables
language features that consume memory or introduce runtime overhead. UCommon
introduces some design patterns from Objective-C, such as reference counted
objects, memory pools, and smart pointers. UCommon introduces some new concepts
for handling of thread locking and synchronization.  Starting with release
5.0, GNU uCommon also bundles GNU Common C++ libraries.

%package utils
Group: Development/C++
Summary: GNU uCommon system and support applications
%description utils
This is a collection of command line tools that use various aspects of the
ucommon library.  Some may be needed to prepare files or for development of
applications.

%package devel
Group: Development/C++
Summary: Headers for building GNU uCommon applications
Requires: libssl-devel
%description devel
This package provides header and support files needed for building
applications that use the uCommon and commoncpp libraries.

%package doc
Group: Development/Documentation
Summary: Generated class documentation for GNU uCommon
%description doc
Generated class documentation for GNU uCommon library from header files in
HTML format.

%package -n %libcommoncpp
Summary: %name library
Group: System/Libraries
%description -n %libcommoncpp
%name library

%package -n %libucommon
Summary: %name library
Group: System/Libraries
%description -n %libucommon
%name library

%package -n %libusecure
Summary: %name library
Group: System/Libraries
%description -n %libusecure
%name library

%prep
%setup

%build
%cmake \
      -DSYSCONFDIR=%_sysconfdir \
      -DINSTALL_MANDIR=%_mandir \
      -DINSTALL_INCLUDEDIR=%_includedir \
      -DINSTALL_BINDIR=%_bindir \
      -DINSTALL_SBINDIR=%_sbindir \
      -DINSTALL_LIBEXEC=%_libexecdir \
      -DINSTALL_LIBDIR=%_libdir \
      #


%cmake_build
%cmake_build doc


%install
#cmake_install DESTDIR=%buildroot
make install -C BUILD DESTDIR=%buildroot

chmod 0755 %buildroot/%_bindir/ucommon-config
chmod 0755 %buildroot/%_bindir/commoncpp-config


%files -n %libcommoncpp
%doc AUTHORS README NEWS SUPPORT ChangeLog
%_libdir/libcommoncpp.so.%sover
%_libdir/libcommoncpp.so.%sover.*
%files -n %libucommon
%doc AUTHORS README NEWS SUPPORT ChangeLog
%_libdir/libucommon.so.%sover
%_libdir/libucommon.so.%sover.*
%files -n %libusecure
%doc AUTHORS README NEWS SUPPORT ChangeLog
%_libdir/libusecure.so.%sover
%_libdir/libusecure.so.%sover.*

%files utils
%_bindir/args
%_bindir/urlout
%_bindir/mdsum
%_bindir/pdetach
%_bindir/sockaddr
%_bindir/zerofill
%_bindir/scrub-files
%_bindir/car
%_bindir/keywait
%_man1dir/args.*
%_man1dir/urlout.*
%_man1dir/car.*
%_man1dir/mdsum.*
%_man1dir/pdetach.*
%_man1dir/scrub-files.*
%_man1dir/sockaddr.*
%_man1dir/zerofill.*
%_man1dir/keywait.*

%files devel
%dir %_datadir/ucommon/
%_libdir/*.so
%_includedir/ucommon/
%_includedir/commoncpp/
%_libdir/pkgconfig/*.pc
%_datadir/ucommon/cmake/
%_bindir/ucommon-config
%_man1dir/ucommon-config.*
%_bindir/commoncpp-config
%_man1dir/commoncpp-config.*

%files doc
%doc BUILD/doc/html/*

%changelog
* Sun Mar 04 2018 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- new version 7.0.0 (with rpmrb script)

* Mon Jun 15 2015 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Thu Oct 23 2014 Sergey V Turchin <zerg@altlinux.org> 6.1.11-alt0.M70P.1
- built for M70P

* Wed Sep 24 2014 Sergey V Turchin <zerg@altlinux.org> 6.1.11-alt1
- initial build
