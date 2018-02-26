Name: loook
Version: 0.6.4
Release: alt0.1.2.1

Summary: Loook searches for text strings in OpenOffice.org files

License: GPL
Group: Text tools
Url: http://www.danielnaber.de/loook/

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %name

Source: http://www.danielnaber.de/loook/%name.zip

# manually removed: eric
# Automatically added by buildreq on Wed Jan 04 2006
BuildRequires: python-base python-modules-encodings unzip

%description
Loook is a simple Python tool that searches for text strings in
OpenOffice.org (and StarOffice 6.0 or later) files. It works under Linux,
Windows and Macintosh. AND, OR and phrase searches are supported. It
doesn't create an index, but searching should be fast enough unless you
have really many files.

%prep
#%%setup -q -n %name
rm -rf %name && mkdir %name && cd %name
unzip %SOURCE0


%install
cd %name
%__install -D %name.py %buildroot%python_sitelibdir/%name.py
%__mkdir_p %buildroot%_bindir
cat >%buildroot%_bindir/%name <<EOF
#!/bin/sh
/usr/bin/env python %python_sitelibdir/%name.py
EOF

%files
%attr (0755, root, root) %_bindir/*
%python_sitelibdir/%name.py

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.4-alt0.1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt0.1.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.6.4-alt0.1.1
- Rebuilt with python-2.5.

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt0.1
- initial build for ALT Linux Sisyphus

