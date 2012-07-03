%define version 0.4pseudo_really0.2
%define release alt5.1

Packager: Denis Medvedev <nbr@altlinux.ru>
Summary: A Python/Twisted library for working with messages in many different formats and protocols
Name: python-module-yarn
Version: %version
Release: %release.1
Source: python-module-yarn.tar.bz2
License: GPL
Group: Development/Python
Url: http://yarnproject.org

BuildPreReq: python python-module-twisted python-devel python-module-setuptools
Requires: python python-module-twisted
BuildArch: noarch
%description
A Python/Twisted library for working with messages in many different formats and protocols, such as RSS and mail messages.



%prep
%setup -n python-module-yarn

%build
mkdir -p buildroot

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
CFLAGS="%optflags" %__python setup.py \
        install --optimize=2 \
                --root=`pwd`/buildroot \
                --record=INSTALLED_FILES
               
%install
mkdir %buildroot/
cp -pr buildroot/* %buildroot/
unset RPM_PYTHON

%files -f INSTALLED_FILES


%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4pseudo_really0.2-alt5.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4pseudo_really0.2-alt5.1
- Rebuilt with python 2.6

* Wed Apr 15 2009 Denis Medvedev <nbr@altlinux.ru> 0.4pseudo_really0.2-alt5
- Noarch now

* Sun Apr 12 2009 Denis Medvedev <nbr@altlinux.ru> 0.4pseudo_really0.2-alt4
- Module name change

* Sun Nov 18 2007 Denis Medvedev <nbr@altlinux.ru> 0.4pseudo_really0.2-alt3
- Changed dependence to python-module-twisted

* Fri Nov 16 2007 Denis Medvedev <nbr@altlinux.ru> 0.4pseudo_really0.2-alt2
 - semi-fixed unicode decode problem

* Thu Nov 15 2007 Denis Medvedev <nbr@altlinux.ru> 0.4pseudo_really0.2-alt1
 - HEP not working with 0.3, need 0.2, created custom pseudo-0.2 version

* Wed Nov 14 2007 Denis Medvedev <nbr@altlinux.ru> 0.3_pre1-alt1
 - Initial ALT release

