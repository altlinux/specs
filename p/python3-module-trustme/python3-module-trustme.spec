%define  modulename trustme

Name:    python3-module-%modulename
Version: 0.9.0
Release: alt1

Summary: #1 quality TLS certs while you wait, for the discerning tester
License: Apache2 or MIT
Group:   Development/Python3
URL:     https://github.com/python-trio/trustme

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
trustme is a tiny Python package that does one thing: it gives you a
fake certificate authority (CA) that you can use to generate fake TLS
certs to use in your tests. Well, technically they're real certs,
they're just signed by your CA, which nobody trusts. But you can trust
it. Trust me.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%{modulename}*

%changelog
* Fri Aug 13 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version.

* Wed Jun 09 2021 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version.
- Build only for Python 3.

* Wed Feb 10 2021 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- New version.

* Thu Mar 26 2020 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt2
- Build both Python2 and Python3 modules.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- New version.

* Thu Oct 31 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.3-alt1
- New version.
- Build without Python2 support.

* Tue Jun 04 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- New version.

* Tue Jan 22 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
