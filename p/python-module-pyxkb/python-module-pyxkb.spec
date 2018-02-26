Name: python-module-pyxkb
Version: 0.1
Release: alt2.2.1.1
Summary: Python module for the X Keyboard Extension (XKB)
Group: Development/Python
License: GPL
URL: https://code.launchpad.net/~marceloshima/tacix/pyxkb

Packager: Boris Savelev <boris@altlinux.org>

Source0: %name-%version.tar
Patch: libxklavier.patch

# Automatically added by buildreq on Sat Jun 06 2009
BuildRequires: libX11-devel libxklavier-devel python-devel

%description
Python-XKB is a (over)simplified Python module for the X Keyboard Extension
 (XKB). It is written using the libxklavier library, and can perform simple
 tasks like:
   * Getting list of keyboard models defined in XKB
   * Getting list of layouts
   * Getting list of variants for a given layout
   * Setting the model, layout, variant and options to use

%prep
%setup
%patch0 -p1

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/pyxkb*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.2.1
- Rebuild with Python-2.7

* Wed Jun 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.2
- Fixed using of xkl_engine_stop_listen

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.1
- Rebuilt with python 2.6

* Fri Nov 20 2009 Boris Savelev <boris@altlinux.org> 0.1-alt2
- rebuild with new libxklavier

* Sat Jun 06 2009 Boris Savelev <boris@altlinux.org> 0.1-alt1
- initial build for Sisyphus

