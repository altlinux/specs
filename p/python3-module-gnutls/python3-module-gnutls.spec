%define  modulename gnutls

Name:    python3-module-%modulename
Version: 3.1.10
Release: alt1

Summary: GnuTLS bindings for Python
License: LGPL-2.1+
Group:   Development/Python3
URL:     https://github.com/AGProjects/python3-gnutls

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: python3-%modulename-%version.tar

%description
This package provides a high level object oriented wrapper around libgnutls,
as well as low level bindings to the GnuTLS types and functions via ctypes.
The high level wrapper hides the details of accessing the GnuTLS library via
ctypes behind a set of classes that encapsulate GnuTLS sessions, certificates
and credentials and expose them to python applications using a simple API.

The package also includes a Twisted interface that has seamless intergration
with Twisted, providing connectTLS and listenTLS methods on the Twisted
reactor once imported (the methods are automatically attached to the reactor
by simply importing the GnuTLS Twisted interface module).

The high level wrapper is written using the GnuTLS library bindings that are
made available via ctypes. This makes the wrapper very powerful and flexible
as it has direct access to all the GnuTLS internals and is also very easy to
extend without any need to write C code or recompile anything.

%prep
%setup -n python3-%modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README
%python3_sitelibdir/%modulename/
%python3_sitelibdir/python3_%{pyproject_distinfo %modulename}

%changelog
* Sun Apr 02 2023 Andrey Cherepanov <cas@altlinux.org> 3.1.10-alt1
- new version 3.1.10

* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.8-alt1
- Initial build for Sisyphus
