%define ver_major 0.12
%def_disable nautilus

Name: postr
Version: %ver_major.4
Release: alt2.1

Summary: Flickr uploader
Group: Graphics
License: GPLv2+
Url: http://www.burtonini.com/blog/computers/postr

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2

%{?_disable_nautilus:BuildArch: noarch}

# from fedora
Patch: %name-0.12.4-nautilus-ext-dir.patch

Requires: %name-data = %version-%release

BuildRequires: python-devel rpm-build-python
%{?_enable_nautilus:BuildRequires: nautilus-python-devel}

%description
Postr is a Flickr uploading tool for the GNOME desktop, which aims to be
simple to use but exposing enough of Flickr to be useful.

%package data
Summary: Common files for the Postr
Group: Graphical desktop/GNOME
BuildArch: noarch

%description data
Postr is a Flickr uploading tool for the GNOME desktop.
This package provides common files for the Postr.

%package nautilus
Summary: Nautilus extension for the Postr
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description nautilus
Postr is a Flickr uploading tool for the GNOME desktop.
This package provides integration with the Postr for the Nautilus file
manager.

%add_python_compile_include %python_sitelibdir_noarch/postr

%prep
%setup -q
%patch -p1

%build
%python_build

%install
%python_install

%files

%files data
%_bindir/*
%python_sitelibdir_noarch/*
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*
%doc AUTHORS README TODO

%if_enabled nautilus
%files nautilus
%_libdir/nautilus/extensions-3.0/python/*
%endif

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt2
- don't build nautilus extension (current nautilus-python-0.7.3 is broken)

* Thu Feb 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- first build for Sisyphus

