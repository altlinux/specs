%define origname libgmail

Name:           python3-module-%origname
Version:        0.1.11
Release:        alt2

Summary:        Library to provide access to Gmail via Python
License:        GPLv2
Group:          Development/Python3
URL:            http://%origname.sourceforge.net
BuildArch:      noarch

Source0:        %origname-%version.tar.gz
Patch0:         fix-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-mechanize 

Requires: python3-module-mechanize


%description
Library to provide access to Gmail via Python.

%prep
%setup -q -n %origname-%version
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%__python3 setup.py build

%install
%__python3 setup.py install --skip-build --root %buildroot --optimize=2
 
%files
%python3_sitelibdir/*


%changelog
* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.11-alt2
- porting on python3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt1
- Version 0.1.11

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.9-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.1
- Rebuilt with python 2.6

* Wed May 14 2008 Mikhail Pokidko <pma@altlinux.org> 0.1.9-alt1
- Initial ALT  build

