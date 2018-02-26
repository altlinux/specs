%set_automake_version 1.9
%set_autoconf_version 2.5

%def_disable nopic

%define name 			libxdtv-i18n-ru
%define m_name 			libxdtv_i18n_ru

%define branch_point alt3
%define revision 1

%define version 		2.4.0
%define base			xdtv

%define summary			%name is a ru NLS library for XdTV
%define LANG			ru

Name: %name
Summary: %summary
Version: %version
Release: %branch_point.%revision.qa1
License: GPL
Url: http://xawdecode.sourceforge.net/
Packager: Hihin Ruslan <ruslandh@altlinux.ru>
Source0: %name-%version.tar.gz
Source1: xdtv-2.4.po.tar.bz2
Patch1: libxdtv-i18n-ru-2.4.0-as-need.patch

Group: Video

BuildPreReq: libalevt-devel  libX11-devel libXpm-devel gcc4.1-c++ iconv sed

# Automatically added by buildreq on Sun Jun 03 2007
BuildRequires: glibc-devel-static libXaw-devel 

Requires: xdtv >= 2.4.0 man-pages-ru

%description
%summary

%prep
%setup -q -a1
%patch1 -p1
%__subst "s|@NPACKAGE@|%name|" src/Makefile.am
%__subst "s|@LPACKAGE@|%m_name|" src/Makefile.am

%build
%__autoreconf
export FLAGS="%optflags -DNDEBUG -DNO_DEBUG -D_GNU_SOURCE "
%configure \
%{subst_enable nopic}


%make
iconv -fUTF8 -tWINDOWS-1251 xdtv_wizard-%LANG-UTF8.conf > xdtv_wizard-%LANG-cp1251.conf

%install
%makeinstall ROOT=%buildroot \
	     SUID_ROOT="" \
	     libdir=%buildroot/%_libdir

install -d -m 755 %buildroot/%_libdir/%base
mv %buildroot%_libdir/*so* %buildroot%_libdir/%base

# %LANG
install -d -m 755 %buildroot%_mandir/%LANG/man1
install -m 644 man/xdtv.1 %buildroot%_mandir/%LANG/man1
install -m 644 man/xdtv_cmd.1 %buildroot%_mandir/%LANG/man1
install -m 644 man/xdtv_alevt.1 %buildroot%_mandir/%LANG/man1
install -m 644 man/xdtv_alevt-cap.1 %buildroot%_mandir/%LANG/man1
install -m 644 xdtv_wizard-ru-cp1251.conf %buildroot%_sysconfdir/xdtv

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/%base/*.so
%_mandir/%LANG/*
%_datadir/locale/%LANG/LC_MESSAGES/xdtv.mo
%_sysconfdir/xdtv/xdtv_wizard-*.conf

%changelog
* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.4.0-alt3.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libxdtv-i18n-ru
  * postun_ldconfig for libxdtv-i18n-ru
  * distribution-tag for libxdtv-i18n-ru
  * postclean-05-filetriggers for spec file

* Sat Jun 16 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt3.1
- version for branch-4.0

* Sun Jun 03 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.5
- correct xdtv.po

* Sun Jun 03 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.2
- new build

* Sun Mar 11 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.1
- disable static

* Sun Mar 11 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2
- new version

* Sat Sep 16 2006 Hihin Ruslan <ruslandh@altlinux.ru> 1.4.0-alt1
- first version for ALT-Linux

* Sat Jul 22 2006 Hihin Ruslan <hihin_c@t_narod_dot_ru> 1.4.0-alt1b
- new

* Sat Jul 22 2006 <hihin_cat_narod_dot_ru> 1.4.0-alt1.1
- cleanup spec

* Sun Jan 30 2005 Sir Pingus <pingus_77@yahoo.fr> 1.0.0-1
- 1.0.0 initial version
