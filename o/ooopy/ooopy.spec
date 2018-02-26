Name: ooopy
Version: 1.4.4873
Release: alt1.1.1

Summary: OOoPy: Modify OpenOffice.org documents in Python

License: GPL
Group: Text tools
Url: http://ooopy.sourceforge.net/

BuildArch: noarch
Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %name

Source: http://prdownloads.sf.net/ooopy/OOoPy-%version.tar.bz2

# Automatically added by buildreq on Sat Jul 05 2008
BuildRequires: python-devel

BuildPreReq: rpm-build-compat >= 1.2

%description
OpenOffice.org (OOo) documents are ZIP archives containing several XML
files.  Therefore it is easy to inspect, create, or modify OOo
documents. OOoPy is a library in Python for these tasks with OOo
documents. To not reinvent the wheel, OOoPy uses an existing XML
library, ElementTree_ by Fredrik Lundh. OOoPy is a thin wrapper around
ElementTree_ using Python's ZipFile to read and write OOo documents.

%prep
%setup -q -n OOoPy-%version

%build
%python_build

%install
%python_install
mkdir -p %buildroot%_bindir
cat >%buildroot%_bindir/%name <<EOF
#!/bin/sh
%_bindir/env python %python_sitelibdir/%modulename/OOoPy.py
EOF

%files
%doc README*
%_bindir/*
%python_sitelibdir/%modulename/
%_datadir/%name/

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.4873-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4873-alt1.1
- Rebuilt with python 2.6

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.4873-alt1
- new version 1.4.4873
- update buildreq, cleanup spec, add rpm-build-compat requires

* Tue Nov 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- first build for ALT Linux Sisyphus

