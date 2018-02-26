Name: python-module-TraitsBackendWX
Version: 3.6.1
Release: alt1.svn20110127.1
Summary: WxPython backend for Traits and TraitsGUI

Group: Development/Python
License: BSD and GPLv2
URL: http://pypi.python.org/pypi/TraitsBackendWX
# https://svn.enthought.com/svn/enthought/TraitsBackendWX
Source: TraitsBackendWX-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch:      noarch
BuildRequires:  python-devel, python-module-setuptools

%description
The TraitsBackendWX project contains an implementation of TraitsGUI
using wxPython. It provides wx-based support for visualization and
editing of Traits-based objects.

%prep
%setup -n TraitsBackendWX-%version

%build
%python_build

%install
%python_install

#sed -i 's|\.dev$||' \
#	%buildroot%python_sitelibdir/TraitsBackendWX-%version-*.egg-info/requires.txt

%files
%doc *.txt docs/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.svn20110127
- Version 3.6.1

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101102
- Version 3.5.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20100708
- Version 3.4.1

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091002.3
- Rebuilt with new NumPy

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091002.2
- Rebuilt with python 2.6

* Sat Oct 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091002.1
- Enabled default_image_slice

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20091002
- Initial build for Sisyphus

