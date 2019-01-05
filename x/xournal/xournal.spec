Name: xournal
Version: 0.4.8.2016
Release: alt2

Summary: Xournal - application for notetaking, sketching, keeping a journal using a stylus
License: GPL
Group: Office

Url: http://xournal.sourceforge.net
Source0: http://dl.sourceforge.net/xournal/%name-%version.tar.gz
Source1: %name.watch
Source2: %name.1
Patch: xournal-0.4.2.1-alt-desktop-file.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Mar 08 2009
BuildRequires: libpoppler-glib-devel libgnomecanvas-devel libgtk+2-devel
BuildRequires: rpm-build-xdg

Summary(pl.UTF-8): Xournal - aplikacja do tworzenia notatek, szkicowania i prowadzenia dziennika pisakiem

%description
Xournal is an application for notetaking, sketching, keeping a journal
using a stylus. It is similar to Microsoft Windows Journal or to other
alternatives such as Jarnal and Gournal.

%description -l pl.UTF-8
Xournal to aplikacja do tworzenia notatek, szkicowania i prowadzenia
dziennika przy użyciu pisaka. Jest podobna do Microsoft Windows
Journal czy innych alternatyw takich jak Jarnal i Gournal.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std desktop-install
%find_lang %name
install -pDm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -pDm644 %name.glade %buildroot%_datadir/%name/%name.glade
install -pDm644 %SOURCE2 %buildroot%_man1dir/%name.1

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README src/TODO
%_bindir/*
%_datadir/%name
%_man1dir/%name.1*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/*/*.svg
%_xdgmimedir/*/*.xml
%_datadir/mimelnk/application/x-xoj.desktop

%changelog
* Sun Jan 06 2019 Michael Shigorin <mike@altlinux.org> 0.4.8.2016-alt2
- fix BR: (thx bircoph@)

* Tue Jul 25 2017 Michael Shigorin <mike@altlinux.org> 0.4.8.2016-alt1
- new version (watch file uupdate)

* Sat Aug 02 2014 Michael Shigorin <mike@altlinux.org> 0.4.8-alt1
- 0.4.8

* Sun Apr 13 2014 Michael Shigorin <mike@altlinux.org> 0.4.7-alt1
- added watch file and manpage from debian
- new version (watch file uupdate)
  + dropped patch1 (fails to apply), patch2 (merged upstream)
- install desktop icons and configuration files

* Mon Mar 25 2013 Michael Shigorin <mike@altlinux.org> 0.4.5-alt5
- rebuilt without libgnomeprintui-devel

* Sat Nov 12 2011 Michael Shigorin <mike@altlinux.org> 0.4.5-alt4
- applied opensuse patches, thanks zerg@ for a pointer
  (the one regarding poppler)

* Wed Mar 09 2011 Michael Shigorin <mike@altlinux.org> 0.4.5-alt3
- rebuilt against current libpoppler

* Tue Aug 31 2010 Michael Shigorin <mike@altlinux.org> 0.4.5-alt2
- rebuilt against current libpoppler

* Mon Nov 02 2009 Michael Shigorin <mike@altlinux.org> 0.4.5-alt1
- 0.4.5
- applied desktop file patch by icesik@

* Sun Mar 08 2009 Michael Shigorin <mike@altlinux.org> 0.4.2.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- heavy spec cleanup
