%define _unpackaged_files_terminate_build 1
%define oname crc32c

%def_with check

Name: python3-module-%oname
Version: 2.2
Release: alt1
Summary: Exposes the Intel SSE4.2 CRC32C instruction
License: LGPLv2.1
Group: Development/Python3
Url: https://pypi.org/project/crc32c/

Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
This package exposes to Python the crc32c algorithm implemented in the SSE 4.2
instruction set of Intel CPUs.

%prep
%setup
%patch -p1

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_INDEX=YES
%define py3_nodot py%{python_version_nodots python3}
export TOXENV=%py3_nodot,%py3_nodot-sw
%_bindir/tox.py3 --sitepackages -p auto -o -vr -s false --console-scripts

%files
%doc *.rst
%python3_sitelibdir/crc32c.cpython-*.so
%python3_sitelibdir/crc32c-%version-py%_python3_version.egg-info/

%changelog
* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 2.2-alt1
- 1.7 -> 2.2.
- Stopped build for Python2.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.7-alt2
- Fixed testing against Pytest 5.

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.7-alt1
- Initial build.
