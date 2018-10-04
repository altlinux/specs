%define  modulename gnutls

Name:    python-module-%modulename
Version: 3.1.2
Release: alt1

Summary: GnuTLS bindings for Python
License: LGPLv2+
Group:   Development/Python
URL:     https://github.com/AGProjects/python-gnutls

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

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
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build in Sisyphus
