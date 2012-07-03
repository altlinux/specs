%set_automake_version 1.9
%set_autoconf_version 2.5

%def_disable nopic

%define name 			libxdtv-theme-carbone-ru
%define m_name 			libxdtv_theme_carbone_ru
%define version 		2.4.0
%define base			xdtv

%define branch_point alt2
%define branch S1
%define revision 1

%define summary			%name is Theme %base NLS library for XdTV
%define LANG			ru

Name: %name
Summary: %summary
Version: %version

License: GPL
Url: http://xawdecode.sourceforge.net/
Release: %branch_point.%branch.%revision.qa1
Packager: Hihin Ruslan <ruslandh@altlinux.ru>
Source0: %name-%version.tar.gz
Patch0: libxdtv-i18n-ru-2.4.0.patch
Group: Video

BuildPreReq: libX11-devel 

# Automatically added by buildreq on Sat Jul 22 2006
BuildRequires: libXaw-devel libXpm-devel libX11-devel 
Requires: xdtv >= 2.4.0

%description
%summary

%prep
%setup -q
%patch0 -p1
%__subst "s|@NPACKAGE@|%name|" src/Makefile.am
%__subst "s|@LPACKAGE@|%m_name|" src/Makefile.am


%build
%__autoreconf
export FLAGS="%optflags -DNDEBUG -DNO_DEBUG -D_GNU_SOURCE "
%configure \
%{subst_enable nopic}


%make

%install
%makeinstall ROOT=%buildroot \
	     SUID_ROOT="" \
	     libdir="%buildroot%_libdir/%base"

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/%base/*.so*
%exclude %_libdir/%base/*.la

%changelog
* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.4.0-alt2.S1.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libxdtv-theme-carbone-ru
  * postun_ldconfig for libxdtv-theme-carbone-ru
  * distribution-tag for libxdtv-theme-carbone-ru
  * postclean-05-filetriggers for spec file

* Sat Jun 16 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.S1.1
- version for branch-4.0

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
