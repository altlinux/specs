# vim: set ft=spec: -*- rpm-spec -*-

Name: gcstar
Version: 1.6.1
Release: alt1

Summary: Personal collections manager
Group: Databases
License: GPL
Url: http://www.gcstar.org/

Requires: xdg-utils

Packager: Alexey Morsov <swi@altlinux.ru>

BuildArch: noarch

Source: http://download.gna.org/gcstar/%name-%version.tar
Patch: %name-%version-%release.patch

%define _perl_lib_path %perl_vendor_privlib:%_datadir/lib%name

# Automatically added by buildreq on Sat Jan 24 2009 (-bi)
BuildRequires: perl-Encode perl-Gtk2 perl-Switch perl-Unicode-Normalize perl-XML-LibXML perl-XML-Parser perl-XML-Simple
BuildRequires: perl-Locale-Codes

%description
GCstar is an application to manage different kind of collections. It
is designed to be able to support as many type of collections as
needed. For the moment it supports these ones:

 * Movies
 * Video games
 * Books
 * User defined collections

%prep
%setup -q -n %name
%patch -p1

%build
sed -i 's,@GCS_LIB_DIR@,%_datadir/lib%name,' bin/gcstar
sed -i 's,@GCS_SHARE_DIR@,%_datadir/%name,' bin/gcstar

%install
mkdir -p %buildroot{%_bindir,%_man1dir,%_datadir/{lib,}%name,%_desktopdir,%_xdgmimedir/packages,%_liconsdir,%_miconsdir,%_niconsdir}

install -p -m755 bin/gcstar %buildroot%_bindir/
cp -a lib/gcstar/* %buildroot%_datadir/lib%name/
cp -a share/gcstar/* %buildroot%_datadir/%name/
install -p -m644 share/gcstar/icons/gcstar_48x48.png %buildroot%_liconsdir/%name.png
install -p -m644 share/gcstar/icons/gcstar_16x16.png %buildroot%_miconsdir/%name.png
install -p -m644 share/gcstar/icons/gcstar_32x32.png %buildroot%_niconsdir/%name.png
install -p -m644 share/applications/gcstar.desktop %buildroot%_desktopdir/%name.desktop
install -p -m644 share/applications/gcstar.xml %buildroot%_xdgmimedir/packages/%name.xml
install -p -m644 man/* %buildroot/%_man1dir/

%files
%doc CHANGELOG README templates
%_bindir/*
%_man1dir/*
%_liconsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png
%_desktopdir/%name.desktop
%_xdgmimedir/packages/%name.xml
%_datadir/lib%name
%_datadir/%name

%changelog
* Tue Nov 09 2010 Alexey Morsov <swi@altlinux.ru> 1.6.1-alt1
- [1.6.1]

* Sun May 30 2010 Alexey I. Froloff <raorn@altlinux.org> 1.5.0-alt1
- [1.5.0]

* Sat Jan 24 2009 Sir Raorn <raorn@altlinux.ru> 1.4.3-alt1
- [1.4.3]
- Dropped obsolete %%update_menus/%%clean_menus calls
- Packaged MIME entry
- Fixed repocop warnings about desktop file

* Mon Sep 08 2008 Sir Raorn <raorn@altlinux.ru> 1.4.2-alt1
- [1.4.2]

* Mon Jul 09 2007 Sir Raorn <raorn@altlinux.ru> 1.1.1-alt1
- [1.1.1]

* Thu Jan 04 2007 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt1
- Built for Sisyphus

