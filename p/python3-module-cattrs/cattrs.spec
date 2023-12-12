%define oname cattrs

%def_with check

Name:    python3-module-%oname
Version: 23.2.3
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
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/cattr
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Tue Dec 12 2023 Grigory Ustinov <grenka@altlinux.org> 23.2.3-alt1
- Automatically updated to 23.2.3.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 23.1.2-alt2
- Fixed FTBFS.

* Thu Jul 27 2023 Grigory Ustinov <grenka@altlinux.org> 23.1.2-alt1
- Automatically updated to 23.1.2.
- Build with check.

* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 22.2.0-alt1
- Initial build for Sisyphus.
