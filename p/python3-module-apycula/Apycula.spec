%define srcname Apycula
%define modulename apycula

Name:    python3-module-%modulename
Version: 0.3
Release: alt1

Summary: Documentation and open source tools for the Gowin FPGA bitstream format
License: MIT
Group:   Development/Python3
Url:     https://github.com/YosysHQ/apicula

# Source-url: %__pypi_url %srcname
Source: %srcname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%description
%summary.

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/%modulename
%python3_sitelibdir/%srcname-%version-py3.*.egg-info
%doc *.md doc/*

%changelog
* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Initial build for Sisyphus
