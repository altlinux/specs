%define pypi_name narwhals

Name: python3-module-narwhals
Version: 2.20.0
Release: alt1

Summary: Extremely lightweight compatibility layer between dataframe libraries

License: MIT
Group: Development/Python3
Url: https://github.com/narwhals-dev/narwhals

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

# All these are optional backends imported lazily (TYPE_CHECKING / sys.modules).
# Pull them in only via the corresponding extras, do not force them at runtime.
%add_python3_req_skip cudf dask dask.dataframe modin modin.pandas
%add_python3_req_skip duckdb ibis ibis.expr.datatypes ibis.expr.types
%add_python3_req_skip pandas polars pyarrow pyarrow.compute
%add_python3_req_skip pyspark pyspark.sql pyspark.sql.connect.dataframe
%add_python3_req_skip sqlframe sqlparse fireducks numpy

%description
Narwhals is an extremely lightweight and extensible compatibility layer
between dataframe libraries (pandas, Polars, PyArrow, Modin, cuDF, Dask,
DuckDB, Ibis, PySpark, SQLFrame).

It is used as a backend for libraries that need to support multiple
dataframe APIs without taking on heavy dependencies. Narwhals itself
is pure Python with no required runtime dependencies; specific backends
are pulled in only when actually used.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- initial build for ALT Sisyphus

