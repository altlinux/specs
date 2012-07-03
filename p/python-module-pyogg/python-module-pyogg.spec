Name: python-module-pyogg
Version: 1.3
Release: alt5.1.1

Summary: A Python module for the the Ogg library
Group: Development/Python
License: GPL
Url: http://www.andrewchatham.com/pyogg

Packager: Dmitry Vukolov <dav@altlinux.ru>

%setup_python_module pyogg

Source: %url/download/%modulename-%version.tar.bz2

%define libogg_ver 1.0

Requires: libogg >= %libogg_ver

Provides: pyogg = %version
Obsoletes: pyogg

BuildPreReq: libogg-devel >= %libogg_ver

# Automatically added by buildreq on Mon Jul 19 2004
BuildRequires: libogg-devel python-devel python-modules-encodings

%description
%name is a wrapper for Ogg library.

%package devel
Summary: %name header and example programs
Group: Development/Python
Requires: %name = %version-%release
Provides: pyogg-devel = %version
Obsoletes: pyogg-devel

%description devel
%name is a wrapper for Ogg library.

Install %name-devel if you need the API documentation and example
programs.

%define python_libdir %_libdir/python%_python_version
%define python_site_packages_dir %python_libdir/site-packages
%define python_includedir %_includedir/python%_python_version

%prep
%setup -n %modulename-%version

%build
export CFLAGS="%optflags"
python config_unix.py --prefix=/usr
%python_build_debug

%install
%python_install --optimize=2

%files
%python_site_packages_dir/ogg
%python_site_packages_dir/*.egg-info
%doc AUTHORS ChangeLog README

%files devel
%python_includedir/%modulename
%doc test/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt5.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt5.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt5
- Rebuilt for debuginfo

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt4
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.3-alt3.1
- Rebuilt with python-2.5.

* Fri Mar 25 2005 Dmitry Vukolov <dav@altlinux.ru> 1.3-alt3
- rebuild with python 2.4

* Mon Jul 19 2004 Dmitry Vukolov <dav@altlinux.ru> 1.3-alt2
- renamed package from pyogg to python-module-pyogg
- repackaged according to the new python policy

* Thu Apr 15 2004 Dmitry Vukolov <dav@altlinux.ru> 1.3-alt1
- version 1.3

* Thu Dec 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt1
- First build for Sisyphus.
