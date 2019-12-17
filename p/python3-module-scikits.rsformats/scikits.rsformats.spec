%define mname scikits
%define oname %mname.rsformats

Name: python3-module-%oname
Epoch: 1
Version: 0.1
Release: alt3

Summary: Tools for reading remote sensing formats
License: BSD
Group: Development/Python3
Url: http://scikits.scipy.org/

# from git://git.altlinux.org/people/real/packages/scikits.git
# which from http://svn.scipy.org/svn/scikits/trunk (don't work now)
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyparsing libnumpy-py3-devel
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires %mname pyparsing numpy


%description
This package provides tools for reading remote sensing formats.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test

%files
%doc scikits/rsformats/examples
%python3_sitelibdir/%mname/rsformats
%python3_sitelibdir/*.egg-info


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:0.1-alt3
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.1-alt2.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1-alt2
- Rebuilt with updated NumPy

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1-alt1
- Initial build for Sisyphus

