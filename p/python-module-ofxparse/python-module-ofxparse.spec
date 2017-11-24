%define  modulename ofxparse

Name:    python-module-%modulename
Version: 0.17
Release: alt1

Summary: Tools for working with the OFX (Open Financial Exchange) file format
License: MIT
Group:   Development/Python
URL:     http://sites.google.com/site/ofxparse

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

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
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Fri Nov 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.17-alt1
- New version.

* Tue Aug 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.16-alt1
- Initial build in Sisyphus
