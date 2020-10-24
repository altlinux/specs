# TODO: check for release

%define oname pyannotate

%def_without check

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: Auto-generate PEP-484 annotations

License: MIT
Group: Development/Python3
Url: https://github.com/dropbox/pyannotate

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

# epm restore --dry-run
%py3_use mypy_extensions >= 0.3.0
%py3_use pytest >= 3.3.0
%py3_use setuptools >= 28.8.0
%py3_use six >= 1.11.0

%description
PyAnnotate: Auto-generate PEP-484 annotations
Insert annotations into your source code based on
call arguments and return types observed at runtime.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%if_with check
%python3_check
%endif

%files
%doc README.md
%_bindir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/pyannotate_tools/
%python3_sitelibdir/pyannotate_runtime/

%changelog
* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Sisyphus
