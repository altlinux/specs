%define apache_version  1.3.6
%set_verify_elf_method unresolved=relaxed

Summary:                DAV module for Apache 1.3.x
Summary(ru_RU.KOI8-R):  Модуль DAV под Apache 1.3.x
Name: mod_dav
Version: 1.0.3
Release: alt4
Group: System/Servers
License: Apache
URL: http://www.webdav.org/mod_dav/
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Requires: apache >= %apache_version
BuildRequires: apache-devel >= %apache_version libgdbm-devel libexpat-devel

%define apache_modconf %_sysconfdir/httpd/conf/addon-modules
%define apache_moddoc  %_var/www/html/addon-modules

Source:  http://www.webdav.org/mod_dav/%name-%version-%apache_version.tar.bz2
Source1: mod_dav.conf

Patch0:  mod_dav-1.0.2-nosdbm.patch
Patch1:  mod_dav-1.0.3-configure.patch

%description
mod_dav is an Apache module to provide DAV capabilities (RFC 2518)
for your Apache 1.3.x web server.

From http://www.webdav.org:

  "WebDAV stands for 'Web-based Distributed Authoring and Versioning'.
   It is a set of extensions to the HTTP protocol which allows users to
   collaboratively edit and manage files on remote web servers."

DAV functionality includes creating, moving, copying, and deleting
files and directories on a remote web server. Utilizing DAV requires
both a DAV-aware client and server. mod_dav provides complete class 1
and 2 DAV services to DAV clients via the Apache webserver (1.3.4 or
later). The number of DAV-aware clients is growing and includes the 
'Web Folders' used in Microsoft Internet Explorer 5.0 and Office 2000.

%prep
%setup -q -n %name-%version-%apache_version
%patch0 -p0
%patch1 -p1

%build
autoconf
CFLAGS='-DDAV_USE_GDBM' \
%configure --with-apxs=%_sbindir/apxs --with-expat=%_prefix
%make_build

%install
mkdir -p %buildroot%_libdir/apache/
mkdir -p %buildroot%apache_modconf/
install -m755 libdav.so %buildroot%_libdir/apache/
install -m644 %SOURCE1 %buildroot%apache_modconf/
install -d -m750 %buildroot%_var/lock/dav/

%clean

%post
%_sbindir/apxs -e -a -n dav libdav.so
%_sbindir/apachectl update
ln -snf %_docdir/%name-%version %apache_moddoc/%name

%preun
if [ $1 = 0 ]; then
    [ -x %_sbindir/apxs ] && %_sbindir/apxs -e -A -n dav libdav.so
    [ -x %_sbindir/apachectl ] && %_sbindir/apachectl update
    %__rm -f %apache_moddoc/%name
fi

%files
%doc README CHANGES LICENSE.html
%_libdir/apache/libdav.so
%config(noreplace) %apache_modconf/mod_dav.conf
%attr(-,apache,apache) %_var/lock/dav/

%changelog
* Thu Mar 30 2006 Sergei Epiphanov <serpiph@altlinux.ru> 1.0.3-alt4
- Fixing unresolved symbols from gdbm
- Setting relaxed for unresolved

* Fri Sep 30 2005 Sergei Epiphanov <serpiph@altlinux.ru> 1.0.3-alt3
- Spec corrections

* Mon Sep 05 2005 Sergei Epiphanov <serpiph@altlinux.ru> 1.0.3-alt2
- Some fixes in mod_dav.conf

* Thu Feb 28 2002 Alexander Bokovoy <ab@altlinux.ru> 1.0.3-alt1
- 1.0.3
- Build against 1.3.23/EAPI 2.8.7
- Preuninstal script fixes

* Sun Feb 11 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.0.2_1.3.6-ipl1mdk
- initial package release
