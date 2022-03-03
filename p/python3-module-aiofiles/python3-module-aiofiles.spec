%define  modulename aiofiles

Name:    python3-module-%modulename
Version: 0.8.0
Release: alt1

Summary: File support for asyncio
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/Tinche/aiofiles
# Source-url: https://pypi.python.org/packages/source/a/aiofiles/aiofiles-%version.tar.gz

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst LICENSE

%changelog
* Thu Mar 03 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt1
- new version (0.8.0) with rpmgs script

* Tue Nov 09 2021 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- new version (0.7.0) with rpmgs script
- source from tarball

* Mon May 24 2021 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt2
- rename srpm to python3-module-aiofiles

* Fri Feb 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
