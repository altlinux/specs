%define pypi_name oracledb

# Tests require an Oracle database to connect to.
%def_without check

Name:    python3-module-%pypi_name
Version: 4.0.0
Release: alt1

Summary: Python driver for Oracle Database conforming to the Python DB API 2.0 specification
License: Apache-2.0 or UPL-1.0
Group:   Development/Python3
URL:     https://github.com/oracle/python-oracledb
VCS:     https://oracle.github.io/python-oracledb/
# Download latest version from https://pypi.org/project/oracledb/

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-Cython

# Optional dependencies
%add_python3_req_skip azure.appconfiguration
%add_python3_req_skip oci

Source: %pypi_name-%version.tar

%description
Python-oracledb is a Python programming language extension module allowing
Python programs to connect to Oracle Database. It is the renamed, new major
release of the popular cx_Oracle driver.
The module conforms to the Python Database API 2.0 specification with a
considerable number of additions and a couple of minor exclusions, see the
feature list.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md LICENSE.txt
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri May 08 2026 Alexander Burmatov <thatman@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus.
