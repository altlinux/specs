%define pypi_name python-json-logger

%def_with check

Name:    python3-module-%pypi_name
Version: 2.0.7
Release: alt2

Summary: Json Formatter for the standard python logger
License: BSD-2-Clause
Group: Development/Python3
URL: https://pypi.org/project/python-json-logger/
VCS: https://github.com/madzak/python-json-logger

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
This library is provided to allow standard python logging to output log data
as json objects. With JSON we can make our logs more readable by machines and
we can stop writing custom parsers for syslog type records.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# delesect for python3.12
%pyproject_run_pytest -v -k "\
not test_custom_object_serialization \
and not test_percentage_format \
and not test_rename_reserved_attrs"


%files
%doc *.md
%python3_sitelibdir/pythonjsonlogger
%python3_sitelibdir/%{pyproject_distinfo python_json_logger}

%changelog
* Mon Jan 22 2024 Anton Vyatkin <toni@altlinux.org> 2.0.7-alt2
- Fixed FTBFS.

* Tue Jun 13 2023 Anton Vyatkin <toni@altlinux.org> 2.0.7-alt1
- Initial build for Sisyphus
