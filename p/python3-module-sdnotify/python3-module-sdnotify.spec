%define  modulename sdnotify

Name:    python3-module-%modulename
Version: 0.3.2
Release: alt3

Summary: A pure Python implementation of systemd's service notification protocol (sd_notify)
License: MIT
Group:   Development/Python3
URL:     https://github.com/bb4242/sdnotify

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

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
* Tue May 25 2021 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt3
- rename srpm to python3-module-sdnotify
- drop python2 subpackage
- cleanup spec

* Tue Aug 28 2018 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt2
- fix buildrequires

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
