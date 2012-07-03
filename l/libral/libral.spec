%define oversion 0.9.6
Name: libral
Version: 0.96
Release: alt0.1.qa1

Summary: An address book engine

License: LGPL
Group: Development/C
#Url: http://libral.sourceforge.net/
Url: http://developer.berlios.de/projects/libral

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://dl.sf.net/%name/%name-%version.tar.bz2
Source: http://download.berlios.de/libral/%name-%oversion.tar.bz2
Patch: %name-0.95.patch

# Automatically added by buildreq on Sun Mar 26 2006
BuildRequires: gcc-c++ glib2-devel glibc-devel libxml2-devel pkg-config zlib-devel
BuildRequires: gtk-doc

%description
Libral is an address book engine. It allows you to create your address
books and to add personal and company cards to them. Data managed in
a personal card include personal data (name, surname, address, etc.),
Web links, email addresses, irc uris, telephone numbers, job information
(company where the contact works, manager, collaborator, etc.), and
notes. In a company card you can manage Web links, email addresses,
telephone numbers, and notes. XML is used to store data. Libral can import
addressbooks from GnomeCard, Kaddressbook, VCard, Evolution, and CSV.

%package devel
Summary: Header files for libral
Summary(ru_RU.KOI8-R): Заголовочные файлы для libral
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contain header files for libral.

%description -l ru_RU.KOI8-R
Пакет содержит заголовочные файлы для libral.

%prep
%setup -q -n %name-%oversion
%patch

%build
%__autoreconf
%configure --disable-static
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS README
%_libdir/*.so.*
%_libdir/%name/

%files devel
%_includedir/%name-*
%_pkgconfigdir/*.pc
%_libdir/*.so
%_datadir/gtk-doc/html/libRAL/

%changelog
* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.96-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libral
  * postun_ldconfig for libral
  * postclean-05-filetriggers for spec file

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt0.1
- new version (0.96)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt0.1
- new version 0.95 (mainstream wrote it as 0.9.5)

* Sun Mar 26 2006 Vitaly Lipatov <lav@altlinux.ru> 0.70-alt0.1
- new version (0.70), fixes for --as-needed
- fix gtk-doc build

* Mon Sep 19 2005 Vitaly Lipatov <lav@altlinux.ru> 0.50-alt1
- new version

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.42.0-alt0.1
- first build for ALT Linux Sisyphus
