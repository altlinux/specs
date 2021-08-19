
Summary: ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI
Name: python3-module-asgiref
Version: 3.4.1
Release: alt1
Url: https://github.com/django/asgiref/
Source: %name-%version.tar
License: BSD
Group: Development/Python3
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
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
* Wed Aug 18 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- Initial build.

