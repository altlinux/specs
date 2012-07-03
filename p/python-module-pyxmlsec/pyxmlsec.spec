Name:		python-module-pyxmlsec
Version:	0.3.0
Release:	alt1
%setup_python_module pyxmlsec
License:	GPLv2	
Group:		Development/Python
Summary:	Python bindings for the XML Security library (XMLSec)
Source:		pyxmlsec-%version.tar.gz
URL:		http://pyxmlsec.labs.libre-entreprise.org/

# Automatically added by buildreq on Fri Jun 08 2012
# optimized out: alternatives libgnutls-devel libltdl7-devel libnspr-devel libnss-devel libssl-devel libxml2-devel libxmlsec1-devel libxmlsec1-gcrypt libxmlsec1-gcrypt-devel libxmlsec1-gnutls libxmlsec1-nss libxmlsec1-openssl libxslt-devel pkg-config python-base python-modules python-modules-compiler python-modules-email
BuildRequires: libxmlsec1-gnutls-devel libxmlsec1-nss-devel libxmlsec1-openssl-devel python-devel

%py_provides xmlsecmod

%description
PyXMLSec is a set of Python bindings for the XML Security library (XMLSec).

In 2003, the development of Glasnost is supported by the French
Department of Economy, Finance and Industry, as part of the UCIP
- Collective Use of Internet by SMEs - programme.

%prep
%setup -n pyxmlsec-%version
mkdir -p alternatives
echo "%python_sitelibdir/xmlsecmod.so	%python_sitelibdir/xmlsecmod-openssl.so	50" > alternatives/xmlsecmod-openssl
echo "%python_sitelibdir/xmlsecmod.so	%python_sitelibdir/xmlsecmod-gcrypt.so	10" > alternatives/xmlsecmod-gcrypt
echo "%python_sitelibdir/xmlsecmod.so	%python_sitelibdir/xmlsecmod-nspr4.so	10" > alternatives/xmlsecmod-nspr4

%build
echo 3 | { %python_build; }
mv build/lib.linux-`arch`-%_python_version/xmlsecmod{,-nspr4}.so

echo 2 | { %python_build; }
mv build/lib.linux-`arch`-%_python_version/xmlsecmod{,-gcrypt}.so

echo 1 | { %python_build; }
cp -p build/lib.linux-`arch`-%_python_version/xmlsecmod{,-openssl}.so

%install
%python_install
mkdir -p %buildroot%_altdir
install alternatives/* %buildroot%_altdir/
rm %buildroot%python_sitelibdir/xmlsecmod.so

%files
%doc docs/* examples AUTHORS ChangeLog PKG-INFO README TODO

%python_sitelibdir/*
%_altdir/*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial bulid from scratch

