Name: libbelle-sip
Version: 1.3.0
Release: alt2
Summary: Linphone sip stack

Group: System/Libraries

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPL
Url: http://www.belle-sip.org
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
# Automatically added by buildreq on Tue Feb 25 2014
# optimized out: antlr3-C antlr3-java gnu-config java jpackage-utils libcloog-isl4 libstdc++-devel pkg-config stringtemplate4
BuildRequires: antlr3-C-devel antlr3-tool gcc-c++ java-devel
BuildRequires: /proc rpm-build-java libpolarssl-devel

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
./autogen.sh

%build
#%%configure --disable-tests --disable-shared --enable-shared
#%%configure
./configure --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin \
            --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share \
            --includedir=/usr/include --libdir=%_libdir \
            --libexecdir=/usr/lib --localstatedir=/var/lib \
            --sharedstatedir=/var/lib --mandir=/usr/share/man \
            --infodir=/usr/share/info --disable-static
make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/*.so.*

%files devel
%_includedir/belle-sip
%_libdir/libbellesip.so
%_libdir/pkgconfig/belle-sip.pc

%changelog
* Sat Mar 01 2014 Alexei Takaseev <taf@altlinux.org> 1.3.0-alt2
- Add TLS transport

* Tue Feb 25 2014 Alexei Takaseev <taf@altlinux.ru> 1.3.0-alt1
- Initial build for ALT Sisyphus

* Mon Aug 19 2013 jehan.monnier <jehan.monnier@linphone.org>
- Initial RPM release.
