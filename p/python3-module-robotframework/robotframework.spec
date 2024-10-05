%define oname robotframework

%def_with check

Name: python3-module-%oname
Version: 7.1
Release: alt1

Summary: A generic test automation framework

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/robotframework
VCS: https://github.com/robotframework/robotframework

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(jsonschema)

BuildRequires: python3(tox)
%endif

%py3_provides %oname

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

BuildArch: noarch

%description
Robot Framework is a generic test automation framework for acceptance
testing and acceptance test-driven development (ATDD). It has
easy-to-use tabular test data syntax and it utilizes the keyword-driven
testing approach. Its testing capabilities can be extended by test
libraries implemented either with Python or Java, and users can create
new higher-level keywords from existing ones using the same syntax that
is used for creating test cases.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    # unit tests
    python utest/run.py -v
EOF
%tox_check_pyproject

%files
%doc *.txt *.rst
%_bindir/libdoc
%_bindir/rebot
%_bindir/robot
%python3_sitelibdir/robot/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Sat Oct 05 2024 Grigory Ustinov <grenka@altlinux.org> 7.1-alt1
- Automatically updated to 7.1.

* Wed Apr 03 2024 Grigory Ustinov <grenka@altlinux.org> 7.0-alt1
- Automatically updated to 7.0.

* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 6.0.2-alt2
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 6.0.2-alt1
- Automatically updated to 6.0.2.

* Fri Nov 04 2022 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt1
- Automatically updated to 6.0.1.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 6.0-alt1
- Automatically updated to 6.0.

* Thu Mar 31 2022 Stanislav Levin <slev@altlinux.org> 5.0-alt1
- 3.0.2 -> 5.0.

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.2-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2-alt1
- Updated to upstream version 3.0.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev20150202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.9-alt1.dev20150202.1
- NMU: Use buildreq for BR.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1.dev20150202
- Version 2.9.dev20150202
- Added module for Python 3

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.7-alt1.dev20141007
- Initial build for Sisyphus

