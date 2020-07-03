%define  modulename distro

Name:    python-module-%modulename
Version: 1.5.0
Release: alt1

Summary: A much more elaborate, renewed alternative implementation for Python's platform.linux_distribution()
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/nir0s/distro

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%package -n python3-module-%modulename
Summary: A much more elaborate, renewed alternative implementation for Python's platform.linux_distribution()
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description -n python3-module-%modulename
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files -n python3-module-%modulename
%_bindir/%modulename
%python3_sitelibdir/*
%doc *.md

%changelog
* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 1.5.0-alt1
- New version

* Mon Apr 08 2019 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
