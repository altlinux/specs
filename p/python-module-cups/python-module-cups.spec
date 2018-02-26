
Name:          python-module-cups
Version:       1.9.55
Release:       alt1.1.1
%setup_python_module cups

Group:         Development/Python
Summary:       Python bindings for the CUPS API
Url:           http://cyberelk.net/tim/software/pycups/
License:       %gpl2plus

Source0:       pycups-%{version}.tar

Packager:      Yury Yurevich <anarresti@altlinux.org>

BuildRequires(pre): rpm-build-licenses libcups-devel
BuildRequires: python-devel

%description
Python bindings for the CUPS API. This module allows
use the CUPS API (managing printers, jobs, etc) in Python.


#--------------------------------------------------------------------

%prep
%setup -n pycups-%version

%build
%make

%install
%make install DESTDIR=%buildroot

%files
%doc NEWS README TODO ChangeLog test.py examples
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.55-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.55-alt1.1
- Rebuild with Python-2.7

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

