%define oname fixedpoint
Summary: A fixed point arithmatic class for python
Name: python-module-fixedpoint
Version: 0.1.2
Release: alt2.1.1
License: Distributable
Group: Development/Python
Url: http://fixedpoint.sourceforge.net/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://download.sourceforge.net/sourceforge/%oname/%oname.%version.tar.gz

# Automatically added by buildreq on Sun Jan 25 2009
BuildRequires: python-dev

%description
FixedPoint is a python module to provide a fixed point arithmatic
class. FixedPoint objects support decimal arithmetic with a fixed
number of digits (called the object's precision) after the decimal
point. The number of digits before the decimal point is variable &
unbounded.

%prep
%setup -n %oname

%build
%__python test_%oname.py

%install
mkdir -p %buildroot%python_sitelibdir
install -m644 %oname.* %buildroot%python_sitelibdir/

%files
%doc README examples
%python_sitelibdir/%oname.*

%changelog
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
