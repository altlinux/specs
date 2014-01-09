Name: python-module-simpletal
Version: 4.3
Release: alt1
Summary: SimpleTAL is an independent implementation of TAL
License: BSD-like
Group: Development/Python
Url: http://www.owlfish.com/software/simpleTAL/
Packager: Gennady Kovalev <gik@altlinux.ru>
Source0: SimpleTAL-%version.tar
BuildRequires: python-module-setuptools
BuildArch: noarch


%description
SimpleTAL is a stand alone Python implementation
of the TAL, TALES and METAL specifications used in Zope.


%prep
%setup -n SimpleTAL-%version


%build
CFLAGS="%optflags" python setup.py install --optimize=2 --root=buildroot --record=INSTALLED_FILES


%install
mkdir -p %buildroot
cp -r buildroot/* %buildroot


%files -f INSTALLED_FILES


%changelog
* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt1
- Version 4.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1-alt2.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt2
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 4.1-alt1.1
- Rebuilt with python-2.5.

* Sun Dec 09 2007 Gennady Kovalev <gik@altlinux.ru> 4.1-alt1
Initial build

