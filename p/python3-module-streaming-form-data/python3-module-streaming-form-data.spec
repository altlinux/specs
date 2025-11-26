%define pypi_name streaming-form-data
Name:    python3-module-%pypi_name
Version: 1.19.1
Release: alt1
Summary: Streaming multipart/form-data parser
License: MIT
URL:     https://streaming-form-data.readthedocs.io/en/stable/
VCS:     https://github.com/siddhantgoel/streaming-form-data
Source:  %name-%version.tar
Group:   Development/Python3

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-smart-open
BuildRequires: python3-module-moto

%description
streaming_form_data provides a Python parser
for parsing multipart/form-datainput chunks
(the encoding used when submitting data over HTTP through HTML forms).

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -q --disable-warnings --maxfail=1 tests

%files
%doc README* LICENSE*
%python3_sitelibdir/streaming_form_data
%python3_sitelibdir/streaming_form_data-%version.dist-info

%changelog
* Thu Oct 30 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 1.19.1-alt1
- Initial build.
