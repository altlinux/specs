%define _unpackaged_files_terminate_build 1
%define pypi_name pathspec

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1
Summary: Utility library for gitignore style pattern matching of file paths
License: MPL-2.0-no-copyleft-exception
Group: Development/Python
Url: https://github.com/cpburnz/python-path-specification

BuildArch: noarch

Source: %name-%version.tar

BuildRequires: rpm-build-python3

%if_with check
BuildRequires: python3(tox)
%endif

%description
%pypi_name is a utility library for pattern matching of file paths. So
far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its
gitignore files.

%prep
%setup

%build
%python3_build

%install
%python3_install
# don't package tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m unittest discover -vv pathspec/tests {posargs}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/
%doc *.rst

%changelog
* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.1 -> 0.9.0.

* Tue May 11 2021 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.5.9 -> 0.8.0.

* Wed Sep 25 2019 Terechkov Evgenii <evg@altlinux.org> 0.5.9-alt1
- Initial build for ALT Linux Sisyphus
