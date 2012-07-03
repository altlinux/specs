Name: python-module-pyvorbis
Version: 1.4
Release: alt1.1.1

Summary: A Python module for the the Ogg/Vorbis library
Group: Development/Python
License: GPL
Url: http://www.andrewchatham.com/pyogg

Packager: Python Development Team <python@packages.altlinux.org>

%setup_python_module pyvorbis

Source: %url/download/%modulename-%version.tar.bz2

%define libvorbis_ver 1.0
%define pyogg_ver 1.3

Requires: libvorbis >= %libvorbis_ver
Requires: python-module-pyogg >= %pyogg_ver

Provides: pyvorbis = %version
Obsoletes: pyvorbis

BuildPreReq: libvorbis-devel >= %libvorbis_ver
BuildPreReq: python-module-pyogg-devel >= %pyogg_ver

# Automatically added by buildreq on Mon Jul 19 2004
BuildRequires: libogg-devel libvorbis-devel python-devel python-module-pyogg-devel python-modules-encodings

%description
%name is a wrapper for libvorbis, a compressed audio format library.

%package devel
Summary: %name headers and example programs
Group: Development/Python
Requires: %name = %version-%release
Provides: pyvorbis-devel = %version
Obsoletes: pyvorbis-devel

%description devel
%name is a wrapper for libvorbis, a compressed audio format library.

Install %name-devel if you need the API documentation and example
programs.

%define python_libdir %_libdir/python%_python_version
%define python_site_packages_dir %python_libdir/site-packages
%define python_includedir %_includedir/python%_python_version

%prep
%setup -q -n %modulename-%version

%build
export CFLAGS="%optflags"
python config_unix.py --prefix /usr
%python_build

%install
%python_install --optimize=2

mkdir -p %buildroot%python_includedir/%modulename
install -m644 src/*.h %buildroot%python_includedir/%modulename
chmod -x test/*

%files
%python_site_packages_dir/ogg/*.so
%python_site_packages_dir/*.egg-info
%doc AUTHORS ChangeLog README

%files devel
%python_includedir/%modulename
%doc test/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt4
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.3-alt3.1
- Rebuilt with python-2.5.

* Fri Mar 25 2005 Dmitry Vukolov <dav@altlinux.ru> 1.3-alt3
- rebuilt with python 2.4

* Mon Jul 19 2004 Dmitry Vukolov <dav@altlinux.ru> 1.3-alt2
- renamed package from pyvorbis to python-module-pyvorbis
- repackaged according to the new python policy

* Thu Apr 15 2004 Dmitry Vukolov <dav@altlinux.ru> 1.3-alt1
- version 1.3

* Thu Dec 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt1
- First build for Sisyphus.

