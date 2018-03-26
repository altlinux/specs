Name: rapid-photo-downloader
Version: 0.9.9
Release: alt1

%define xdg_name net.damonlynch.%name

Summary: Download photos and videos from cameras, memory cards and Portable Storage Devices
License: GPLv3+
Group: Graphics

Url: http://www.damonlynch.net/rapid/
Source: http://launchpad.net/rapid/pyqt/%version/+download/%name-%version.tar.gz

BuildArch: noarch

BuildRequires: intltool perl-podlators
BuildRequires: rpm-build-gir
BuildRequires: rpm-build-python3 python3-devel python3-module-setuptools

%if "%(rpmvercmp '%{get_version python3}' '3.6.0')" <= "0"
Requires: python3-module-typing >= 3.6.4
%endif

Requires: python3-module-PyQt5 >= 5.9.2
Requires: python3-module-easygui
Requires: python3-module-pymediainfo >= 2.2.0
Requires: python3-module-rawkit >= 0.6.0
Requires: python3-module-pyprind
Requires: python3-module-colorlog
Requires: exiv2 perl-Image-ExifTool
Requires: gst-plugins-good1.0 gst-libav

%add_typelib_req_skiplist typelib(Unity)

%description
Rapid Photo Downloader imports photos and videos from cameras, phones,
memory cards and other devices at high speed. It can be configured to
rename photos and videos with meaningful filenames you specify. It can
also back up photos and videos as they are downloaded. It downloads from
and backs up to multiple devices simultaneously.

%prep
%setup
subst "s|'share\/solid\/actions'|'share/apps/solid/actions'|" setup.py

%build
%python3_build

%install
%python3_install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/analyze-pv-structure
%python3_sitelibdir/*
%_desktopdir/%xdg_name.desktop
%_datadir/appdata/%xdg_name.appdata.xml
%_man1dir/analyze-pv-structure.1.*
%_man1dir/%name.1.*
%_datadir/apps/solid/actions/%xdg_name.desktop
%doc README.rst RELEASE_NOTES.rst CHANGES.rst


%changelog
* Mon Mar 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9

* Tue Feb 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.8-alt1
- 0.9.8

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.10-alt1
- 0.4.10

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.4.1-alt1
- Initial build.
