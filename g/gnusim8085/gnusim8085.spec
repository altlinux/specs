#TODO: http://live.gnome.org/GtkSourceView/PortingGuide

Name: gnusim8085
Version: 1.3.2
Release: alt1.qa3

Summary: Simulator and assembler for the Intel 8085 Microprocessor

License: GPL
Group: Emulators
Url: http://gnusim8085.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%name/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Sep 23 2007
BuildRequires: gcc-c++ libSM-devel libgnomeui-devel libgtksourceview1-devel

Obsoletes: GNUSim8085
Provides: GNUSim8085

%description
GNUSim8085 is a graphical simulator plus assembler with debugger for
the Intel 8085 microprocessor.  It is written using GNOME libs.  It
can also run on several window managers.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall
#mv %buildroot/%_prefix/doc %buildroot/%_docdir
rm -rf %buildroot/%_datadir/gnome/

sed -i -e 's,Encoding=UTF-8,Version=1.0,' GNUSim8085.desktop
echo 'Categories=System;Emulator;' >> GNUSim8085.desktop
install -D -m0644 GNUSim8085.desktop %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%_docdir/%name/
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*
%_datadir/gtksourceview-1.0/language-specs/8085asm.lang

%changelog
* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1.qa3
- NMU: second cleanup of .desktop files

* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1.qa2
- NMU: .desktop file cleanup

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gnusim8085
  * postclean-05-filetriggers for spec file

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- new version 1.3.2 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version 1.3 (with rpmrb script)
- enable update/clean menus scripts
- rename package to low case name
- update buildrequires

* Mon Jul 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.90-alt0.1
- initial build for ALT Linux Sisyphus
