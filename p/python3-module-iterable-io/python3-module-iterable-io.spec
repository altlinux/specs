%define pypi_name iterable_io
%define mod_name iterableio

Name: python3-module-iterable-io
Version: 1.0.4
Release: alt1

Summary: Adapt generators and other iterables to a file-like interface

License: LGPL-3.0-only
Group: Development/Python3
URL: https://github.com/pR0Ps/iterable-io

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-pytest

%description
iterable-io is a small Python library that provides an adapter so that
it's possible to read from iterable objects in the same way as file-like
objects (open_iterable() works like the builtin open(), but takes
an iterable instead of a file).

It is useful as glue between an interface that expects a file-like object
to call .read() on and another one that only provides a generator of bytes,
without writing the data to a temporary file.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v tests

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for Sisyphus

