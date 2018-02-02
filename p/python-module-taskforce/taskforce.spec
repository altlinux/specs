%define oname taskforce

%def_with python3

Name: python-module-%oname
Version: 0.1.14
Release: alt1.git20141129.1.1
Summary: Starts and restarts daemon processes
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/taskforce/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/akfullfo/taskforce.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-yaml python-module-inotifyx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-yaml python-tools-2to3
%endif

%py_provides %oname
%py_requires yaml inotifyx

%description
Taskforce starts and restarts daemon processes. It will detect
executable and/or module changes and automatically restart the affected
processes. Initially this supports python 2.7 on Unix derivatives.

%package -n python3-module-%oname
Summary: Starts and restarts daemon processes
Group: Development/Python3
%py3_provides %oname
%py3_requires yaml

%description -n python3-module-%oname
Taskforce starts and restarts daemon processes. It will detect
executable and/or module changes and automatically restart the affected
processes. Initially this supports python 2.7 on Unix derivatives.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	../python3/bin/%oname
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README* examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README* examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.14-alt1.git20141129.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.14-alt1.git20141129.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.14-alt1.git20141129
- Version 0.1.14

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1.git20141120
- Version 0.1.12

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt1.git20141112
- Version 0.1.11

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt1.git20141112
- Initial build for Sisyphus

