%define  modulename ofxparse

Name:    python-module-%modulename
Version: 0.17
Release: alt2

Summary: Tools for working with the OFX (Open Financial Exchange) file format
License: MIT
Group:   Development/Python
URL:     http://sites.google.com/site/ofxparse

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

%description
ofxparse is a parser for Open Financial Exchange (.ofx) format files.
OFX files are available from almost any online banking site, so they
work well if you want to pull together your finances from multiple
sources. Online trading accounts also provide account statements in OFX
files.

%package -n python3-module-%modulename
Summary: Tools for working with the OFX (Open Financial Exchange) file format
Group:   Development/Python3

%description -n python3-module-%modulename
ofxparse is a parser for Open Financial Exchange (.ofx) format files.
OFX files are available from almost any online banking site, so they
work well if you want to pull together your finances from multiple
sources. Online trading accounts also provide account statements in OFX
files.

%prep
%setup -n %modulename-%version
mkdir build-python3
cp -a * build-python3 ||:

%build
%python_build
pushd build-python3
%python3_build
popd

%install
%python_install
pushd build-python3
%python3_install
popd

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info


%changelog
* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 0.17-alt2
- Build both for Python2 and Python3.

* Fri Nov 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.17-alt1
- New version.

* Tue Aug 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.16-alt1
- Initial build in Sisyphus
