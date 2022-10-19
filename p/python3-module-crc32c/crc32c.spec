%define _unpackaged_files_terminate_build 1
%define pypi_name crc32c

%def_with check

Name: python3-module-%pypi_name
Version: 2.3
Release: alt1
Summary: Exposes the Intel SSE4.2 CRC32C instruction
License: LGPLv2.1
Group: Development/Python3
Url: https://pypi.org/project/crc32c/
VCS: https://github.com/ICRAR/crc32c.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
This package exposes to Python the crc32c algorithm implemented in the SSE 4.2
instruction set of Intel CPUs.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -u run-tests.py
EOF
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/crc32c.cpython-*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 2.3-alt1
- 2.2 -> 2.3.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 2.2-alt1
- 1.7 -> 2.2.
- Stopped build for Python2.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.7-alt2
- Fixed testing against Pytest 5.

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.7-alt1
- Initial build.
