%define oname PyPanel

Name: python-module-%oname
Version: 2.4
Release: alt4.4.1.1

Summary: Lightweight panel/taskbar for X11 Window Managers
Group: Graphical desktop/Other
License: GPL
Url: http://pypanel.sourceforge.net/

Source0: %oname-%version.tar.gz

Patch0: PyPanel-2.4-alt-spaces.patch
Patch1: PyPanel-2.4-alt-python.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Provides: %oname = %version-%release
Obsoletes: %oname < %version-%release

# Automatically added by buildreq on Sun Aug 02 2009
BuildRequires: imlib2-devel libXext-devel libXft-devel python-devel
BuildPreReq: python-module-xlib zlib-devel

%description
PyPanel is a lightweight panel/taskbar written in Python and C for X11 window
managers.  It can be easily customized to match any desktop theme or taste.
PyPanel works with EWMH compliant WMs.

The panel displays currently running tasks/applications and can also be
configured to display the current desktop name, date/time, a system tray
(notification area) and application launcher.

%prep
%setup
%patch0 -p1
%patch1 -p1

%install

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
%python_build_install --optimize=2 --record=INSTALLED_FILES

#unset RPM_PYTHON

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/pypanel \
	%buildroot%python_sitelibdir/
%endif

%files
%_bindir/*
%python_sitelibdir/*
%doc README

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4-alt4.4.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4-alt4.4.1
- Rebuild with Python-2.7

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt4.4
- Fixed build

* Tue Jun 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt4.3
- Applied upstream patches

* Mon Jun 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt4.2
- Fixed path to files
- Renamed package

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt4.1
- Rebuilt with python 2.6

* Sun Aug 02 2009 Igor Zubkov <icesik@altlinux.org> 2.4-alt4
- buildreq

* Wed Jan 30 2008 Grigory Batalov <bga@altlinux.ru> 2.4-alt3.1
- Rebuilt with python-2.5.

* Wed Jan 23 2008 Grigory Batalov <bga@altlinux.ru> 2.4-alt3
- Get python version from sys.version_info.

* Fri Jul 06 2007 Igor Zubkov <icesik@altlinux.org> 2.4-alt2
- fix unresolved
- buildreq

* Thu Jun 08 2006 Igor Zubkov <icesik@altlinux.ru> 2.4-alt1
- Initial build for Sisyphus
