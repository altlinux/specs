%define origname libgmail
Name:           python-module-%origname
Version:        0.1.9
Release:        alt1.1.1
Summary:        Library to provide access to Gmail via Python 
Group:          Development/Python
License:        GPLv2
Packager:	Mikhail Pokidko <pma@altlinux.org>
URL:            http://%origname.sourceforge.net 
Source0:        %origname-%version.tar.gz 
BuildArch:      noarch 
# Automatically added by buildreq on Wed May 14 2008
BuildRequires: python-devel python-module-ClientCookie python-modules-logging 
Requires: python-module-ClientCookie

%description
Library to provide access to Gmail via Python.

%prep
%setup -q -n %origname-%version

%build
%__python setup.py build

%install
%__python setup.py install --skip-build --root %buildroot --optimize=2 --record=INSTALLED_FILES
#chmod 755 %buildroot/%python_sitelibdir/libgmail.py
 
%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.9-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.1
- Rebuilt with python 2.6

* Wed May 14 2008 Mikhail Pokidko <pma@altlinux.org> 0.1.9-alt1
- Initial ALT  build

