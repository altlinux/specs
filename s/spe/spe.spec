Name: spe
Summary: Integrated Python Development Environment
Version: 0.8.4.h
Release: alt3.1
License: GPL
Group: Development/Python
Url: http://pythonide.stani.be/
Packager: Fr. Br. George <george@altlinux.ru>
BuildArch: noarch
%setup_python_module %name
Source: %name-%version-wx2.6.1.0.tar.gz

# Automatically added by buildreq on Sat Apr 11 2009
BuildRequires: ImageMagick-tools OpenSP docbook-dtds docbook-to-man python-devel

Requires: %packagename = %version, pychecker

%description
SPE (Stani's Python Editor) is an Integrated Development Editor for the Python programming language (fully compatible with Blender). SPE has an editor with syntax highligthing and code completion, can generate UML diagram and code documentation using pydoc. spe is written using wxWidgets and integrate wxGlade and XRCed as plugins to make GUI creation easier. spe can also use pychecker for code check and winpdb to debug python code.

%package -n %packagename
Summary: Stani's Python Editor -- module files
License: GPL
Group: Development/Python

%description -n %packagename
SPE (Stani's Python Editor) is an Integrated Development Editor for the Python programming language (fully compatible with Blender).

This package is %name %__python_version module.

%prep
%setup

%build
python setup.py build

for size in 16x16 32x32 48x48 ; do
    convert _spe/images/spe.png -resize $size %name-$size.png
done

docbook-to-man %name.sgml > %name.1

%install
python setup.py install -O1 --skip-build --root="%buildroot" --prefix="%prefix"
install -D spe.desktop %buildroot%_desktopdir/spe.desktop
install -D _spe/images/spe.png %buildroot%_pixmapsdir/spe.png
for size in 16x16 32x32 48x48 ; do
    install -D %name-$size.png %buildroot%_iconsdir/hicolor/$size/apps/%name.png
done
install -D %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_desktopdir/*.desktop
%_pixmapsdir/*.png
%_iconsdir/*/*/*/*.png
%_man1dir/%name.*

%files -n %packagename
%python_sitelibdir/_%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4.h-alt3.1
- Rebuild with Python-2.7

* Mon Sep 20 2010 Fr. Br. George <george@altlinux.ru> 0.8.4.h-alt3
- Fix icons sizes
- Closes #23829

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4.h-alt2.1
- Rebuilt with python 2.6

* Sat Apr 11 2009 Fr. Br. George <george@altlinux.ru> 0.8.4.h-alt2
- PyCheker dependency (closes: #17750)
- Python module separation

* Fri May 23 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.8.4.h-alt1
- Initial ALT build
