%define pkgname	chardet
%def_with python3


%define python3_dirsetup \
%if_with python3 \
rm -rf ../python3 \
cp -a . ../python3 \
%endif \
%nil

#find ../python3 -name "*.py" | xargs %__subst "s|^#!/usr/bin/env python$|#!/usr/bin/python3|g"

%define python3_dirbuild \
%if_with python3 \
pushd ../python3 \
%python3_build \
popd \
%endif \
%nil

%define python3_dirinstall \
%if_with python3 \
pushd ../python3 \
%python3_install \
popd \
%endif \
%nil

#TODO: python3_dircheck


Name: python-module-chardet
Version: 2.3.0
Release: alt1.1

Summary: Character encoding auto-detection in Python

License: LGPL
Url: https://pypi.python.org/pypi/%pkgname
Group: Development/Python

Packager: Evgenii Terechkov <evg@altlinux.ru>

Source: https://pypi.python.org/packages/source/c/chardet/%pkgname-%version.tar

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools

%description
Character encoding auto-detection in Python.

%if_with python3
%package -n python3-module-%pkgname
Summary: Character encoding auto-detection in Python
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description -n python3-module-%pkgname
Character encoding auto-detection in Python.
%endif


%prep
%setup -n %pkgname-%version

%python3_dirsetup

%build
%python_build
%python3_dirbuild

%install
%python_install
%python3_dirinstall

rm -rf %buildroot%_bindir/

%files
# FIXME: makes checker think it use python3 libs
#_bindir/chardetect
%python_sitelibdir/%pkgname/
%python_sitelibdir/%pkgname-*egg-info/
#doc docs

%if_with python3
%files -n python3-module-%pkgname
%python3_sitelibdir/%pkgname/
%python3_sitelibdir/*.egg-info/
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Sun Apr 13 2014 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)
- build for python3 too

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Mar 22 2010 Terechkov Evgenii <evg@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.3.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.3
- Site-packages removed from packages (Closes #18909)
- Packager tag added

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.2
- Really fix build on x86_64

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.1
- Egg dropped to build on x86_64

* Sun Dec 28 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux Sisyphus (thanks Mandriva for initial spec)
