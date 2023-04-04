%define mname greplin
%define oname scales

%def_with check

Name: python3-module-%oname
Version: 1.0.9
Release: alt1

Summary: Stats for Python processes
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/scales/
Vcs: https://github.com/Cue/scales.git

Source: %name-%version.tar
Patch: clean_testsuit.patch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

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
%patch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

sed -i 's|cgi|html|' $(find ./ -name 'formats.py')

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
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

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
* Tue Apr 04 2023 Anton Vyatkin <toni@altlinux.org> 1.0.9-alt1
- New version 1.0.9.

* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.8-alt3
- compatibility with python 3.8

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

