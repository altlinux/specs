%define _unpackaged_files_terminate_build 1
%define pypi_name ghp-import

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: Copy your docs directly to the gh-pages branch
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/ghp-import

# https://github.com/davisp/ghp-import.git
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires:
BuildRequires: python3(dateutil)
%endif

Provides: ghp-import.py3 = %EVR
Obsoletes: ghp-import.py3 < 0.5.5

# file conflict: /usr/bin/ghp-import
Conflicts: ghp-import

# PyPI name(dash, underscore)
%py3_provides %pypi_name

Requires: git

%description
As part of gunicorn, Benoit Chesneau and I have been starting to look at
how to host documentation. There's the obvious method of using GitHub's
post-receive hook to trigger doc builds and rsync to a webserver, but we
ended up wanting to try out github's hosting to make the whole interface
a bit more robust.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# upstream doesn't provide tests, at least, install it and run `--help`
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    {envbindir}/ghp-import --help
EOF
%tox_check_pyproject

%files
%doc LICENSE README.md
%_bindir/ghp-import
%python3_sitelibdir/ghp_import.py
%python3_sitelibdir/__pycache__/ghp_import.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 17 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.1 -> 2.1.0.

* Mon Jul 19 2021 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 0.5.4 -> 2.0.1 (closes: #40448).
- Stopped build for Python2(EOL).

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20141001.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141001
- Initial build for Sisyphus

