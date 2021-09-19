%define modulename xcaplib

Name:    python3-module-%modulename
Version: 2.0.1
Release: alt1

Summary: XCAP (RFC4825) client library
License: LGPLv2+
Group:   Development/Python3
URL:     https://github.com/AGProjects/python3-xcaplib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source: python3-%modulename-%version.tar
Patch: xcaplib-fix-urllib.request.HTTPHandler-inheritance.patch

Conflicts: python-module-xcaplib

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
%setup -n python3-%modulename-%version
%patch -p1

%build
%python3_build

%install
%python3_install

%files
%doc README examples TODO
%_bindir/xcapclient3
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Sep 16 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
