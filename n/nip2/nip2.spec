Name: nip2
Version: 7.28.4
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: An image processing system
License: GPLv2+
Group: Graphics

Url: http://www.vips.ecs.soton.ac.uk
Source0: %{name}-%{version}.tar.gz
Source1: %name.xpm
Source100: nip2.watch

Requires: vips >= 7.8.6
Provides: nip = %version
Obsoletes: nip <= 7.8.11

# Automatically added by buildreq on Fri Aug 13 2010
BuildRequires: desktop-file-utils flex libgsl-devel libgtk+2-devel libvips-devel xdg-utils
BuildRequires: gcc-c++

%description
nip2 is an image processing system. It is good for very large
images (ie. larger than the amount of RAM in your machine), and
for working with colour. In use it's rather like a spreadsheet.
There's complete documentaion.

%package doc
Summary: Documentation for %name
Group: Graphics
BuildArch: noarch

%description doc
Documentation for %name.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

install -pDm644 %SOURCE1 %buildroot%_niconsdir/nip2.xpm
install -pDm644 nip2.desktop %buildroot%_desktopdir/nip2.desktop

# copy the formatted PS and HTML docs into the install area
cp -a doc/html doc/pdf %buildroot%_docdir/%name/

%files
%_bindir/nip2
%_bindir/run-nip2.sh
%_man1dir/*
%_datadir/nip2
%_desktopdir/*.desktop
%_niconsdir/*
%_datadir/mime/packages/nip2.xml
%_datadir/mime/image/x-vips.xml

%files doc
%_docdir/%name

# TODO:
# - look into uninstalled /usr/share/mime/*

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 7.28.4-alt1
- new version (watch file uupdate)

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 7.28.3-alt1
- 7.28.3

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 7.26.4-alt1
- 7.26.4
- drop RPATH

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 7.26.3-alt1
- 7.26.3 (thx fedorawatch)

* Mon Apr 04 2011 Michael Shigorin <mike@altlinux.org> 7.24.1-alt2
- don't include mimeinfo.cache
- amended BR:

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 7.24.1-alt1
- 7.24.1 (thanks force@)

* Sat Oct 16 2010 Michael Shigorin <mike@altlinux.org> 7.22.3-alt1
- 7.22.3
- minor spec cleanup

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 7.22.2-alt1
- 7.22.2

* Thu Dec 03 2009 Victor Forsyuk <force@altlinux.org> 7.20.6-alt1
- 7.20.6

* Mon Aug 10 2009 Michael Shigorin <mike@altlinux.org> 7.18.2-alt1
- 7.18.2

* Mon Mar 23 2009 Michael Shigorin <mike@altlinux.org> 7.16.4-alt2
- applied repocop patch

* Sat Mar 21 2009 Michael Shigorin <mike@altlinux.org> 7.16.4-alt1
- 7.16.4
- autoreconf

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt3
- added Packager:
- require libified vips
- minor spec cleanup

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt2
- applied repocop patch

* Mon Nov 17 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt1
- 7.16.3

* Tue Oct 07 2008 Michael Shigorin <mike@altlinux.org> 7.16.2-alt1
- 7.16.2
- fixed build (buildreq)
- renamed package to nip2
- spec cleanup
- replaced debian menufile with desktop file
- NB: the package seeks proper maintainer

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 7.8.11-alt2.1
- Rebuilt with libtiff.so.4.

* Tue Nov 04 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.11-alt2
- cleanup spec

* Mon Sep 15 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.11-alt1
- new version

* Fri May 09 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.7-alt1
- adapted for Sisyphus, create menu and icon.

* Mon Feb 3 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.6-2
- hack to change default install prefix to /usr/local

* Thu Jan 30 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.6-1
- first stab at an rpm package for nip
