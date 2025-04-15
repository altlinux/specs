%define oname cattrs

%def_with check

Name:    python3-module-%oname
Version: 24.1.3
Release: alt1

Summary: Complex custom class converters for attrs.

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/cattrs
VCS:     https://github.com/python-attrs/cattrs

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-immutables
BuildRequires: python3-module-bson
BuildRequires: python3-module-ujson
BuildRequires: python3-module-orjson
BuildRequires: python3-module-cbor2
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-msgspec
%endif

%description
cattrs is an open source Python library for structuring and unstructuring data.
cattrs works best with attrs classes, dataclasses and the usual
Python collections, but other kinds of classes are supported by manually
registering converters.

Python has a rich set of powerful, easy to use, built-in data types
like dictionaries, lists and tuples. These data types are also the lingua franca
of most data serialization libraries, for formats like json, msgpack, cbor, yaml
or toml.

Data types like this, and mappings like dict s in particular, represent
unstructured data. Your data is, in all likelihood, structured:
not all combinations of field names or values are valid inputs to your programs.
In Python, structured data is better represented with classes and enumerations.
attrs is an excellent library for declaratively describing the structure
of your data, and validating it.

When you're handed unstructured data (by your network, file system, database...),
cattrs helps to convert this data into structured data. When you have to convert
your structured data into data types other libraries can handle, cattrs turns
your classes and enumerations into dictionaries, integers and strings.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_build

%install
%pyproject_install

%check
#https://github.com/python-attrs/cattrs/issues/575
%pyproject_run_pytest -k "not test_simple_roundtrip and not \
test_nested_roundtrip and not \
test_optional_field_roundtrip and not \
test_simple_roundtrip_tuple and not \
test_simple_roundtrip_defaults_tuple and not \
test_nested_roundtrip and not \
test_310_union_field_roundtrip and not \
test_optional_field_roundtrip and not \
test_310_optional_field_roundtrip and not \
test_omit_default_roundtrip and not \
test_structure_simple_from_dict_default and not \
test_union_field_roundtrip and not \
test_nodefs_generated_unstructuring_cl and not \
test_unmodified_generated_structuring and not \
test_renaming and not \
test_individual_overrides"

%files
%doc LICENSE *.md
%python3_sitelibdir/cattr
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Apr 14 2025 Grigory Ustinov <grenka@altlinux.org> 24.1.3-alt1
- Automatically updated to 24.1.3.

* Mon Jan 06 2025 Grigory Ustinov <grenka@altlinux.org> 24.1.2.0.7.git31eff82-alt1
- Build from snapshot.

* Tue Dec 12 2023 Grigory Ustinov <grenka@altlinux.org> 23.2.3-alt1
- Automatically updated to 23.2.3.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 23.1.2-alt2
- Fixed FTBFS.

* Thu Jul 27 2023 Grigory Ustinov <grenka@altlinux.org> 23.1.2-alt1
- Automatically updated to 23.1.2.
- Build with check.

* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 22.2.0-alt1
- Initial build for Sisyphus.
