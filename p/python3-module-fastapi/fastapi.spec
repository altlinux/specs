%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi

%def_with check

Name: python3-module-%pypi_name
Version: 0.87.0
Release: alt1

Summary: FastAPI framework, high performance, easy to learn, fast to code, ready for production
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi

Source: %name-%version.tar
Patch0: fastapi-0.85.0-alt-email_tests.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pydantic)
BuildRequires: python3(starlette) 
BuildRequires: python3(httpx)
BuildRequires: python3(sqlalchemy)
BuildRequires: python3(flask)
BuildRequires: python3(email_validator)
BuildRequires: python3(databases)
# BuildRequires: python3(multipart)
# FastAPI based on Starlette, which requires 'python-multipart' exactly.
# See https://bugzilla.altlinux.org/43483 for more information.
BuildRequires: python3(python-multipart)
BuildRequires: python3(orjson)
BuildRequires: python3(jose)
BuildRequires: python3(passlib)
BuildRequires: python3(peewee)
BuildRequires: python3(ujson)
%endif

BuildArch: noarch

%description
FastAPI is a modern, fast (high-performance), web framework for building APIs
with Python 3.7+ based on standard Python type hints.

The key features are:

    Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette
and Pydantic). One of the fastest Python frameworks available.
    Fast to code: Increase the speed to develop features by about 200%% to
300%%.
    Fewer bugs: Reduce about 40%% of human (developer) induced errors. *
    Intuitive: Great editor support. Completion everywhere. Less time debugging.
    Easy: Designed to be easy to use and learn. Less time reading docs.
    Short: Minimize code duplication. Multiple features from each parameter
declaration. Fewer bugs.
    Robust: Get production-ready code. With automatic interactive documentation.
    Standards-based: Based on (and fully compatible with) the open standards
for APIs: OpenAPI (previously known as Swagger) and JSON Schema.


%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.* CONTRIBUTING.md LICENSE SECURITY.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 0.87.0-alt1
- 0.85.0 -> 0.87.0

* Sat Sep 18 2022 Anton Zhukharev <ancieg@altlinux.org> 0.85.0-alt1
- Initial build for sisyphus (thanks Alexandr Shashkin <dutyrok@altlinux.org>)

