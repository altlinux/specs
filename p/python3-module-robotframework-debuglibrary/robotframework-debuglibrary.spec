%define _unpackaged_files_terminate_build 1
%define oname robotframework-debuglibrary

%def_with check

Name: python3-module-%oname
Version: 2.2.2
Release: alt1

Summary: RobotFramework debug library and an interactive shell
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/robotframework-debuglibrary/

BuildArch: noarch

# https://github.com/xyb/robotframework-debuglibrary.git
Source: %name-%version.tar

Patch1: %oname-2.2.2-tests-Drop-dependency-on-coverage.patch
Patch2: %oname-2.2.2-fail-Fixed-expected-attr-name-for-robotframework-5.0.patch
Patch3: %oname-2.2.2-tests-Make-selenium-tests-conditional.patch
Patch4: %oname-2.2.2-tests-Mark-step_functional_testing-as-xfail.patch
Patch5: %oname-2.2.2-deps-Unpin-upper-version-of-prompt-toolkit.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
# install_requires=
BuildRequires: python3(prompt_toolkit)
BuildRequires: python3(robotframework)

BuildRequires: python3(coverage)
BuildRequires: python3(pexpect)
BuildRequires: python3(tox)
%endif

%description
Robotframework-DebugLibrary is A debug library for RobotFramework, which
can be used as an interactive shell(REPL) also.

%prep
%setup
%autopatch1 -p1

sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m unittest -v tests/test_debuglibrary.py
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr --develop

%files
%doc LICENSE
%doc ChangeLog *.rst
%_bindir/*
%python3_sitelibdir/DebugLibrary
%python3_sitelibdir/robotframework_debuglibrary-%version-py*.egg-info

%changelog
* Thu Mar 31 2022 Stanislav Levin <slev@altlinux.org> 2.2.2-alt1
- 2.2.1 -> 2.2.2.

* Tue Sep 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.git20130806.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.git20130806
- Added module for Python 3

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20130806
- Initial build for Sisyphus

