%define _unpackaged_files_terminate_build 1
%define pypi_name brotli
%define old_name brotlipy

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Brotli compression format
License: MIT
Group:   Development/Python3
URL:     https://github.com/google/brotli

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

Provides: python3-module-%old_name = %EVR
Obsoletes: python3-module-%old_name < %EVR

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %pypi_name-%version-alt.patch

%description
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with
a compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with deflate
but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in RFC 7932.

%prep
%setup -n %pypi_name-%version
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Sat Oct 21 2023 Andrey Limachko <liannnix@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
