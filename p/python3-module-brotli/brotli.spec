%define _unpackaged_files_terminate_build 1
%define pypi_name brotli
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1
Summary: Brotli compression format
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/brotli/
Vcs: https://github.com/google/brotli
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
Provides: python3-module-brotlipy = %EVR
Obsoletes: python3-module-brotlipy < %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with
a compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with deflate
but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in RFC 7932.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# see .github/workflows/build_test.yml and setup.py
%pyproject_run_unittest discover -v -p '*_test.py' -s python/

%files
%doc README.*
%python3_sitelibdir/_%mod_name.*.so
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Dec 09 2025 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- NMU: fixed FTBFS (tox 4).

* Sat Oct 21 2023 Andrey Limachko <liannnix@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
