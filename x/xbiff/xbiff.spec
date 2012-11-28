# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(xaw7) pkgconfig(xbitmaps) pkgconfig(xext)
# END SourceDeps(oneline)
Summary: X.Org X11 new e-mail graphical notification application
Name: xbiff
Version: 1.0.2
Release: alt1_6
License: MIT
Group: System/X11
URL: http://www.x.org

Source:  ftp://ftp.x.org/pub/individual/app/xbiff-1.0.2.tar.bz2
Patch6: xbiff-1.0.2-xmu-configure.patch
Source44: import.info

BuildRequires: xorg-util-macros

%description
xbiff provides graphical notification of new e-mail.                            
It only handles mail stored in a filesystem accessible file,                    
not via IMAP, POP or other remote access protocols.                             

%prep
%setup -q
%patch6 -p2 -b .xmu-configure

%build
# Build all apps
sed -i '/XAW_/ s/)/, xaw7)/; /XAW_/ s/XAW_CHECK_XPRINT_SUPPORT/PKG_CHECK_MODULES/' configure.ac
autoreconf -v --install
%configure --disable-xprint
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/xbiff
%{_mandir}/man1/xbiff.1*

%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_6
- build for Sisyphus
