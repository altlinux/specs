Name: rapid-photo-downloader
Version: 0.4.1
Release: alt1.1

Summary: Download photos and videos from cameras, memory cards and Portable Storage Devices
License: GPLv2+
Group: Graphics

Url: http://www.damonlynch.net/rapid/
Source: http://launchpad.net/rapid/trunk/%version/+download/%name-%version.tar.gz
Patch1: rapid-photo-downloader-0.4.1-webbrowser.patch

# Automatically added by buildreq on Sun Jun 19 2011
BuildRequires: python-devel

BuildArch: noarch

Requires: python-module-hachoir-metadata python-module-kaa-metadata ffmpegthumbnailer

%description
Rapid Photo Downloader is written by a photographer for professional and
amateur photographers. It can download photos from multiple memory cards
and Portable Storage Devices simultaneously. It provides a variety of
options for sub-folder creation, image renaming and backup. It does not
download images directly from a camera unless the camera is recognized
as an external drive.

%prep
%setup
%patch1 -p1

rm -f rapid/renamesubfolderprefstest.py

%build
%python_build

%install
%python_install

%find_lang %name

%files -f %name.lang
%_bindir/rapid-photo-downloader
%python_sitelibdir/*
%_desktopdir/*
%_pixmapsdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.4.1-alt1
- Initial build.
