%define oname metakit
Name: python-module-%oname
Version: 2.4.9.7
Release: alt1.1.1

Summary: Metakit is an embeddable database

License: GPL
Group: Development/Python
Url: http://www.equi4.com/metakit/python.html

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://www.equi4.com/pub/mk/%oname-%version.tar.bz2

%setup_python_module %oname

# Automatically added by buildreq on Fri Mar 14 2008
BuildRequires: gcc-c++ python-devel

%description
Metakit is an embeddable database which runs on Unix, Windows,
Macintosh, and other platforms.  It lets you build applications which
store their data efficiently, in a portable way, and which will not
need a complex runtime installation.  In terms of the data model,
Metakit takes the middle ground between RDBMS, OODBMS, and flat-file
databases - yet it is quite different from each of them.

%prep
%setup -q -n %oname-%version
sed -i 's|python2\.5|python%__python_version|g' unix/configure
%ifarch x86_64
sed -i 's|lib/python|lib64/python|g' unix/configure
%endif

%build
cd builds
../unix/configure --prefix=%_prefix --with-python=%_prefix
%make_build python

%install
cd builds
mkdir -p %buildroot%python_sitelibdir/
%make_install install-python DESTDIR=%buildroot pylibdir=%python_sitelibdir

%files
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.9.7-alt1.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9.7-alt1.1
- Rebuilt with python 2.6

* Fri Mar 14 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.9.7-alt1
- initial build for ALT Linux Sisyphus
