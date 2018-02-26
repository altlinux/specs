Name: gimmage
Version: 0.2.3
Release: alt4

Packager: Victor Forsyuk <force@altlinux.org>

Summary: A simple image viewer that supports command line operation
License: GPLv2+
Group: Graphics

Url: http://gimmage.berlios.de/
Source0: http://download.berlios.de/gimmage/gimmage-%version.tar.gz
Source1: gimmage.desktop
Patch1: gimmage-0.2.3-gcc43.patch

# Automatically added by buildreq on Wed Nov 19 2008
BuildRequires: gcc-c++ libcurl-devel libgtkmm2-devel libmagic-devel

%description
Gimmage is a simple image viewer that aims to have a minimalist interface and
tries to be keyboard operable for browsing through a large number of images
quickly. It is appropriate for command line usage as it accepts directories
and image filenames as arguments. It has an in-application file browser that
allows users to select and drag images and directories into the image viewing
area in order to have them displayed.

%prep
%setup
%patch1 -p1

%build
# Sorry, LAZY fixing for as-needed (one-liner, not patch).
%__subst 's/ -lcurl -lmagic//; s/^LDADD = /LDADD = -lcurl -lmagic /' src/Makefile.in

%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -p -m644 %SOURCE1 %buildroot%_desktopdir/

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/gimmage
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Wed Nov 19 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt4
- Fix FTBFS with gcc4.3.
- Remove obsolete post-scripts.

* Fri Apr 11 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt3
- Desktop mime entry fix.

* Tue Sep 25 2007 Victor Forsyuk <force@altlinux.org> 0.2.3-alt2
- Add required menu updating scripts.

* Fri Sep 14 2007 Victor Forsyuk <force@altlinux.org> 0.2.3-alt1
- Initial build.
