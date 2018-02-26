Name: cairo-clock
Version: 0.3.4
Release: alt1.qa3

Summary: MacSlow's Cairo-Clock

Url: http://macslow.thepimp.net/?page_id=23
License: GPL
Group: Office

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://macslow.thepimp.net/projects/cairo-clock/%{name}-%version.tar.bz2

# manually removed: libnss-mysql 
# Automatically added by buildreq on Thu Jan 03 2008
BuildRequires: gcc-c++ glibc-devel libglade-devel librsvg-devel perl-XML-Parser
BuildRequires: desktop-file-utils

%description
It's an analog clock displaying the system-time.
It leverages the new visual features offered by Xorg 7.0 in combination
with a compositing-manager (e.g. compiz), gtk+ 2.10.x, cairo 1.2.0 and
librsvg 2.14.0 to produce a time-display with pretty-pixels.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Clock \
	%buildroot%_desktopdir/cairo-clock.desktop

%files -f %name.lang
%doc AUTHORS README NEWS
%_bindir/%name
%_datadir/%name/
%_desktopdir/*
%_man1dir/*
%_pixmapsdir/*

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.4-alt1.qa3
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for cairo-clock

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.4-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * update_menus for cairo-clock
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for cairo-clock

* Sat Mar 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.4-alt1
- new version 0.3.4 (with rpmrb script)

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt1
- initial build for ALT Linux Sisyphus
