%def_enable  openssl
%def_without devel

Summary: CONE mail reader
Name: cone
Version: 1.7
Release: alt0.1
Url: http://www.courier-mta.org/cone
Source0: %name-%version.tar.bz2
License: GPLv3
Group: Networking/Mail

Patch1: cone-alt-sendmail.patch
Patch2: cone-alt-app-defaults.patch
Patch3: cone-1.6-alt-m4.patch

Packager: L.A. Kostis <lakostis@altlinux.org>

BuildRequires: libaspell-devel libxml2-devel
BuildRequires: zlib-devel libgamin-devel perl libncursesw-devel
BuildRequires: libstdc++-devel gcc-c++
BuildRequires: openldap-devel libidn-devel courier-unicode-devel
BuildRequires: gnupg2 libpcre2-devel

%if_enabled openssl
BuildRequires: openssl
BuildRequires: openssl-devel
%else
BuildRequires: gnutls-devel libgcrypt-devel
%endif

Requires(post): perl

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
%patch3 -p2
for d in curses libmail cone; do
pushd "$d"
ln -s ../{NEWS,README,AUTHORS,ChangeLog} . ||:
popd
done

%autoreconf
%configure -C \
            --with-notice=unicode \
	    --libexecdir=%_prefix/libexec \
	    --with-certdb=%_datadir/ca-certificates/ca-bundle.crt \
	    %subst_with devel
%build
%make_build
%install
make install DESTDIR=%buildroot
install sysconftool %buildroot%_datadir/cone/cone.sysconftool
touch %buildroot%_sysconfdir/cone

# Remove dupe copies of doc/html from the install tree.
ls cone/html | ( cd %buildroot%_datadir/cone && xargs -n10 rm -f )

%post
perl %_datadir/cone/cone.sysconftool %_sysconfdir/cone.dist >/dev/null

%triggerun -- cone < 0.96
echo 'WARNING! WARNING!'
echo 'Outdated cone version detected, manual intervention needed!'
echo 'Please read INSTALL documentation about upgrade from cone 0.96'
echo 'and earlier'

%files
%attr(644,root,root) %_sysconfdir/cone.dist
%ghost %verify(user group mode) %attr(644,root,root) %_sysconfdir/cone
%_bindir/*
%_prefix/libexec/cone
%_datadir/cone
%_man1dir/*
%doc ChangeLog README NEWS AUTHORS COPYING COPYING.GPL INSTALL

%if_with devel
%files devel-static
%_libdir/*.a
%_mandir/man[35]/*
%_includedir/libmail
%doc cone/html
%endif

%changelog
* Mon Nov 28 2022 L.A. Kostis <lakostis@altlinux.ru> 1.7-alt0.1
- 1.7.

* Tue Sep 13 2022 L.A. Kostis <lakostis@altlinux.ru> 1.6-alt0.1
- 1.6.
- app-defaults: optimize.
- add pcre2 deps (for maildir filters).

* Tue Sep 07 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2-alt0.1
- 1.2.

* Wed Mar 10 2021 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.1
- 1.1.
- Added cone < 0.96 upgrade trigger.

* Sun Jan 08 2017 L.A. Kostis <lakostis@altlinux.ru> 0.94-alt0.2
- use correct libexec dir.

* Fri Jan 06 2017 L.A. Kostis <lakostis@altlinux.ru> 0.94-alt0.1
- 0.94.

* Tue Jul 28 2015 L.A. Kostis <lakostis@altlinux.ru> 0.92-alt0.1
- 0.92.

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
