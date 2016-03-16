%define rname ring-daemon
%define _libexecdir %prefix/libexec

Name: ring-daemon
Version: 2.3.0
Release: alt0.1

Group: System/Servers
Summary: SIP and IAX2 compatible softphone - Core
Url: http://ring.cx/
License: GPLv3

#Conflicts: sflphone sflphone-common

Source: %name-%version.tar
Source1: pjproject-2.4.5.tar.bz2
Source2: opendht-281b62dfd529a226e94d0da19e01acf07871a797.tar.gz
Source3: msgpack-c-cpp-1.2.0.tar.gz
Source4: iax-git.tar.gz
Patch1: alt-fix-compile.patch

# Automatically added by buildreq on Tue Mar 15 2016 (-bi)
# optimized out: boost-devel-headers cmake-modules elfutils fontconfig gnu-config kde4libs libavcodec-devel libavutil-devel libcdio-paranoia libdbus-c++ libdbus-devel libdbusmenu-qt2 libdc1394-22 libgnome-keyring libgpg-error libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt4-core libqt4-dbus libqt4-gui libqt4-network libqt4-svg libqt4-xml libraw1394-11 libsasl2-3 libstdc++-devel libyaml-cpp0 perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators pkg-config python-base python3 python3-base rpm-build-python3 xz
#BuildRequires: cmake curl doxygen gcc-c++ git-core glibc-devel-static graphviz libalsa-devel libavdevice-devel libavformat-devel libdbus-c++-devel libgnutls-devel libgsm-devel libnettle-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel libspeexdsp-devel libsubversion-auth-gnome-keyring libsubversion-auth-kwallet libswscale-devel libudev-devel libupnp-devel libuuid-devel libyaml-cpp-devel perl-Pod-Usage python3.3-site-packages ruby ruby-stdlibs subversion
BuildRequires: cmake gcc-c++ glibc-devel autoconf-archive
BuildRequires: doxygen graphviz
BuildRequires: libalsa-devel libavdevice-devel libavformat-devel libdbus-c++-devel libgnutls-devel libgsm-devel
BuildRequires: libnettle-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel
BuildRequires: libspeexdsp-devel libswscale-devel libudev-devel libupnp-devel libuuid-devel
BuildRequires: zlib-devel libopus-devel libspeex-devel ilbc-devel
BuildRequires: libyaml-cpp-devel perl-Pod-Usage
#curl git-core subversion

%description
Ring is a Voice-over-IP software phone. We want it to be:
- user friendly (fast, sleek, easy to learn interface)
- professional grade (transfers, holds, optimal audio quality)
- fully compatible with Asterisk (SIP and IAX protocols)
- de-centralized call (P2P-DHT)
- customizable

As the SIP/audio daemon and the user interface are separate processes,
it is easy to provide different user interfaces. Ring comes with
various graphical user interfaces and even scripts to control the daemon from
the shell.

%package devel
Group: Development/Other
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Group: Development/Other
Summary: Development files for %name
Requires: %name-devel
%description devel-static
The %name-devel package contains static libraries for
developing applications that use %name.

%prep
%setup -qn %name-%version
%patch1 -p1
install -m 0644 %SOURCE1 contrib/tarballs/
sed -i '/^pjproject:/s|\.sum-pjproject||' contrib/src/pjproject/rules.mak
install -m 0644 %SOURCE2 contrib/tarballs/
sed -i '/^opendht:/s|\.sum-opendht||' contrib/src/opendht/rules.mak
install -m 0644 %SOURCE3 contrib/tarballs/
sed -i '/^msgpack:/s|\.sum-msgpack||' contrib/src/msgpack/rules.mak
install -m 0644 %SOURCE4 contrib/tarballs/
sed -i '/^iax:/s|\.sum-iax||' contrib/src/iax/rules.mak

%build
%add_optflags %optflags_shared
mkdir -p contrib/native
cd contrib/native
../bootstrap --disable-ogg --disable-flac --disable-vorbis --disable-vorbisenc --disable-speex --disable-sndfile --disable-speexdsp --disable-gsm
make list
make
cd ../..
echo "Contribs built"
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

%install
%makeinstall

%files
%doc AUTHORS COPYING README
%_libexecdir/dring
%_datadir/ring/
%_datadir/dbus-1/services/cx.ring.*

%files devel
%_includedir/dring/

%files devel-static
%_libdir/libring.a

%changelog
* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.1
- initial build
