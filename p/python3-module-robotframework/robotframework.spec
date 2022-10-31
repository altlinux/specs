%define _unpackaged_files_terminate_build 1
%define oname robotframework

%def_with check

Name: python3-module-%oname
Version: 6.0
Release: alt1
Summary: A generic test automation framework
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/robotframework/

# https://github.com/robotframework/robotframework.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(jsonschema)

BuildRequires: python3(tox)
%endif

%py3_provides %oname

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

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
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    # unit tests
    python utest/run.py -v
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr --develop

%files
%doc *.txt *.rst
%_bindir/libdoc
%_bindir/rebot
%_bindir/robot
%python3_sitelibdir/robot/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
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

