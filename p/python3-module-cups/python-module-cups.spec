%define oname cups

Name:          python3-module-cups
Version:       1.9.74
Release:       alt3.1

Summary:       Python bindings for the CUPS API

Group:         Development/Python3
Url:           http://cyberelk.net/tim/software/pycups/
License:       %gpl2plus

# git://git.fedorahosted.org/git/pycups.git
Source0:       pycups-%{version}.tar
Patch0:        python-module-cups-1.9.74-alt-extension-copy-document.patch
Patch1:        3df8a811b650c01cca595fff89209087b92f801c.patch

Packager:      Yury Yurevich <anarresti@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): libcups-devel >= 2.2.12-alt2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Python bindings for the CUPS API. This module allows
use the CUPS API (managing printers, jobs, etc) in Python.

%package docs
Summary: Documentation for Python bindings for the CUPS API
Group: Development/Documentation
BuildArch: noarch

%description docs
Python bindings for the CUPS API. This module allows
use the CUPS API (managing printers, jobs, etc) in Python.

This package contains documentation for Python bindings for the CUPS
API.

#--------------------------------------------------------------------

%prep
%setup -n pycups-%version
%patch0 -p1
%patch1 -p1

subst 's|python|python3|g' Makefile
subst 's|build/lib\*/$@|build/lib*/cups*.so|g' Makefile
subst 's|#!.*python$|#!%__python3|' $(grep -Rl 'python$' *)

%build
%make
%make doc

%install
%makeinstall_std

%files
%doc NEWS README TODO test.py examples
%python3_sitelibdir/*

%files docs
%doc html/*


%changelog
* Thu Dec 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.9.74-alt3.1
- NMU: add setuptools to build dependencies

* Fri Aug 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.74-alt3
- build python3 module separately

* Mon Jun 21 2021 Paul Wolneykien <manowar@altlinux.org> 1.9.74-alt2
- Added API to support ALT copy document IPP extension.

* Wed May 13 2020 Pavel Vasenkov <pav@altlinux.org> 1.9.74-alt1
- Version 1.9.74

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.73-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Nov 28 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.9.73-alt2
- release bump for separate build into p8

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.73-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Feb 10 2016 Sergey Alembekov <rt@altlinux.ru> 1.9.73-alt1
- Version 1.9.73

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.67-alt1
- Version 1.9.67
- Added module for Python 3

* Tue Oct 09 2012 Sergey V Turchin <zerg@altlinux.org> 1.9.62-alt1
- new version

* Thu Jul 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.61-alt1
- 1.9.61

* Tue Mar 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.9.55-alt1
- new version
- clean requires

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.49.git20100322-alt1.1
- Rebuilt for debuginfo

* Sun Mar 28 2010 Yury Yurevich <anarresti@altlinux.org> 1.9.49+git20100322-alt1
- Update upstream to 1.9.49+git20100322

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.9.48-alt1.M51.1
- built for M51

* Fri Feb 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.9.48-alt2
- add requires to libcups version

* Thu Feb 18 2010 Sergey V Turchin <zerg@altlinux.org> 1.9.48-alt1
- new version

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.46-alt1.1
- Rebuilt with python 2.6

* Mon Jul 13 2009 Yury Yurevich <anarresti@altlinux.org> 1.9.46-alt1
- update upstream to 1.9.46

* Fri Apr 17 2009 Yury Yurevich <anarresti@altlinux.org> 1.9.45-alt2
- new packager (anarresti@)
- use upstream's git as source
- add examples to %%doc
- use license macros

* Thu Feb 05 2009 Sergey V Turchin <zerg at altlinux dot org> 1.9.45-alt1
- new version

* Thu Nov 20 2008 Sergey V Turchin <zerg at altlinux dot org> 1.9.42-alt1
- initial specfile

