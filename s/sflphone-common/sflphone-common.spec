%define rname sflphone

Name: sflphone-common
Version: 1.4.1
Release: alt1

Group: System/Servers
Summary: SIP and IAX2 compatible softphone - Core
Url: http://www.sflphone.org/
License: GPLv3

Conflicts: sflphone

Source: %name-%version.tar
Patch1: sflphone-1.3.0-alt-find-gsm.patch
Patch10: pjproject-2.0.1-alt-libav.patch
Patch11: sflphone-1.3.0-alt-libav10.patch
Patch12:sflphone-1.4.0-alt-fix-compile.patch

# Automatically added by buildreq on Tue Feb 19 2013 (-bi)
# optimized out: elfutils gcc-c++ gnu-config libavcodec-devel libavutil-devel libccrtp-devel libcom_err-devel libcommoncpp2-devel libdbus-c++ libdbus-devel libgpg-error libkrb5-devel libopencore-amrnb0 libstdc++-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators pkg-config python-base ruby ruby-stdlibs
#BuildRequires: glibc-devel-static libSDL-devel libalsa-devel libavformat-devel libdbus-c++-devel libexpat-devel libgsm-devel libopencore-amrnb-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libspeex-devel libssl-devel libswscale-devel libuuid-devel libv4l-devel libyaml-devel libzrtpcpp-devel perl-Pod-Parser python-module-distribute rpm-build-ruby
BuildRequires: gcc-c++ glibc-devel libSDL-devel libalsa-devel libavformat-devel libdbus-c++-devel libexpat-devel
BuildRequires: libgsm-devel libopencore-amrnb-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel
BuildRequires: libspeex-devel libssl-devel libswscale-devel libuuid-devel libv4l-devel libyaml-devel
BuildRequires: zrtpcpp-devel perl-Pod-Parser python-devel ilbc-devel libopus-devel
BuildRequires: libudev-devel libavdevice-devel libswscale-devel
BuildRequires: libgnutls-devel

%description
SFLphone is meant to be a robust enterprise-class desktop phone.
 SFLphone is released under the GNU General Public License.
 SFLphone is being developed by the global community, and maintained by
 Savoir-faire Linux, a Montreal, Quebec, Canada-based Linux consulting company.

Authors:
--------
    Julien Bonjean <julien.bonjean@savoirfairelinux.com>

%prep
%setup -qn %name-%version
%patch1 -p1
pushd libs/pjproject-*/
%patch10 -p1
%patch11 -p1
%patch12 -p1
popd
sed -i 's|^export[[:space:]][[:space:]]*CC[[:space:]][[:space:]]*=.*$|export CC = gcc -c|' libs/pjproject-*/build/cc-auto.mak.in
sed -i 's|^export[[:space:]][[:space:]]*CXX[[:space:]][[:space:]]*=.*$|export CXX = g++ -c|' libs/pjproject-*/build/cc-auto.mak.in
#sed -i 's|^export[[:space:]][[:space:]]*AR[[:space:]][[:space:]]*=.*$|export AR = ar rv|' libs/pjproject-*/build/cc-auto.mak.in
sed -i 's|^export[[:space:]][[:space:]]*AR[[:space:]][[:space:]]*=.*$|export AR = ar|' libs/pjproject-*/build/cc-auto.mak.in
#sed -i 's|^export[[:space:]][[:space:]]*LD[[:space:]][[:space:]]*=.*$|export LD = gcc|' libs/pjproject-*/build/cc-auto.mak.in
sed -i 's|^export[[:space:]][[:space:]]*RANLIB[[:space:]][[:space:]]*=.*$|export RANLIB = ranlib|' libs/pjproject-*/build/cc-auto.mak.in
sed -i 's|\$(CROSS_COMPILE)||' libs/pjproject-*/build/cc-gcc.mak
sed -i 's|\$CROSS_COMPILE||' libs/pjproject-*/aconfigure
%autoreconf

%build
pushd libs/pjproject-*/
CFLAGS="%optflags_shared" CC=gcc CXX=g++ %configure
%make dep
%make
popd
%configure \
    --with-libilbc \
    --with-opus \
    --enable-video \
    --enable-ipv6 \
    #
%make_build

%install
%makeinstall

[ -e %buildroot/usr/lib/sflphoned ] && \
    mv %buildroot/usr/lib/sflphoned %buildroot/%_libdir/sflphone/

%files
%doc AUTHORS COPYING README
%prefix/share/dbus-1/services/org.sflphone.*
%_datadir/sflphone/
%_libdir/sflphone/
%_mandir/man1/sflphoned.1*

%changelog
* Thu Oct 23 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.1-alt1
- new version

* Thu Oct 23 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1.M70P.1
- built for M70P

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt2
- build with new ilbc

* Wed Sep 24 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- new version

* Mon May 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt2
- built with new libav

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt0.M70P.1
- built for M70P

* Fri Jan 31 2014 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt2
- rebuilt with new libav

* Fri Aug 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1
- new version

* Thu Feb 21 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt3
- enable video support

* Tue Feb 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt2
- fix packaging sflphoned

* Tue Feb 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1
- initial build
