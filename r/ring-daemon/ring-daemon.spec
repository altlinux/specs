%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif
%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif

%define rname ring-daemon
%define _libexecdir %prefix/libexec
%define sover 0
%define libring libring%sover

Name: ring-daemon
Version: 4.0.0
Release: alt1%ubt

Group: System/Servers
Summary: SIP and IAX2 compatible softphone - Core
Url: http://ring.cx/
License: GPLv3

PreReq(post,preun): alternatives >= 0.2
#Conflicts: sflphone sflphone-common
#Requires: %name-common >= %EVR

Source: %name-%version.tar
Patch1: alt-fix-compile.patch
Patch2: alt-fix-linking.patch

# Automatically added by buildreq on Tue Mar 15 2016 (-bi)
# optimized out: boost-devel-headers cmake-modules elfutils fontconfig gnu-config kde4libs libavcodec-devel libavutil-devel libcdio-paranoia libdbus-c++ libdbus-devel libdbusmenu-qt2 libdc1394-22 libgnome-keyring libgpg-error libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt4-core libqt4-dbus libqt4-gui libqt4-network libqt4-svg libqt4-xml libraw1394-11 libsasl2-3 libstdc++-devel libyaml-cpp0 perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators pkg-config python-base python3 python3-base rpm-build-python3 xz
#BuildRequires: cmake curl doxygen gcc-c++ git-core glibc-devel-static graphviz libalsa-devel libavdevice-devel libavformat-devel libdbus-c++-devel libgnutls-devel libgsm-devel libnettle-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel libspeexdsp-devel libsubversion-auth-gnome-keyring libsubversion-auth-kwallet libswscale-devel libudev-devel libupnp-devel libuuid-devel libyaml-cpp-devel perl-Pod-Usage python3.3-site-packages ruby ruby-stdlibs subversion
BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake gcc-c++ glibc-devel autoconf-archive
BuildRequires: doxygen graphviz gtk-doc
BuildRequires: chrpath
BuildRequires: libalsa-devel libavdevice-devel libavformat-devel libdbus-c++-devel libgnutls-devel libgsm-devel
BuildRequires: libnettle-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel
BuildRequires: libspeexdsp-devel libswscale-devel libudev-devel libupnp-devel libuuid-devel jsoncpp-devel
BuildRequires: zlib-devel libopus-devel libspeex-devel ilbc-devel libmsgpack-devel libx264-devel libva-devel
BuildRequires: libyaml-cpp-devel yasm perl-Pod-Usage cppunit-devel libgmp-devel

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

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
Conflicts: ring-daemon < 3
%description common
Common %name files

%package -n %libring
Group: System/Libraries
Summary: %summary
Requires: %name-common >= %EVR
%description -n %libring
%summary

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
%patch2 -p1

pushd .gear
while read project_dir tarball_dir tarball_name
do
    tb_fmt=`echo $tarball_name | sed -e 's|^.*\.tar\.||'`
    tb_opt=czf
    case "$tb_fmt" in
	xz)
	    tb_opt=cJf ;;
	bz2)
	    tb_opt=cjf ;;
	*)
	    tb_opt=czf ;;
    esac
    mv $project_dir $tarball_dir
    tar $tb_opt ../contrib/tarballs/$tarball_name $tarball_dir
    rm -rf $tarball_dir
done <<__EOF__
argon2    phc-winner-argon2-1eea0104e7cb2a38c617cf90ffa46ce5db6aceda argon2-1eea0104e7cb2a38c617cf90ffa46ce5db6aceda.tar.gz
gmp       gmp-6.1.0                                                  gmp-6.1.0.tar.bz2
gnutls    gnutls-3.5.10                                              gnutls-3.5.10.tar.xz
pjproject pjproject-2.6                                              pjproject-2.6.tar.bz2
opendht   opendht-6f3eafc5eea1b456a625bdf473419464eb0b202a           opendht-6f3eafc5eea1b456a625bdf473419464eb0b202a.tar.gz
msgpack   msgpack-c-cpp-2.1.3                                        msgpack-c-cpp-2.1.3.tar.gz
asio      asio-28d9b8d6df708024af5227c551673fdb2519f5bf              asio-28d9b8d6df708024af5227c551673fdb2519f5bf.tar.gz
boost     boost_1_61_0                                               boost_1_61_0.tar.bz2
cryptopp  cryptopp-54557b18275053bbfc34594f7e65808dd92dd1a6          cryptopp-54557b18275053bbfc34594f7e65808dd92dd1a6.tar.gz
ffmpeg    ffmpeg-n3.3.1                                              ffmpeg-n3.3.1.tar.xz
natpmp    libnatpmp-20150609                                         libnatpmp-20150609.tar.gz
vpx       libvpx-v1.5.0                                              libvpx-v1.5.0.tar.gz
restbed   restbed-34187502642144ab9f749ab40f5cdbd8cb17a54a           restbed-34187502642144ab9f749ab40f5cdbd8cb17a54a.tar.gz
yaml-cpp  yaml-cpp-24fa1b33805c9a91df0f32c46c28e314dd7ad96f          yaml-cpp-24fa1b33805c9a91df0f32c46c28e314dd7ad96f.tar.gz
__EOF__
popd


%build
%add_optflags %optflags_shared
mkdir -p contrib/native
cd contrib/native
../bootstrap --no-checksums --disable-downloads --disable-ogg --disable-flac --disable-vorbis --disable-vorbisenc --disable-speex --disable-sndfile --disable-speexdsp --disable-gsm
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

chrpath --delete %buildroot/%_libdir/ring/dring

# install alternative
mkdir %buildroot/%_bindir/
echo >%buildroot/%_bindir/ring-client-dummy <<__EOF__
#!/bin/sh
echo "ring-client not found"
exit 1
__EOF__
chmod 0755 %buildroot/%_bindir/ring-client-dummy
ln -s /bin/true %buildroot/%_bindir/ring
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/ring       %_bindir/ring-client-dummy      1
__EOF__

%files
%doc AUTHORS COPYING README
%config /%_sysconfdir/alternatives/packages.d/%name
%ghost %_bindir/ring
%_bindir/ring-client-dummy
%_libdir/ring/
%_datadir/dbus-1/services/cx.ring.*

%files common
%_datadir/ring/

%files -n %libring
%_libdir/libring.so.%sover
%_libdir/libring.so.%sover.*

%files devel
%_libdir/lib*.so
%_includedir/dring/
%_datadir/dbus-1/interfaces/cx.ring.Ring.*.xml
%_man1dir/dring.*

%files devel-static
#%_libdir/libring.a

%changelog
* Tue Jul 25 2017 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt1%ubt
- new version
- add dummy client alternative

* Wed Feb 22 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.1%ubt
- new beta

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.3
- fix build requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.2
- update from master branch

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.1
- initial build
