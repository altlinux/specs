%def_disable nautilus

Name: arista
Version: 0.9.8
Release: alt0.1

Summary: An easy to use multimedia transcoder for the GNOME Desktop
Group: Video
License: LGPLv2+
Url: http://programmer-art.org/projects/arista-transcoder

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel nautilus-python-devel ImageMagick-tools rpm-build-gir

Requires: gst-plugins-base
Requires: gst-plugins-good
Requires: gst-plugins-bad
Requires: gst-plugins-ugly
# add manual requires
Requires: python-module-simplejson python-module-pyinotify lsdvd
BuildRequires: desktop-file-utils

%description
Arista is a multimedia transcoder for the GNOME Desktop. Arista
focuses on being easy to use by making the complex task of encoding
for various devices simple. Pick your input, pick your target device,
choose a file to save to and go.

%package -n nautilus-%name
Summary: Arista transcoder Nautilus extension
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Requires: nautilus-python
Provides: %name-nautilus = %version-%release
Obsoletes: %name-nautilus

%description -n nautilus-%name
Arista is a multimedia transcoder for the GNOME Desktop. Arista focuses
on being easy to use by making the complex task of encoding for various
devices simple. Pick your input, pick your target device, choose a file
to save to and go.

This package provides the ability to create conversions of media files
directly in Nautilus.

%prep
%setup -q

sed -i -e 's|Icon=/usr/share/arista/ui/icon.svg|Icon=%{name}|g' \
	%{name}.desktop


%build
%python_build

%install
%python_install

#icons.
mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
convert -scale 48 ui/icon.svg %buildroot%_liconsdir/%name.png
convert -scale 32 ui/icon.svg %buildroot%_iconsdir/%name.png
convert -scale 16 ui/icon.svg %buildroot%_miconsdir/%name.png

# cleanup
rm -rf %buildroot%_datadir/doc/%name
rm -rf %buildroot%_datadir/locale/templates

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/arista.desktop

%files -f %name.lang
%doc AUTHORS README.*
%_bindir/*
%python_sitelibdir_noarch/%{name}*.egg-info
%python_sitelibdir_noarch/%name
%_desktopdir/*
%_datadir/%name
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_man1dir/*

%if_enabled nautilus
%files -n nautilus-%name
%_datadir/nautilus-python/extensions/arista-nautilus.py
%endif

%changelog
* Thu May 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt0.1
- upstream snapshot edcf2565eea92014b55c1084acd12a832aab1ca2
- disable nautilus extension

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7-alt0.1.1
- Rebuild with Python-2.7

* Tue Jun 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.7-alt0.1
- upstream snapshot
- port nautilus extension to nautilus-3

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.5-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for arista

* Mon Jul 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt2
- build snapshot
- rename arista-nautilus to nautilus-arista
- move nautilus-python arista extension to noarch path
- add icons

* Fri Jul 02 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- first build for Sisyphus

