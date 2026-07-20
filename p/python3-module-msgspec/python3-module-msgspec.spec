%define pypi_name msgspec

%def_with check

Name:    python3-module-%pypi_name
Version: 0.21.1
Release: alt1

Summary: A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/jcrist/msgspec

BuildRequires(pre): rpm-build-python3
BuildRequires: git-core python3-module-setuptools python3-module-setuptools_scm python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mypy
%endif

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export CFLAGS="%optflags"
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v \
  --ignore="tests/typing/test_pyright.py" \
%ifarch i586
  --deselect="tests/unit/test_common.py::TestIntEnum::test_hashtable[values1]" \
  --deselect="tests/unit/test_msgpack.py::TestDecoderMisc::test_decoding_large_arrays_doesnt_preallocate[None]" \
  --deselect="tests/unit/test_msgpack.py::TestDecoderMisc::test_decoding_large_arrays_doesnt_preallocate[list]" \
  --deselect="tests/unit/test_msgpack.py::TestDecoderMisc::test_decoding_large_arrays_doesnt_preallocate[tuple]" \
  --deselect="tests/unit/test_msgpack.py::TestDecoderMisc::test_decoding_large_arrays_doesnt_preallocate[set]" \
  --deselect="tests/unit/test_msgpack.py::TestDecoderMisc::test_decoding_large_arrays_as_keys_doesnt_preallocate" \
  --deselect="tests/unit/test_msgpack.py::TestTimestampExt::test_timestamp32_upper" \
  --deselect="tests/unit/test_msgpack.py::TestTimestampExt::test_timestamp64_upper" \
  --deselect="tests/unit/test_msgpack.py::TestTimestampExt::test_timestamp96_upper" \
%endif

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 02 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.21.1-alt1
- 0.18.6 -> 0.21.1.

* Mon Jul 28 2025 Grigory Ustinov <grenka@altlinux.org> 0.18.6-alt2
- Fixed build with python3.13.

* Wed Jul 17 2024 Alexander Burmatov <thatman@altlinux.org> 0.18.6-alt1
- Initial build for Sisyphus. (thx toni@)
