Name: gtkwave
Version: 3.3.34
Release: alt1
Summary: %name
License: GPL
Group: Development/Other

Packager: Denis Smirnov <mithraen@altlinux.ru>

Url: http://gtkwave.sourceforge.net/

Source: %name-%version.tar

# Automatically added by buildreq on Wed Apr 04 2012 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-server pkg-config python-base rpm-build-tcl shared-mime-info tcl tcl-devel xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel desktop-file-utils flex gperf libgtk+2-devel liblzma-devel tk-devel

%description
%summary

%prep
%setup

%build
%configure --disable-mime-update
%make_build
%install
%makeinstall_std

%files
%_bindir/*
%_man5dir/*
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/gnome/16x16/mimetypes/*.png
%_iconsdir/gnome/32x32/mimetypes/*.png
%_iconsdir/gnome/48x48/mimetypes/*.png
%_iconsdir/gtkwave_256x256x32.png
%_iconsdir/gtkwave_files_256x256x32.png
%_iconsdir/gtkwave_savefiles_256x256x32.png
%_datadir/mime/packages/*.xml

%changelog
* Wed Apr 04 2012 Denis Smirnov <mithraen@altlinux.ru> 3.3.34-alt1
- 3.3.34

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.26-alt2
- add buildrequires to liblzma-devel

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.26-alt1
- 3.3.26

* Fri Mar 25 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt5
- rebuild

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt4
- auto rebuild

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt3
- auto rebuild

* Thu Dec 31 2009 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt2
- add Url tag

* Sun Dec 27 2009 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt1
- first build for Sisyphus
