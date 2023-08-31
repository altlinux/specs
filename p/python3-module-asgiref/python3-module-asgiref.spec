
Summary: ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI
Name: python3-module-asgiref
Version: 3.7.2
Release: alt1
Url: https://github.com/django/asgiref/
Source: %name-%version.tar
License: BSD-3-Clause
Group: Development/Python3
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
# For python_version < "3.11"
# BuildRequires: python3(typing_extensions) >= 4
# For check
BuildRequires: pytest3 python3-module-pytest-asyncio

%description
ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI,
intended to provide a standard interface between async-capable
Python web servers, frameworks, and applications.

Where WSGI provided a standard for synchronous Python apps,
ASGI provides one for both asynchronous and synchronous apps,
with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.

%prep
%setup -q

%build
%python3_build

%install
%python3_install

%check
python3 -m pytest -v

%files
%python3_sitelibdir/*
%doc README.rst CHANGELOG.txt

%changelog
* Thu Aug 31 2023 Alexey Shabalin <shaba@altlinux.org> 3.7.2-alt1
- New version 3.7.2.

* Wed Aug 18 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- Initial build.

