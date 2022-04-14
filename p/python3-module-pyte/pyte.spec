%define oname pyte

%def_with check

Name: python3-module-%oname
Version: 0.8.1
Release: alt1

Summary: Simple VTXXX-compatible terminal emulator

License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyte/

# https://github.com/selectel/pyte.git
Source: %name-%version.tar
BuildArch: noarch

%py3_provides %oname

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-wcwidth
%endif

%description
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc AUTHORS CHANGES README examples
%python3_sitelibdir/*

%changelog
* Thu Apr 14 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Automatically updated to 0.8.1.

* Sun Jun 06 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Build new version.
- build without docs.

* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.4.9-alt2.git20141204
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.9-alt1.git20141204.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.9-alt1.git20141204.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1.git20141204.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20141204
- Initial build for Sisyphus

