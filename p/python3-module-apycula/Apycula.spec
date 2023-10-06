%define srcname Apycula
%define modulename apycula

Name:    python3-module-%modulename
Version: 0.9.1
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
BuildRequires: python3(wheel)

%description
%summary.

%prep
%setup -n %srcname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/*
%python3_sitelibdir/%modulename
%python3_sitelibdir/%srcname-%version.dist-info
%doc *.md doc/*

%changelog
* Fri Oct 06 2023 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt1
- new version (0.9.1) with rpmgs script

* Mon Aug 14 2023 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- new version (0.8.3) with rpmgs script

* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt1
- new version (0.8.1) with rpmgs script

* Sun Apr 30 2023 Anton Midyukov <antohami@altlinux.org> 0.8-alt1
- new version (0.8) with rpmgs script

* Sat Jan 14 2023 Anton Midyukov <antohami@altlinux.org> 0.6.1-alt1
- new version (0.6.1) with rpmgs script

* Sun Jun 19 2022 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- new version (0.4) with rpmgs script

* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Initial build for Sisyphus
