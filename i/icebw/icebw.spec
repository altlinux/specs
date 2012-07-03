# For build on x86_64 fix (via macros?)
#gpointer knop=gtk_object_get_user_data(GTK_OBJECT(widget));
#switch ((gint)knop)

%define build_lang uk_UA.KOI8-U

%define oname iceBw
%define oversion 7_0
Name: icebw
Version: 7.0
Release: alt1

Summary: Free financial accounting system with GTK interface

Group: Office
License: GPL
Url: http://www.iceb.com.ua

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %url/download/%oname.tar

Patch1: icebw-6_1_alt_gcc.patch
Patch2: icebw-7_0-fix-overflow.patch

BuildRequires: gcc-c++ libMySQL-devel libgtk+2-devel

%description
Free financial accounting system.

%prep
%setup -q -c
%patch2 -p2
subst "s|/usr/share/locale/ru/|%buildroot%_datadir/locale/uk/|g" locale/Makefile

%build
export LANG=%build_lang
%make_build

%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/locale/uk/LC_MESSAGES/
make install install \
    BINDIR=%buildroot%_bindir

%files
%_bindir/*
%_datadir/locale/uk/LC_MESSAGES/%oname.mo

%changelog
* Wed Aug 31 2011 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1
- New version 7.0

* Tue Apr 19 2011 Andrey Cherepanov <cas@altlinux.org> 6.11-alt1
- New version 6.11

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 6.1-alt1
- 6_1

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- initial build for ALT Linux Sisyphus

