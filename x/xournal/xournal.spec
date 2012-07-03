Name: xournal
Version: 0.4.5
Release: alt4

Summary: Xournal - application for notetaking, sketching, keeping a journal using a stylus
License: GPL
Group: Office

Url: http://xournal.sourceforge.net
Source: http://dl.sourceforge.net/xournal/%name-%version.tar.gz
Patch0: xournal-0.4.2.1-alt-desktop-file.patch
Patch1: xournal-no-copy-dt-needed-entries.patch
Patch2: xournal-poppler-0.18.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Mar 08 2009
BuildRequires: libgnomeprintui-devel libpoppler-glib-devel

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
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%autoreconf
%configure
%make

%install
%makeinstall_std
%find_lang %name
install -pDm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -pDm644 %name.glade %buildroot%_datadir/%name/%name.glade

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README src/TODO
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop

%changelog
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
