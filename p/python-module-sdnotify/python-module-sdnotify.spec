%define  modulename sdnotify

Name:    python-module-%modulename
Version: 0.3.2
Release: alt2

Summary: A pure Python implementation of systemd's service notification protocol (sd_notify)
License: MIT
Group:   Development/Python3
URL:     https://github.com/bb4242/sdnotify

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%package -n python3-module-%modulename
Summary: A pure Python implementation of systemd's service notification protocol (sd_notify)
Group: Development/Python3

%description -n python3-module-%modulename
%summary

%prep
%setup -n %modulename-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Aug 28 2018 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt2
- fix buildrequires

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
