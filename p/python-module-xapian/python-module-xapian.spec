%define oname xapian-bindings

Name: python-module-xapian
Version: 1.2.12
Release: alt1

Summary: Xapian search engine interface for Python
License: GPL
Group: Development/Python

Url: http://www.xapian.org/
Source: http://www.oligarchy.co.uk/xapian/%version/%oname-%version.tar
Source100: xapian-bindings.watch
Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

# Automatically added by buildreq on Tue Nov 13 2007
BuildRequires: gcc-c++ python-devel python-modules-compiler

BuildPreReq: libxapian-devel = %version

# force rebuild with libxapian
Requires: libxapian = %version

%description
Xapian is an Open Source Probabilistic Information Retrieval framework.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package provides the files needed for developing Python scripts
which use Xapian.

%prep
%setup -n %oname-%version
# due to missing .la files
sed -i "s|--ltlibs|--libs|g" configure

%build
%configure --with-python
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_docdir/%oname/

%files
%doc python/docs/index.html python/docs/examples
%python_sitelibdir/*

%changelog
* Thu Jun 28 2012 Michael Shigorin <mike@altlinux.org> 1.2.12-alt1
- 1.2.12

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 1.2.10-alt1
- 1.2.10
- added watch file
- minor spec cleanup

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 1.2.9-alt2
- argh, forgotten rebuild

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 1.2.9-alt1
- 1.2.9

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7-alt1.1
- Rebuild with Python-2.7

* Tue Aug 16 2011 Michael Shigorin <mike@altlinux.org> 1.2.7-alt1
- 1.2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.2
- Rebuilt for debuginfo

* Sat Oct 09 2010 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1.1
- simplify dependency invariant

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)

* Wed Jun 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.21-alt1
- new version 1.0.21 (with rpmrb script)

* Tue May 04 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.20-alt1
- new version 1.0.20 (with rpmrb script)

* Mon Apr 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.19-alt1
- new version 1.0.19 (with rpmrb script)

* Mon Apr 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt1
- new version 1.0.18 (with rpmrb script)

* Sat Feb 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt1
- new version 1.0.17 (with rpmrb script) (fix alt bug #22673)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.1
- Rebuilt with python 2.6

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Linux Sisyphus
