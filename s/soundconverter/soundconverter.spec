# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: soundconverter
Version: 4.0.3
Release: alt1

Summary: A simple sound converter application for GNOME
License: GPL-3.0-or-later
Group: Sound

Url: https://github.com/kassoulet/soundconverter
Source: %name-%version.tar
Patch: soundconverter-4.0.0-drop-unity.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: intltool
BuildRequires: python3-devel
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-distutils-extra
BuildRequires: gir(Gst) = 1.0
BuildRequires: desktop-file-utils
Requires: gst-plugins-ugly1.0
Requires: gst-plugins-good1.0
Requires: gst-plugins-base1.0

%description
A simple sound converter application for the GNOME environment.
It reads and writes anything the GStreamer library can.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Audio \
	--add-category=AudioVideoEditing \
	build/share/applications/%name.desktop

# install locale
mkdir -p %buildroot%_datadir/locale
cp -a build/mo/* %buildroot%_datadir/locale
%find_lang %name

# remove unidentified locale
rm -r %buildroot%_datadir/locale/sr@Latn/

# Cleanup docdir
rm -r %buildroot%_datadir/doc/%name

%files -f %name.lang
%doc AUTHORS README.md
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/*.egg-info
%_datadir/%name
%_datadir/metainfo/%name.appdata.xml
%_datadir/glib-2.0/schemas/*
%_pixmapsdir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/*.svg

%changelog
* Sun Nov 07 2021 Anton Midyukov <antohami@altlinux.org> 4.0.3-alt1
- New version 4.0.3

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 4.0.1-alt1
- New version 4.0.1
- not require GConf

* Wed Jan 13 2021 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt1
- New version 4.0.0

* Fri Aug 07 2020 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1
- New version 3.1.0
- Update russian translation (Thanks Olesya Gerasimenko)

* Thu Jun 25 2020 Anton Midyukov <antohami@altlinux.org> 3.0.2-alt2.20200625
- New snapshot
- Added requires gst-plugins-base1.0

* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 3.0.2-alt1.20190423
- 3.0.2

* Sun Feb 10 2019 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1.20190207
- 3.0.1

* Fri Sep 14 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt3.20180902
- new snapshot

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt2.20180406.S1
- new snapshot

* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- 3.0.0 beta 1

* Sat Sep 24 2016 Anton Midyukov <antohami@altlinux.org> 2.1.6-alt1
- 2.1.6

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 2.0.2-alt1
- 2.0.2

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.4-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.5.4-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for soundconverter

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 1.5.4-alt1
- 1.5.4 (thanks force@)
- dropped patch

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.1
- Rebuilt with python 2.6

* Sat Oct 17 2009 Michael Shigorin <mike@altlinux.org> 1.4.4-alt1
- adapted for Sisyphus (heavily cleaned up fedora package)
