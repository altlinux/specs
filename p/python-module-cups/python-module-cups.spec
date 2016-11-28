%define oname cups

%def_with python3

Name:          python-module-%oname
Version:       1.9.73
Release:       alt2
%setup_python_module %oname

Group:         Development/Python
Summary:       Python bindings for the CUPS API
Url:           http://cyberelk.net/tim/software/pycups/
License:       %gpl2plus

# git://git.fedorahosted.org/git/pycups.git
Source0:       pycups-%{version}.tar

Packager:      Yury Yurevich <anarresti@altlinux.org>

BuildRequires(pre): rpm-build-licenses libcups-devel
BuildRequires: python-devel python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
Python bindings for the CUPS API. This module allows
use the CUPS API (managing printers, jobs, etc) in Python.

%package -n python3-module-%oname
Summary: Python bindings for the CUPS API
Group: Development/Python3

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
sed -i 's|python|python3|g' ../python3/Makefile
%endif

%build
%make

%if_with python3
pushd ../python3
%make
popd
%endif

%make doc

%install
%makeinstall_std

%if_with python3
pushd ../python3
%makeinstall_std
popd
%endif

%files
%doc NEWS README TODO test.py examples
%python_sitelibdir/*

%files docs
%doc html/*

%if_with python3
%files -n python3-module-%oname
%doc NEWS README TODO test.py examples
%python3_sitelibdir/*
%endif

%changelog
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

