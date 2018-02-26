%define		src gloox

Name:		lib%src
Version:	1.0
Release:	alt1.2
Summary:	A rock-solid, full-featured Jabber/XMPP client library
Group:		System/Libraries
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>

URL:		http://camaya.net/gloox
Source0:	http://camaya.net/download/%src-%version.tar.bz2

# Automatically added by buildreq on Wed Jun 02 2010 (-bi)
BuildRequires: gcc-c++ libidn-devel libssl-devel zlib-devel

%description
gloox is a rock-solid, full-featured Jabber/XMPP client library, written in
C++. It makes writing spec-compliant clients easy and allows for hassle-free
integration of Jabber/XMPP functionality into existing applications.

%package	devel
Summary:	Development files for %name
Group:		Development/C++
Requires:	%name = %version-%release

%description	devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %src-%version

%build
export PTHREAD_LIBS="-lpthread"
%configure --disable-static

%make_build
# recode to UTF
mv -f AUTHORS AUTHORS.old
iconv -f iso8859-1 -t UTF-8 AUTHORS.old > AUTHORS

%install
make install DESTDIR=%buildroot
find %buildroot -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog README TODO UPGRADING
%_libdir/*.so.*

%files devel
%dir %_includedir/%src
%_bindir/%src-config
%_pkgconfigdir/%src.pc
%_includedir/%src/*
%_libdir/*.so

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 1.0-alt1.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt for soname set-versions

* Wed Jun 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- initial build for ALT Linux from FC3 package
