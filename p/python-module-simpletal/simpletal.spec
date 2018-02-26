Name: python-module-simpletal
Version: 4.1
Release: alt2.1
Summary: SimpleTAL is an independent implementation of TAL
License: BSD-like
Group: Development/Python
Url: http://www.owlfish.com/software/simpleTAL/
Packager: Gennady Kovalev <gik@altlinux.ru>
Source0: SimpleTAL-%version.tar
Patch0: SimpleTAL-%version-alt-allinone.patch
BuildRequires: python-module-setuptools
BuildArch: noarch


%description
SimpleTAL is a stand alone Python implementation
of the TAL, TALES and METAL specifications used in Zope.


%prep
%setup -n SimpleTAL-%version
%patch0


%build
CFLAGS="%optflags" python setup.py install --optimize=2 --root=buildroot --record=INSTALLED_FILES


%install
mkdir -p %buildroot
cp -r buildroot/* %buildroot


%files -f INSTALLED_FILES


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1-alt2.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt2
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 4.1-alt1.1
- Rebuilt with python-2.5.

* Sun Dec 09 2007 Gennady Kovalev <gik@altlinux.ru> 4.1-alt1
Initial build

