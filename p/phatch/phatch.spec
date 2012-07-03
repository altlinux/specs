%define gnome_libdir %_libdir
%define gnome_mimedir %_datadir/mime

Name: phatch
Version:	0.2.7.1
Release:	alt3.1
%setup_python_module %name
Summary:  Easy-to-use graphical photo batch processor and EXIF renamer
Source:		%{name}-%{version}.tar.gz
Url: http://photobatch.stani.be/
Group: Graphics
License: GPL v3
Patch1: do_not_raise_string_exceptions.patch
Patch2: pyexiv2.patch
Buildarch: noarch
Requires: %packagename = %version

# Automatically added by buildreq on Sat Nov 01 2008
BuildRequires: python-devel python-modules-encodings desktop-file-utils
%add_python_req_skip core app

%description
Phatch is a simple to use cross-platform graphical Photo Batch Processor
and Exif Renamer with a nice graphical user interface. Phatch handles
all popular image formats and can duplicate (sub)folder hierarchies.
Phatch can batch resize, rotate, apply shadows, perspective, rounded
corners,  and do much more actions in minutes instead of hours or days
if you do it manually.

%package -n %packagename
Group: Graphics
Summary: Phatch python API module
Requires:	/usr/bin/locate
%description -n %packagename
Phatch is a simple to use cross-platform graphical Photo Batch Processor
and Exif Renamer with a nice graphical user interface. Phatch handles
all popular image formats and can duplicate (sub)folder hierarchies.
Phatch can batch resize, rotate, apply shadows, perspective, rounded
corners,  and do much more actions in minutes instead of hours or days
if you do it manually.

This package provides Python API modiule for Phatch.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
python ./setup.py build

%install
python ./setup.py install --prefix="%prefix" --root="%buildroot"

sed -i '\|^$|d' %buildroot%_desktopdir/%name.desktop

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--dir %buildroot%_desktopdir\
	 %buildroot%_desktopdir/%name.desktop

%find_lang %name

%clean
rm -rf "%buildroot"

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/*/*/apps/*
%doc %_man1dir/%name.1*
%gnome_mimedir/packages/%name.xml
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/pixmaps/*.png

%files -n %packagename
%python_sitelibdir/*

%changelog
* Fri Nov 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.7.1-alt3.1
- Rebuild with Python-2.7

* Fri Nov 04 2011 Fr. Br. George <george@altlinux.ru> 0.2.7.1-alt3
- Debian patches added

* Sat Nov 06 2010 Fr. Br. George <george@altlinux.ru> 0.2.7.1-alt2
- Dependency to /usr/bin/locate added (closes #24372)

* Sun Aug 29 2010 Fr. Br. George <george@altlinux.ru> 0.2.7.1-alt1
- Version up

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.1
- Rebuilt with python 2.6

* Thu Oct 22 2009 Fr. Br. George <george@altlinux.ru> 0.1.6-alt1
- Version up

* Sat Nov 01 2008 Fr. Br. George <george@altlinux.ru> 0.1.5-alt1
- Initial build from pclos
- Version up

* Thu Sep 11 2008 Neverstopdreaming 0.1.4.bzr526-2
- Rebuild

* Thu May 26 2008 Stumpy842 <stump842@gmail.com> 0.1.4bzr526-1
- Import for pclos
