Name: gtkcdlabel
Version: 1.0pre8
Release: alt4

Summary: a utility to generate cd covers with cdlabelgen
License: GPL
Group: Archiving/Cd burning

Url: http://gtkcdlabel.sf.net
Source: %{name}_%version.tar.gz
Patch1: gtkcdlabel-1.0pre8-alt-paths.patch
Patch2: gtkcdlabel-1.0pre8-alt-a4letter.patch

Requires: cdlabelgen >= 2.2.0
#Requires: %_bindir/evince

# Automatically added by buildreq on Tue May 06 2008
BuildRequires: libglade-devel

%description
A utility to generate cd covers with cdlabelgen.
Based on code from gcombust and gcdlabelgen.

You might want to install evince for previews.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
export LDFLAGS="${LDFLAGS:- -export-dynamic}"
export CFLAGS="%optflags"
%configure
%make
 
%install
%makeinstall
install -pD -m644 %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc README ChangeLog INSTALL AUTHORS
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*

# FIXME: broken version will require Serial: to upgrade cleanly;
# see http://wiki.sisyphus.ru/devel/spectips/Release

# TODO: 
# - evince isn't a hard dependency, it's only suggested but configurable

%changelog
* Tue May 06 2008 Michael Shigorin <mike@altlinux.org> 1.0pre8-alt4
- moved desktop file to current location, thanks viy@
- removed dependency on evince
- buildreq

* Mon Nov 05 2007 Michael Shigorin <mike@altlinux.org> 1.0pre8-alt3
- replaced Requires: to %%_bindir/evince as proposed by lav@
  (due to binary now provided by both evince and evince-gtk)
- added patch to replace /mnt/cdrom default with /media/cdrom
- added patch to fix default paper size (s/Letter/A4/g)

* Sat Nov 11 2006 Michael Shigorin <mike@altlinux.org> 1.0pre8-alt2
- added Requires: evince (fixes: #10160)

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 1.0pre8-alt1
- 1.0pre8

* Sat Sep 03 2005 Michael Shigorin <mike@altlinux.org> 1.0pre7-alt1
- 1.0pre7

* Mon Feb 09 2004 Michael Shigorin <mike@altlinux.ru> 1.0pre6-alt1
- pre6
- for *ALT Linux* I said! :)

* Tue Nov 25 2003 Michael Shigorin <mike@altlinux.ru> 1.0pre4-1
- built for ALT Linux

