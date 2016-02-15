Name: libbelle-sip
Version: 1.4.2
Release: alt2
Summary: Linphone sip stack

Group: System/Libraries

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPL
Url: http://www.belle-sip.org
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: belle-sip-1.4.2-antlr34.patch
# Automatically added by buildreq on Fri Jul 31 2015
# optimized out: antlr3-C antlr3-java gnu-config java jpackage-utils libstdc++-devel pkg-config stringtemplate4 tzdata-java
BuildRequires: antlr3-C-devel antlr3-tool gcc-c++ java-devel

BuildRequires: /proc rpm-build-java

%description
Belle-sip is an object oriented c written SIP stack used by Linphone.

%package devel
Summary: Development libraries for belle-sip
Group: Development/Other
Requires: %name = %version-%release

%description devel
Libraries and headers required to develop software with belle-sip

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
pushd polarssl
sh ./autogen.sh
./configure --prefix=/usr --libdir=%_libdir
make
popd

./autogen.sh

export LDFLAGS="$LDFLAGS -L${RPM_BUILD_DIR}/%name-%version/polarssl/library/.libs"
export CFLAGS="$CFLAGS -I${RPM_BUILD_DIR}/%name-%version/polarssl/include"
export CPPFLAGS="$CPPFLAGS -I${RPM_BUILD_DIR}/%name-%version/polarssl/include"

./configure --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin \
            --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share \
            --includedir=/usr/include --libdir=%_libdir \
            --libexecdir=/usr/lib --localstatedir=/var/lib \
            --sharedstatedir=/var/lib --mandir=/usr/share/man \
            --infodir=/usr/share/info --disable-static

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool

make

%install

%makeinstall

pushd polarssl
make install DESTDIR=%buildroot
popd

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/*.so.*

%files devel
%_includedir/belle-sip
%_libdir/libbellesip.so
%_libdir/pkgconfig/belle-sip.pc

%changelog
* Mon Feb 15 2016 Alexei Takaseev <taf@altlinux.org> 1.4.2-alt2
- Add patch for antlr >= 3.4

* Tue Nov 03 2015 Alexei Takaseev <taf@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Jul 30 2015 Alexei Takaseev <taf@altlinux.org> 1.4.1-alt3
- Disable system libmbedtls, use polarssl from linphone.org

* Wed Jun 24 2015 Alexei Takaseev <taf@altlinux.org> 1.4.1-alt2
- Rebuild with new libmbedtls-1.3.11

* Wed May 06 2015 Alexei Takaseev <taf@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Mar 12 2015 Alexei Takaseev <taf@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Sep 19 2014 Alexei Takaseev <taf@altlinux.org> 1.3.3-alt1
- 1.3.3

* Fri Aug 08 2014 Alexei Takaseev <taf@altlinux.org> 1.3.0-alt4
- Rebuild with polarssl-1.3.8

* Tue Apr 22 2014 Alexei Takaseev <taf@altlinux.org> 1.3.0-alt3
- Rebuild with polarssl-1.3.6

* Sat Mar 01 2014 Alexei Takaseev <taf@altlinux.org> 1.3.0-alt2
- Add TLS transport

* Tue Feb 25 2014 Alexei Takaseev <taf@altlinux.ru> 1.3.0-alt1
- Initial build for ALT Sisyphus

* Mon Aug 19 2013 jehan.monnier <jehan.monnier@linphone.org>
- Initial RPM release.
