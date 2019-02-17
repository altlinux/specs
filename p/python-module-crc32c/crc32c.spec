%define _unpackaged_files_terminate_build 1
%define oname crc32c

%def_with check

Name: python-module-%oname
Version: 1.7
Release: alt1
Summary: Exposes the Intel SSE4.2 CRC32C instruction
License: LGPLv2.1
Group: Development/Python
Url: https://pypi.org/project/crc32c/

Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(tox)
%endif

%description
This package exposes to Python the crc32c algorithm implemented in the SSE 4.2
instruction set of Intel CPUs.

%package -n python3-module-%oname
Summary: Exposes the Intel SSE4.2 CRC32C instruction
Group: Development/Python3

%description -n python3-module-%oname
This package exposes to Python the crc32c algorithm implemented in the SSE 4.2
instruction set of Intel CPUs.

%prep
%setup
%patch -p1

rm -rf ../python3
cp -a . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
export PIP_NO_INDEX=YES
%define py_nodot py%{python_version_nodots python}
%define py3_nodot py%{python_version_nodots python3}
export TOXENV=%py_nodot,%py_nodot-sw,%py3_nodot,%py3_nodot-sw
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst
%python_sitelibdir/crc32c.so
%python_sitelibdir/crc32c-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/crc32c.cpython-*.so
%python3_sitelibdir/crc32c-%version-py%_python3_version.egg-info/

%changelog
* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.7-alt1
- Initial build.
