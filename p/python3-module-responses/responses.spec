%define _unpackaged_files_terminate_build 1
%define pypi_name responses

%def_with check

Name: python3-module-%pypi_name
Version: 0.21.0
Release: alt1

Summary: A utility library for mocking out the requests Python library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/responses/
VCS: https://github.com/getsentry/responses.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# deps
BuildRequires: python3(requests)

BuildRequires: python3(pytest)
BuildRequires: python3(pytest-asyncio)
BuildRequires: python3(pytest-localserver)
%endif

%description
A utility library for mocking out the `requests` Python library.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

rm -r %buildroot%python3_sitelibdir/responses/tests/

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/responses/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1
- 0.12.0 -> 0.21.0.

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version (0.12.0) with rpmgs script

* Wed Feb 12 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.9-alt1
- new version 0.10.9 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 0.3.0-alt3
- Rebuild with changed site-packages in sisyphus

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 0.3.0-alt2
- Rebuild into sisyphus

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

