%define oname strippers.mixi

Name: python3-module-%oname
Version: 1.0
Release: alt2

Summary: Python library for mixi Graph API
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/strippers.mixi/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires strippers


%description
Python library for mixi Graph API.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
export LC_ALL=en_US.UTF-8

%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test

%files
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/strippers/mixi


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

