Name:           python-module-gdata
Version:        2.0.10
Release:        alt1.svn.987.1
Summary:        A Python module for accessing online Google services
Group:          Development/Python
License:        Apache-2.0
URL:            http://code.google.com/p/gdata-python-client/
Source0:	%name-%version-%release.tar
Packager:	Mikhail A Pokidko <pma@altlinux.org>

BuildArch:      noarch
BuildRequires:  python-devel

%description
This is a Python module for accessing online Google services, such as:
- Blogger
- Calendar
- Picasa Web Albums
- Spreadsheets
- YouTube
- Notebook
and other

%prep
%setup -q

%build
%__python setup.py build
chmod -x samples/*/*.py
rm -rf src/gdata/Crypto/test.py
rm -rf src/gdata/Crypto/Util/test.py

%install
%__python setup.py install -O2 --skip-build --root %buildroot --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.10-alt1.svn.987.1
- Rebuild with Python-2.7

* Sat Jun 19 2010 Mikhail Pokidko <pma@altlinux.org> 2.0.10-alt1.svn.987
- 2.0.10. Closes: #20657

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.1
- Rebuilt with python 2.6

* Thu Jul 02 2009 Mikhail Pokidko <pma@altlinux.org> 2.0.0-alt1
- version up. closes: #20657

* Thu Aug 14 2008 Mikhail Pokidko <pma@altlinux.org> 1.1.1-alt1
- Version up

* Wed May 14 2008 Mikhail Pokidko <pma@altlinux.org> 1.0.13-alt1
- Initial ALT build

