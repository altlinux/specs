%define ver_major 0.13
%def_disable nautilus

Name: postr
Version: %ver_major.1
Release: alt1

Summary: Flickr uploader
Group: Graphics
License: GPLv2+
Url: http://www.burtonini.com/blog/computers/postr

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch
Obsoletes: %name-data

BuildRequires: python-module-pygobject3-devel
BuildRequires: intltool gnome-doc-utils
BuildRequires: libnautilus-devel python-module-pygtk-devel nautilus-python-devel

%description
Postr is a Flickr uploading tool for the GNOME desktop, which aims to be
simple to use but exposing enough of Flickr to be useful.

%package nautilus
Summary: Nautilus extension for the Postr
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description nautilus
Postr is a Flickr uploading tool for the GNOME desktop.
This package provides integration with the Postr for the Nautilus file
manager.

%prep
%setup

%build
%configure \
    --with-nautilus-extension-dir=%_datadir/nautilus-python/extensions

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%python_sitelibdir_noarch/%name/
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*
%doc AUTHORS README TODO

%if_enabled nautilus

%files nautilus
%_datadir/nautilus-python/extensions/*
%endif

%changelog
* Sun Jul 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Thu Oct 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt2
- don't build nautilus extension (current nautilus-python-0.7.3 is broken)

* Thu Feb 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- first build for Sisyphus

