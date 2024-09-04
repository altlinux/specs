%define oname kiwisolver
%def_without check

Name: python3-module-%oname
Version: 1.4.6
Release: alt1
Summary: A fast implementation of the Cassowary constraint solver
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kiwisolver/
# VCS: https://github.com/nucleic/kiwi
Packager: Andrey Cherepanov <cas@altlinux.org>

# https://github.com/nucleic/kiwi.git
Source: kiwi-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: python3-module-cppy
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-build
BuildRequires: python3-module-toml
BuildRequires: python3-module-wheel
BuildRequires: pip

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
Kiwi is an efficient C++ implementation of the Cassowary constraint
solving algorithm. Kiwi is an implementation of the algorithm based on
the seminal Cassowary paper. It is not a refactoring of the original C++
solver. Kiwi has been designed from the ground up to be lightweight and
fast. Kiwi ranges from 10x to 500x faster than the original Cassowary
solver with typical use cases gaining a 40x improvement. Memory savings
are consistently > 5x.

%prep
%setup -n kiwi-%version

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
git init
git config user.email author@example.com
git config user.name author
git add .
git commit -m 'release'
git tag '%version'

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%__python3 -m build -n

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
pip3 install --root=%buildroot --no-deps dist/*.whl

%if_with check
%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    # see .github/workflows/ci.yml for details
    python -X dev -m pytest -vra py
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr --develop
%endif

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Sep 04 2024 Andrey Cherepanov <cas@altlinux.org> 1.4.6-alt1
- New version.

* Fri Aug 25 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.5-alt1
- New version.

* Mon Jul 18 2022 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- New version.
- Disabled checks.
- Built by PEP 517/518.

* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- New version.

* Fri Aug 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- New version.

* Mon Nov 02 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.

* Thu Oct 22 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.

* Fri Mar 27 2020 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Thu Dec 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Add python3-dev to build requirements.

* Tue Nov 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version.
- Package as python3 module.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.git20140712.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20140712
- Initial build for Sisyphus

