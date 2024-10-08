%define _unpackaged_files_terminate_build 1
%define pypi_name cbor2
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.4.6
Release: alt2

Summary: Pure Python CBOR (de)serializer with extensive tag support

License: MIT
Group: Development/Python
Url: https://github.com/agronholm/cbor2

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4
# build backend and its deps
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
%if_with check
BuildRequires: python3-module-pytest
%endif

%description

This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (`RFC 7049`_) serialization format. `Read the docs
<https://cbor2.readthedocs.io/>`_ to learn more.

It is implemented in pure python with an optional C backend and is
compatible with versions 2.7 through to 3.7.

On cPython>=3.3 cbor2 can use a built in C module for performance similar
to how ``pickle`` wraps the ``_pickle`` C module in the Python Standard
Library. On Windows, this is restricted to cPython>=3.5.

On PyPy, cbor2 runs with almost identical performance to the C backend.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%check
%pyproject_run_pytest -vra -o=addopts=''

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_%mod_name.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 5.4.6-alt2
- Migrated from removed setuptools' test command (#51666).

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.6-alt1
- new version 5.4.6 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.3-alt1
- new version 5.4.3 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.2-alt1
- new version 5.4.2 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt1
- new version 5.4.0 (with rpmrb script)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script)

* Fri Apr 10 2020 Eugene Omelyanovich <regatio@etersoft.ru> 5.1.0-alt1
- new version (5.1.0) with rpmgs script

