# TODO: fix getDaboLocaleDir()
%define module dabo

Name: python-module-dabo
Version: 0.9.13
Release: alt1

Summary: true 3-tier desktop application framework

License: BSD like
Url: http://dabodev.com/
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://dabodev.com/dabo/%module-%version.tar.bz2
Patch: %name-locale.patch

BuildArch: noarch

# manually removed: python-module-Rabbyt 
# Automatically added by buildreq on Mon Dec 31 2007
BuildRequires: libuuid python-module-MySQLdb python-module-PyXML python-module-Pyrex python-module-ctypes python-module-pysqlite2 python-module-setuptools

BuildPreReq: python-modules-json

%description
Dabo is a Python module that provides a true 3-tier desktop application
framework. It separates the three main parts of a desktop app: database
access, user interface and business logic. You would typically use Dabo
to develop graphical, data-aware desktop applications.

%prep
%setup -n %module
#patch

%build
%python_build

%install
mkdir -p %buildroot%_datadir/
%python_install

mv %buildroot%_prefix/dabo/locale %buildroot%_datadir
%find_lang %module

%files -f %module.lang
%doc AUTHORS ChangeLog README.md RELEASENOTES.md dabo/LICENSE.TXT
%doc demo
%python_sitelibdir/*


%changelog
* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.13-alt1
- Version 0.9.13

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt2
- Rebuilt with python 2.6

* Thu Jul 31 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)
- disable locale hack

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- initial build for ALT Linux Sisyphus

