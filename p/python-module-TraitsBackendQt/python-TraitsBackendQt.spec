Name:           python-module-TraitsBackendQt
Version:        3.6.1
Release:        alt1.svn20110127.1
Summary:        PyQt backend for Traits and TraitsGUI

Group:          Development/Python
# Confirmed from upstream that some files are BSD and most are GPLed
License:        BSD and GPLv2
URL:            http://pypi.python.org/pypi/TraitsBackendQt/%version
# https://svn.enthought.com/svn/enthought/TraitsBackendQt
Source:        TraitsBackendQt-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch:      noarch
BuildRequires:  python-devel, python-module-setuptools

%description
The TraitsBackendQt project contains an implementation of TraitsGUI
using PyQt. It provides Qt-based support for visualization and editing
of Traits-based objects.

%prep
%setup -n TraitsBackendQt-%version
sed -i 's/\r//' image_LICENSE.txt
rm -rf TraitsBackendQt.egg-info

%build
python%_python_version setup.py release build

%install
%python_install
#sed -i 's/\.dev$//g' \
#	%buildroot/%python_sitelibdir/TraitsBackendQt-%version-*.egg-info/requires.txt

%files
%doc *.txt docs/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.svn20110127
- Version 3.6.1

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101016
- Version 3.5.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20100723
- Version 3.4.1

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090915.2
- Rebuilt with new NumPy

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090915.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090915
- Version 3.2.1

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Updated

* Tue Mar 17 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.3-4
- Egg-info directory deleted

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.3-3
- Fix BuildRequires

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.3-2
- Fixed the license and confimed by upstream

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.3-1
- Initial package
