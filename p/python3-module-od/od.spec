%define _unpackaged_files_terminate_build 1
%define oname od

%def_with check

Name: python3-module-%oname
Version: 2.0.2
Release: alt2

Summary: Shorthand syntax for building OrderedDicts

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/od

# Source-url: https://pypi.io/packages/source/o/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(repeated_test)
BuildRequires: python3(tox)
%endif


%description
Shorthand syntax for building OrderedDicts.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -f %buildroot%python3_sitelibdir/test_od.py

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m unittest -v
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt2
- Moved on modern pyproject macros.

* Tue Mar 29 2022 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.0 -> 2.0.2.

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- add BR:repeated_test and enable test

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
