%define  modulename ofxparse

Name:    python3-module-%modulename
Version: 0.21
Release: alt2

Summary: Tools for working with the OFX (Open Financial Exchange) file format
License: MIT
Group:   Development/Python3
URL:     http://sites.google.com/site/ofxparse

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

%description
ofxparse is a parser for Open Financial Exchange (.ofx) format files.
OFX files are available from almost any online banking site, so they
work well if you want to pull together your finances from multiple
sources. Online trading accounts also provide account statements in OFX
files.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.21-alt2
- Drop python2 support.

* Mon May 31 2021 Andrey Cherepanov <cas@altlinux.org> 0.21-alt1
- New version.

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.20-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.19-alt1
- New version.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 0.17-alt2
- Build both for Python2 and Python3.

* Fri Nov 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.17-alt1
- New version.

* Tue Aug 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.16-alt1
- Initial build in Sisyphus
