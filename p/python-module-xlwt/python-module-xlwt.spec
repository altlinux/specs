Name: python-module-xlwt
Version: 1.0.0
Release: alt1

Summary: Library to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.

License: BSD-style
Group: Development/Python
Url: http://pypi.python.org/pypi/xlwt
BuildArch: noarch

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

Buildrequires: python-dev >= 2.4
Buildrequires: python-module-setuptools

Requires: python >= 2.4

%description
Provide a library for developers to use to generate spreadsheet
files compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or
packages outside the standard Python distribution.

%prep
%setup -q

%build

%install
python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES

mkdir -p %buildroot%_defaultdocdir/%name/
cp -av README.rst docs examples %buildroot%_defaultdocdir/%name/

%files -f INSTALLED_FILES
%doc %_defaultdocdir/%name/

%changelog
* Thu Jan 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version
- Package all docs and examples

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1
- New version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.1
- Rebuilt with python 2.6

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.7.2-alt1
- new version

* Mon May 04 2009 Alexey Morsov <swi@altlinux.ru> 0.7.1-alt1
- initial build for Sisyphus- 

