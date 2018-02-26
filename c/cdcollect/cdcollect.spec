# stalled. checked at 13.01.2009
Name: cdcollect
Version: 0.6.0
Release: alt5

Summary: CD/DVD catalog application for GNOME

Group: Office
License: GPL
Url: http://cdcollect.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Patch: cdcollect-0.6.1.patch
Patch2: cdcollect-0.6.1-sqlite.patch
Patch3: cdcollect-0.6.0-desktop.patch

# Typical environment for GNOME program
Requires(post): GConf2
Requires(post,postun): scrollkeeper
BuildPreReq: libGConf2-devel
BuildPreReq: desktop-file-utils

# Automatically added by buildreq on Tue Sep 08 2009
BuildRequires: GConf gcc-c++ glib2-devel libgnome-sharp mono-data-sqlite mono-mcs perl-XML-Parser

# FIXME: broken buildreq for mono packages?
BuildPreReq: libgtk-sharp2-devel libgnome-sharp-devel libsqlite3-devel mono-devel

BuildRequires: /proc

%description
CDCollect is a CD/DVD catalog application for gnome 2.16. Its
functionality is similar to the old gtktalog application for gnome 1.4.
It's goal is to be able to catalog your entire CD collection allowing
for searches of your CD/DVD files with a clean and simple interface.

%prep
%setup -q
%patch -p1
%patch2 -p1
%patch3 -p1

%build
%configure --disable-schemas-install --disable-scrollkeeper
%make_build

%install
# overwrite libdir for fix x86_64 build
%makeinstall_std cdcollectlibdir=%_libdir/%name
# fix for user cdcollectlibdir instead
sed -i "s|/usr/lib|%_libdir|g" %buildroot/%_bindir/%name

%find_lang %name --with-gnome
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=Application \
	--add-category=AudioVideo \
	--add-category=Database \
	%buildroot%_desktopdir/cdcollect.desktop

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc AUTHORS ChangeLog README NEWS
%_bindir/%name
%_libdir/%name/
%_pixmapsdir/*
%_desktopdir/*
%config %_sysconfdir/gconf/schemas/*

%changelog
* Wed Feb 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt5
- svn trunk
- rebuild with new mono-2.10

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.0-alt4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for cdcollect
  * freedesktop-desktop-file-proposed-patch for cdcollect
  * postclean-03-private-rpm-macros for the spec file

* Tue Sep 08 2009 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt4
- update buildreqs

* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt3
- cleanup spec, rebuild package (fix bug #18496)

* Thu Oct 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt2
- fix build on x86_64

* Thu Oct 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for ALT Linux Sisyphus

