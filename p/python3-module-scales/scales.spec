%define mname greplin
%define oname scales

Name: python3-module-%oname
Version: 1.0.8
Release: alt2

Summary: Stats for Python processes
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/scales/
# https://github.com/Cue/scales.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six python3-module-nose

%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires six


%description
Tracks server state and statistics, allowing you to see what your server
is doing. It can also send metrics to Graphite for graphing or to a file
for crash forensics.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Tracks server state and statistics, allowing you to see what your server
is doing. It can also send metrics to Graphite for graphing or to a file
for crash forensics.

This package contains tests for %oname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

%check
python3 setup.py test

%files
%doc AUTHORS *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.8-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.8-alt1.git20150203.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt1.git20150203.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt1.git20150203.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20150203
- Initial build for Sisyphus

