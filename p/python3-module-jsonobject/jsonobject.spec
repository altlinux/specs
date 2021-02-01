%define _unpackaged_files_terminate_build 1

%define oname jsonobject

Name: python3-module-%oname
Version: 0.9.9.0.11.git91aa99b
Release: alt1

Summary: A library for dealing with JSON as python objects
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsonobject/
# https://github.com/dimagi/jsonobject.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython
BuildRequires: python3-module-unittest2

%description
A python library for handling deeply nested JSON objects as
well-schema'd python objects.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
%__python3 -m unittest test.test_couchdbkit

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Mon Feb 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.9.0.11.git91aa99b-alt1
- Build from last commit for python3.9 support.

* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.8-alt3
- Build for python2 disabled.

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 0.9.8-alt2
- Dropped BR on argparse.

* Wed Dec 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.8-alt1
- Version updated to 0.9.8

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.git20150130.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150130
- New snapshot

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141126
- Initial build for Sisyphus

