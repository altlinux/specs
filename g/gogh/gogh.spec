# test new macroses
%define python_build CFLAGS="%optflags" %__python setup.py build
%define python_install %__python setup.py install --root %buildroot

%define oname Gogh
Name: gogh
Version: 0.1.2.3
Release: alt1.1
Summary: 2D graphical editor

Group: Graphics
License: GPL
Url: http://www.goghproject.com/
Packager: Vitaly Lipatov <lav@altlinux.ru>
BuildArch: noarch

Source: http://www.goghproject.com/%oname-%version.tar.bz2

# Typical environment for GNOME program
#Requires(post): GConf2
#Requires(post,postun): scrollkeeper
#Requires(post,postun): desktop-file-utils
#BuildPreReq: GConf2
#BuildPreReq: desktop-file-utils
#BuildPreReq: menu-devel

#add_python_req_skip brushdata brushmanagementdialog brushmanager brushstroke colordialog goghdoc goghglobals goghutil goghview layersdialog resizedialog savedialog scaledialog

Requires: python-module-PyXML librsvg
Requires: python%__python_version(libglade)
# python%__python_version(PyXML)
#add_python_lib_path %python_sitelibdir/

# Automatically added by buildreq on Thu Jun 19 2008
BuildRequires: python-devel

%description
Gogh is a GNU/Linux bitmap graphics editor. It is designed to work with
pressure-sensitive input devices, like a Wacom tablet.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install
# hack
cp *.xml %buildroot%python_sitelibdir/
cp *.py %buildroot%python_sitelibdir/
cp -a glade/ %buildroot%python_sitelibdir/
rm -f %buildroot%python_sitelibdir/setup*
%find_lang %name

%files -f %name.lang
%doc PKG-INFO
%_bindir/%name
%python_sitelibdir/*
# hack
%python_sitelibdir/glade/
#_datadir/%name/
#_datadir/mime/packages/*
#_pixmapsdir/*
#_desktopdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2.3-alt1.1
- Rebuild with Python-2.7

* Sun Jan 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2.3-alt1
- Version 0.1.2.3
- Rebuilt without python-module-Numeric

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2.1-alt1.1
- Rebuilt with python 2.6
- Set as noarch package

* Thu Jun 19 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.2.1-alt1
- initial build for ALT Linux Sisyphus
