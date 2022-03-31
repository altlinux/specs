%define _unpackaged_files_terminate_build 1
%define oname robotframework-lint

%def_with check

Name: python3-module-%oname
Version: 1.1
Release: alt1

Summary: Static analysis tool for robotframework plain text files
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/robotframework-lint/
BuildArch: noarch

# https://github.com/boakley/robotframework-lint.git
Source: %name-%version.tar
Patch0: robotframework-lint-1.1-tests-Sync-expected-out-for-Python-3.10.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(robotframework)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

# PEP503 normalized name
%py3_provides robotframework-lint

%description
Linter for robot framework plain text files.

This is a static analysis tool for robot framework plain text files.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    robot -A tests/conf/smoke.args
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --develop

%files
%doc *.md
%_bindir/rflint
%python3_sitelibdir/rflint/
%python3_sitelibdir/robotframework_lint-%version-py%_python3_version.egg-info/

%changelog
* Thu Mar 31 2022 Stanislav Levin <slev@altlinux.org> 1.1-alt1
- 0.7 -> 1.1.

* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150205
- Version 0.5

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141222
- Version 0.4

* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141130
- New snapshot

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141125
- Initial build for Sisyphus

