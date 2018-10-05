%define  modulename xcaplib

Name:    python-module-%modulename
Version: 1.2.1
Release: alt1

Summary: XCAP (RFC4825) client library
License: LGPLv2+
Group:   Development/Python
URL:     https://github.com/AGProjects/python-xcaplib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  python-%modulename-%version.tar

%description
XCAP protocol, defined in RFC 4825, allows a client to read, write, and
modify application configuration data stored in XML format on a server.
XCAP maps XML document sub-trees and element attributes to HTTP URIs, so
that these components can be directly accessed by HTTP. An XCAP server
used by XCAP clients to store data like presence policy in combination
with a SIP Presence server that supports PUBLISH/SUBSCRIBE/NOTIFY SIP
methods can provide a complete SIP SIMPLE solution.

The XCAP client example script provided by this package can be used to
manage documents on an XCAP server.

%prep
%setup -n python-%modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README examples TODO
%_bindir/xcapclient
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
