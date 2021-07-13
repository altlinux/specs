%define oname junos-eznc

Summary: Junos 'EZ' automation for non-programmers
Name: python3-module-%oname
Version: 2.0.1
Release: alt2
Url: https://github.com/Juniper/py-junos-eznc
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: Apache-2.0
Group: Development/Python3

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs

%description
Junos PyEZ is a Python library to remotely manage/automate Junos
devices. The user is NOT required: (a) to be a "Software Programmer",
(b) have sophisticated knowledge of Junos, or (b) have a complex
understanding of the Junos XML API.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%files
%doc COPYRIGHT INSTALL-FEDORA.md INSTALL-FREEBSD.md INSTALL-OSX.md INSTALL-UBUNTU-DEBIAN.md LICENSE README.md README.txt RELEASE-NOTES.md development.txt docreq.txt requirements.txt
%python3_sitelibdir/*

%changelog
* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Drop python2 support.

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 2.0.1-alt1
- New version

* Thu Jun 16 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt2
- Do not move jnpr/junos stuff to jnpr directory (ALT#32198)
  (thx Andrey Cherepanov cas@).
- %%python_req_hier -- for more detailed self-satisfied autoreqs (jnpr.*),
  without the general UNMET python2.X(jnpr).

* Thu Jun 16 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.3.1-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.2-alt1
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.2-alt1
- Initial build for ALT

