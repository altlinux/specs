%define oname fixedpoint

Name: python3-module-fixedpoint
Version: 0.1.2
Release: alt3

Summary: A fixed point arithmatic class for python
License: Distributable
Group: Development/Python3
Url: http://fixedpoint.sourceforge.net/

Source: http://download.sourceforge.net/sourceforge/%oname/%oname.%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
FixedPoint is a python module to provide a fixed point arithmatic
class. FixedPoint objects support decimal arithmetic with a fixed
number of digits (called the object's precision) after the decimal
point. The number of digits before the decimal point is variable &
unbounded.

%prep
%setup -n %oname

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%__python3 test_%oname.py

%install
mkdir -p %buildroot%python3_sitelibdir
install -m644 %oname.* %buildroot%python3_sitelibdir/

%files
%doc README examples
%python3_sitelibdir/%oname.*
%python3_sitelibdir/__pycache__/*


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt3
- python2 -> python3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2.1.1.qa1
- NMU: applied repocop patch

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.1
- Rebuilt with python 2.6

* Thu Feb 19 2009 Boris Savelev <boris@altlinux.org> 0.1.2-alt2
- place files in %%python_sitelibdir (fix #18906)

* Sun Jan 25 2009 Boris Savelev <boris@altlinux.org> 0.1.2-alt1
- initial build for Sisyphus from RHEL

* Wed Jan  3 2001 Tim Powers <timp@redhat.com>
- fixed bad Requires

* Wed Jul 12 2000 Crutcher Dunnavant <crutcher@redhat.com>
- initial package
