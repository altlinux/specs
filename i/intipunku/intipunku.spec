# TODO: build with python vlc module
# test new define
%define _python_egg_info %python_sitelibdir/%name-%version-py%__python_version.egg-info

%define rel %nil

Name: intipunku
Version: 0.52
Release: alt1.1.1

Summary: A sunny photo manager

Group: Graphics
License: GPL3
Url: http://code.google.com/p/intipunku/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://intipunku.googlecode.com/files/%name-%version%rel.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Thu Nov 13 2008
BuildRequires: python-devel

BuildPreReq: rpm-build-python

%add_python_req_skip EasyDialogs vlc win32com win32gui

%description
IntiPunku is a photo manager which aims at feature richness and ease
of use. Originally the idea was to create a clone of the popular photo
manager Picasa on windows. The name means Sun Gate and originates from
historical site Tiwanaku in Bolivia. Tiwanaku is till now know as the
legacy of the oldest civilization of South America.

%prep
%setup -n %name-%version%rel

%build
%python_build

%install
%python_install
%find_lang %name

%files -f %name.lang
%doc FEATURES TODO credits.txt license.txt
%_bindir/%name
%_bindir/%name-import
%_bindir/%name-viewer
%python_sitelibdir/inti/
%_datadir/%name/
%_pixmapsdir/%name.png
%_desktopdir/*.desktop
%_python_egg_info

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.52-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.52-alt1.1
- Rebuilt with python 2.6

* Thu Aug 20 2009 Vitaly Lipatov <lav@altlinux.ru> 0.52-alt1
- new version 0.52 (with rpmrb script)

* Thu Nov 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Linux Sisyphus
