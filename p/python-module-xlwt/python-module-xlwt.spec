Name: python-module-xlwt
Version: 0.7.2
Release: alt1.1.1

Summary: Library to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.

License: BSD-style
Group: Development/Python
Url: http://pypi.python.org/pypi/xlwt
BuildArch: noarch

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

Buildrequires: python-dev >= 2.4

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
install -m 644 HISTORY.html  licences.py  README.html %buildroot%_defaultdocdir/%name/

%files -f INSTALLED_FILES
%defattr(-,root,root)
%_defaultdocdir/%name/


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.1
- Rebuilt with python 2.6

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.7.2-alt1
- new version

* Mon May 04 2009 Alexey Morsov <swi@altlinux.ru> 0.7.1-alt1
- initial build for Sisyphus- 

