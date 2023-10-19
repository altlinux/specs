%define  modulename num2words

Name:    python3-module-%modulename
Version: 0.5.13
Release: alt1

Summary: Modules to convert numbers to words. 42 --> forty-two
License: LGPL-2.1
Group:   Development/Python3
URL:     https://github.com/savoirfairelinux/num2words

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

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
* Thu Oct 19 2023 Andrey Cherepanov <cas@altlinux.org> 0.5.13-alt1
- New version.

* Sun Aug 21 2022 Andrey Cherepanov <cas@altlinux.org> 0.5.12-alt1
- New version.

* Thu Aug 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.5.11-alt1
- New version.

* Sun May 12 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.10-alt1
- New version.

* Fri Jan 11 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.9-alt1
- New version.

* Tue Dec 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.8-alt1
- New version.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.7-alt1
- New version.

* Fri Apr 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.6-alt1
- Initial build for Sisyphus
