%def_enable  openssl
%def_without devel

Summary: CONE mail reader
Name: cone
Version: 0.89
Release: alt0.1
Url: http://www.courier-mta.org/cone
Source0: %name-%version.tar.bz2
License: GPL
Group: Networking/Mail

Patch1: cone-alt-sendmail.patch
Patch2: cone-alt-app-defaults.patch

Packager: L.A. Kostis <lakostis@altlinux.org>

BuildRequires: libaspell-devel libxml2-devel
BuildRequires: zlib-devel libgamin-devel perl libncursesw-devel
BuildRequires: libstdc++-devel gcc-c++
BuildRequires: openldap-devel libidn-devel

%if_enabled openssl
BuildRequires: openssl
BuildRequires: openssl-devel
%else
BuildRequires: gnutls-devel libgcrypt-devel
%endif

Requires(post): %__perl

%description
CONE is a simple, text-based E-mail reader and writer.

%if_with devel
%package devel-static
Group: Development/C++
Summary: LibMAIL mail client development library
Requires: %name = 0:%version-%release

%description devel-static
The %name-devel package the header files and library files for developing
application using LibMAIL - a high level, C++ OO library for mail clients.
%endif

%prep
%setup -q
%patch1 -p2
%patch2 -p2
pushd cone
autoconf
popd
pushd libmail
autoconf
popd
%configure -C \
	    --with-certdb=%_datadir/ca-certificates/ca-bundle.crt \
	    %subst_with devel
%build
%make_build
%install
%__make install DESTDIR=%buildroot
%__install sysconftool %buildroot%_datadir/cone/cone.sysconftool
touch %buildroot%_sysconfdir/cone

# Remove dupe copies of doc/html from the install tree.
ls cone/html | ( cd %buildroot%_datadir/cone && xargs -n10 rm -f )

%post
%__perl %_datadir/cone/cone.sysconftool %_sysconfdir/cone.dist >/dev/null

%files
%attr(644,root,root) %_sysconfdir/cone.dist
%ghost %verify(user group mode) %attr(644,root,root) %_sysconfdir/cone
%_bindir/*
%_libexecdir/cone
%_datadir/cone
%_man1dir/*
%doc ABOUT-NLS ChangeLog README NEWS AUTHORS COPYING COPYING.GPL

%if_with devel
%files devel-static
%_libdir/*.a
%_mandir/man[35]/*
%_includedir/libmail
%doc cone/html
%endif

%changelog
* Wed Jan 18 2012 L.A. Kostis <lakostis@altlinux.ru> 0.89-alt0.1
- 0.89.
- Change default app settings.

* Mon Aug 31 2009 L.A. Kostis <lakostis@altlinux.ru> 0.79-alt0.1
- 0.79.

* Sun Jun 28 2009 L.A. Kostis <lakostis@altlinux.ru> 0.78.20090507-alt0.2
- Initial build for ALTLinux.
- Disable -devel package (due it's static nature).

* Wed Apr 14 2004 Mr. Sam <sam@email-scan.com>
- Replace BuildPreReq: with BuildRequires, +other fixes.
- Remove duplicate html docs, move them to -devel subpackage.

* Mon Sep  1 2003 Mr. Sam <sam@email-scan.com>
- Fix for Red Hat 9+

* Sat Jul 26 2003 Mr. Sam 0.52
- Use wide-char compatible ncurses in current RH Beta.

* Wed Mar  5 2003 Mr. Sam <mrsam@courier-mta.com>
- Initial build.
