%define oname ftputil
Name: python-module-%oname
Version: 2.2.3
Release: alt2.1.1

Summary: high-level interface to the ftplib module

License: GPL
Group: Development/Python
Url: http://ftputil.sschwarzer.net/trac

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://ftputil.sschwarzer.net/trac/attachment/wiki/Download/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# Automatically added by buildreq on Wed Oct 24 2007
BuildRequires: python-devel python-modules-compiler

%description
The ftputil Python library is a high-level interface to the ftplib
module. The FTPHost objects generated with ftputil allow many operations
similar to those of os  and os.path

%prep
%setup -q -n %oname-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

pushd %buildroot%python_sitelibdir/%oname
TXTS=$(ls README.html 2>/dev/null|wc -l)
if [ "$TXTS" = "0" ]; then
mv %buildroot%_libdir/python%__python_version/site-packages/%oname/*.html \
	%buildroot%_libdir/python%__python_version/site-packages/%oname/*.txt ./
fi
popd

%files
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.3-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt2.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.2.3-alt1.1
- Rebuilt with python-2.5.

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- initial build for ALT Linux Sisyphus
