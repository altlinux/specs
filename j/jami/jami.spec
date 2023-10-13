%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%define IF_ver_eq() %if "%(rpmvercmp '%1' '%2')" == "0"
%define IF_ver_not_gt() %if "%(rpmvercmp '%1' '%2')" <= "0"
%define IF_ver_not_gteq() %if "%(rpmvercmp '%1' '%2')" < "0"
%define IF_ver_not_lt() %if "%(rpmvercmp '%2' '%1')" <= "0"
%define IF_ver_not_lteq() %if "%(rpmvercmp '%2' '%1')" < "0"
%define IF_ver_not_eq() %if "%(rpmvercmp '%1' '%2')" != "0"

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif
%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif

%define rname ring-project
%define _cmake__builddir BUILD
%define _libexecdir %prefix/libexec
%define builddir %_builddir/%name-%version
%define jami_sover 0
%define libjami libjami%jami_sover
%define jamiclient_sover 1.0.0
%define libjamiclient libjamiclient%jamiclient_sover

Name: jami
Version: 20230922
Release: alt3

Group: Networking/Instant messaging
Summary: SIP and IAX2 compatible softphone
Url: https://jami.net/
License: GPL-3.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Source: %name-%version.tar
Source100: ffmpeg-n6.0.tar
Source101: msgpack-c-cpp-6.0.0.tar
Source102: pjproject-97f45c2040c2b0cf6f3349a365b0e900a2267333.tar
Source103: restinio-bbaa034dbcc7555ce67df0f8a1475591a7441733.tar
Source104: opendht-2.6.0.tar
Source105: sdbus-cpp-1.2.0.tar
Source106: gmp-6.2.1.tar
Source107: dhtnet-2f3539bc19cf770cd23912c7eebe63e8d2f80515.tar
Source108: pupnp-release-1.14.18.tar
Source109: libgit2-v1.6.4.tar
Source110: http-parser-2.9.4.tar
Source111: argon2-16d3df698db2486dde480b09a732bf9bf48599f9.tar
Source112: asio-asio-1-22-1.tar
Source113: libnatpmp-20150609.tar
Source114: secp256k1-0b7024185045a49a1a6a4c5615bf31c94f63d9c4.tar
Source115: webrtc-audio-processing-v0.3.1.tar
Source116: jsoncpp-1.9.3.tar

Source120: ffmpeg-remove-x86-optimization.patch
Patch3: alt-armh.patch
Patch4: alt-ppc.patch
Patch5: alt-qt-build.patch
Patch6: alt-link.patch
Patch7: ffmpeg-remove-x86-optimization-add.patch
Patch8: alt-include.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: cmake gcc-c++ glibc-devel autoconf-archive
BuildRequires: asio-devel libnatpmp-devel
BuildRequires: libsystemd-devel
BuildRequires: doxygen graphviz gtk-doc
BuildRequires: qt6-tools-devel
BuildRequires: qt6-declarative-devel qt6-multimedia-devel qt6-svg-devel qt6-webengine-devel qt6-5compat-devel
BuildRequires: chrpath desktop-file-utils
BuildRequires: libalsa-devel libdbus-c++-devel libgnutls-devel libgsm-devel
BuildRequires: libavutil-devel libavcodec-devel libavformat-devel libavdevice-devel libavfilter-devel libswscale-devel libswresample-devel
BuildRequires: nv-codec-headers
BuildRequires: libssl-devel libgpg-error-devel libgcrypt-devel
#BuildRequires: libssl-devel-static
BuildRequires: libnettle-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel libvpx-devel
BuildRequires: libspeexdsp-devel libswscale-devel libudev-devel libupnp-devel libuuid-devel jsoncpp-devel
BuildRequires: zlib-devel libopus-devel libspeex-devel libilbc-devel libx264-devel libx265-devel libva-devel libvdpau-devel
BuildRequires: libfmt-devel libarchive-devel libgit2-devel
#BuildRequires: libmsgpack-devel
BuildRequires: libyaml-cpp-devel yasm perl-Pod-Usage cppunit-devel libgmp-devel libexpat-devel
#BuildRequires: evolution-data-server-devel libclutter-gtk3-devel libnotify-devel libpixman-devel libappindicator-gtk3-devel libwebkit2gtk-devel libcanberra-gtk3-devel
BuildRequires: libgio-devel glib2-devel
BuildRequires: libXdmcp-devel libpng-devel libXxf86vm-devel libqrencode-devel


%description
Jami is a universal and distributed communication platform which respects the freedoms and privacy of users.
* Communicate freely with Jami:
  - send text messages
  - make audio calls
  - make video calls
  - share pictures and files
* Reach your peers directly in peer to peer !
* Use your Jami account on multiple devices !
* Available on Windows, macOS, iOS, GNU/Linux, Android and Android TV !
* SIP account support available !

%package -n jami-daemon
Group: System/Servers
Summary: SIP and IAX2 compatible softphone daemon
Provides: ring-daemon = %EVR
Obsoletes: ring-daemon < %EVR
%description -n jami-daemon
As the SIP/audio daemon and the user interface are separate processes.

%package -n jami-client
Summary: Ring client written in Qt
Group: Networking/Instant messaging
Requires: qt6-multimedia qt6-declarative qt6-5compat qt6-svg
Requires: qt6-webchannel qt6-webengine qt6-translations
Requires: jami-daemon
Provides: jami-client-qt = %EVR
Provides: jami-qt = %EVR
Obsoletes: ring-client-kde5 < 3.2
Provides: ring-client-qt = %EVR
Obsoletes: ring-client-qt < %EVR
Provides: ring-client-gnome = %EVR
Obsoletes: ring-client-gnome < %EVR
%description -n jami-client
Jami provides all its users a universal communication tool, autonomous, free, secure
and built on a distributed architecture thus requiring no authority or central server to function.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
Conflicts: jami-daemon < 3
Provides: ring-daemon-common = 4.1
Obsoletes: ring-daemon-common < 4.1
Provides: libringclient-common = 1.1
Obsoletes: libringclient-common < 1.1
Provides: ring-project-common = %EVR
Obsoletes: ring-project-common < %EVR
%description common
Common %name files

%package -n %libjami
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libjami
%name library.

%package -n %libjamiclient
Group: System/Libraries
Summary: Ring client library
Requires: %name-common >= %EVR
%description -n %libjamiclient
Client library for GNU Ring.

%package devel
Group: Development/Other
Summary: Development files for %name
Provides: ring-project-devel = %version-%release
Provides: ring-daemon-devel = %version-%release
Provides: libringclient-devel = %version-%release
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Group: Development/Other
Summary: Development files for %name
Requires: %name-devel
Provides: ring-daemon-devel-static = %version-%release
%description devel-static
The %name-devel package contains static libraries for
developing applications that use %name.

%prep
%setup -n %name-%version
#%patch3 -p1
%patch4 -p1
#%patch5 -p1
#%patch6 -p1
%patch7 -p1
%patch8 -p1

gzip  -c1 %SOURCE100 > daemon/contrib/tarballs/`basename %SOURCE100`.gz
gzip  -c1 %SOURCE101 > daemon/contrib/tarballs/`basename %SOURCE101`.gz
gzip  -c1 %SOURCE102 > daemon/contrib/tarballs/`basename %SOURCE102`.gz
gzip  -c1 %SOURCE103 > daemon/contrib/tarballs/`basename %SOURCE103`.gz
gzip  -c1 %SOURCE104 > daemon/contrib/tarballs/`basename %SOURCE104`.gz
gzip  -c1 %SOURCE105 > daemon/contrib/tarballs/`basename %SOURCE105`.gz
bzip2 -c1 %SOURCE106 > daemon/contrib/tarballs/`basename %SOURCE106`.bz2
gzip  -c1 %SOURCE107 > daemon/contrib/tarballs/`basename %SOURCE107`.gz
gzip  -c1 %SOURCE108 > daemon/contrib/tarballs/`basename %SOURCE108`.gz
gzip  -c1 %SOURCE109 > daemon/contrib/tarballs/`basename %SOURCE109`.gz
gzip  -c1 %SOURCE110 > daemon/contrib/tarballs/`basename %SOURCE110`.gz
gzip  -c1 %SOURCE111 > daemon/contrib/tarballs/`basename %SOURCE111`.gz
gzip  -c1 %SOURCE112 > daemon/contrib/tarballs/`basename %SOURCE112`.gz
gzip  -c1 %SOURCE113 > daemon/contrib/tarballs/`basename %SOURCE113`.gz
gzip  -c1 %SOURCE114 > daemon/contrib/tarballs/`basename %SOURCE114`.gz
gzip  -c1 %SOURCE115 > daemon/contrib/tarballs/`basename %SOURCE115`.gz
gzip  -c1 %SOURCE116 > daemon/contrib/tarballs/`basename %SOURCE116`.gz

install -m 0644 %SOURCE120 daemon/contrib/src/ffmpeg/

# build shared lib
sed -i '/add_library.*STATIC/s|STATIC|SHARED|' src/libclient/CMakeLists.txt

# don't build internal vpx
rm -rf daemon/contrib/src/vpx
rm -rf daemon/contrib/tarballs/libvpx*.tar.gz
sed -i '/DEPS_ffmpeg/s/vpx//' daemon/contrib/src/ffmpeg/rules.mak

%build
%add_optflags %optflags_shared -Wno-error=return-type
export CXXFLAGS="%optflags"
mkdir -p daemon/contrib/native
pushd daemon/contrib/native
../bootstrap \
    --no-checksums \
    --disable-downloads \
    --disable-ogg \
    --disable-flac \
    --disable-vorbis \
    --disable-vorbisenc \
    --disable-speex \
    --disable-sndfile \
    --disable-speexdsp \
    --disable-gsm \
    --disable-natpmp \
    #
make list
make
popd
pushd daemon
./autogen.sh
%configure \
    --with-libilbc \
    --with-opus \
    --enable-video \
    --enable-ipv6 \
    --without-jack \
    CFLAGS="%optflags" \
    LDFLAGS="-Wl,-z,defs" \
    #
%make_build
popd

RING_XML_INTERFACES_DIR=${PWD}/daemon/bin/dbus

# main
%cmake \
    -DENABLE_VIDEO=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DRING_XML_INTERFACES_DIR=$RING_XML_INTERFACES_DIR \
    #
pushd BUILD
%make_build
popd

pushd src/libclient
%cmake \
    -DRING_BUILD_DIR=%builddir/daemon/src \
    -DENABLE_VIDEO=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DRING_XML_INTERFACES_DIR=$RING_XML_INTERFACES_DIR \
    #
[ -e build ] || ln -s BUILD build
pushd BUILD
%make_build
popd
popd

%install
%makeinstall -C daemon
make install -C BUILD DESTDIR=%buildroot
# install libjamiclient
cp -ar src/libclient/BUILD/libjamiclient.so* %buildroot/%_libdir/
mkdir -p %buildroot/%_includedir/libjamiclient/
cp -ar src/libclient/*.h %buildroot/%_includedir/libjamiclient/
cp -ar src/libclient/{api,interfaces} %buildroot/%_includedir/libjamiclient/
# cleanup
rm -f %buildroot/%_libdir/*.a
#chrpath --delete %buildroot/%_libexecdir/jamid
chrpath --delete %buildroot/%_libdir/libjamiclient.so.%jamiclient_sover

# fix desktop-file
echo >> %buildroot/%_desktopdir/jami.desktop

# find translations
echo "%%defattr(644,root,root,755)" >jami-client-qt.lang
find %buildroot/%_datadir/jami/translations/ -type f -name \*.qm | \
while read t
do
    lang_file=`basename $t`
    lang_name=`echo "$lang_file" | sed -e 's|\.qm$||' -e 's|.*jami_client_qt_||'`
    if echo $lang_name | grep -q ^en
    then
	echo "%%_datadir/jami/translations/$lang_file" >>jami-client-qt.lang
    else
	echo "%%lang($lang_name) %%_datadir/jami/translations/$lang_file" >>jami-client-qt.lang
    fi
done

# install alternatives
mkdir -p %buildroot/%_bindir/
ln -s jami %buildroot/%_bindir/jami-gnome
ln -s jami %buildroot/%_bindir/jami-qt

%find_lang lrc --with-qt
%find_lang jami-client-gnome

%files common
%_iconsdir/hicolor/*/apps/jami*.*

%files -n jami-daemon
%doc daemon/AUTHORS daemon/COPYING
%_libexecdir/jamid
%dir %_datadir/jami/
%_datadir/dbus-1/services/cx.ring.*
%_man1dir/jamid.*

%files -n jami-client -f jami-client-qt.lang
%doc COPYING
%dir %_datadir/jami/translations/
%_bindir/jami
%_bindir/jami-*
%_datadir/jami/ringtones/
%_desktopdir/jami.desktop
%_datadir/metainfo/*jami*.xml

%files -n %libjami
%doc daemon/AUTHORS daemon/COPYING
%_libdir/libjami.so.%jami_sover
%_libdir/libjami.so.*

%files -n %libjamiclient -f lrc.lang
%_libdir/libjamiclient.so.%jamiclient_sover
%_libdir/libjamiclient.so.*

%files devel
%_libdir/lib*.so
%_includedir/jami/
%_includedir/libjamiclient/
%_datadir/dbus-1/interfaces/*ring*.xml
%_pkgconfigdir/jami.pc

%changelog
* Fri Oct 13 2023 Sergey V Turchin <zerg@altlinux.org> 20230922-alt3
- cleanup jami.tar from tarballs

* Wed Oct 11 2023 Sergey V Turchin <zerg@altlinux.org> 20230922-alt2
- fix to build on p10

* Thu Oct 05 2023 Sergey V Turchin <zerg@altlinux.org> 20230922-alt1
- new version

* Mon Oct 02 2023 Sergey V Turchin <zerg@altlinux.org> 20230619-alt4
- fix requires

* Thu Sep 21 2023 Sergey V Turchin <zerg@altlinux.org> 20230619-alt3
- fix requires

* Mon Sep 11 2023 Sergey V Turchin <zerg@altlinux.org> 20230619-alt2
- fix requires

* Tue Sep 05 2023 Sergey V Turchin <zerg@altlinux.org> 20230619-alt1
- initial build
