%define  modulename jaraco.packaging

Name:    python3-module-%modulename
Version: 9.1.2
Release: alt1

Summary: Tools to supplement packaging Python releases
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.packaging

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm
BuildRequires: python3-module-toml

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version
echo 'import setuptools; setuptools.setup()' > setup.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install
rm -rf %buildroot/%_bindir/

%files
%python3_sitelibdir/jaraco/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Dec 29 2022 Andrey Cherepanov <cas@altlinux.org> 9.1.2-alt1
- New version.

* Fri Sep 30 2022 Andrey Cherepanov <cas@altlinux.org> 9.1.1-alt1
- New version.

* Wed Sep 28 2022 Andrey Cherepanov <cas@altlinux.org> 9.1.0-alt1
- New version.

* Fri Feb 11 2022 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Mon Mar 15 2021 Andrey Cherepanov <cas@altlinux.org> 8.2.1-alt1
- New version.

* Tue Dec 29 2020 Andrey Cherepanov <cas@altlinux.org> 8.2.0-alt1
- New version.

* Sun Nov 22 2020 Andrey Cherepanov <cas@altlinux.org> 8.1.1-alt1
- New version.

* Tue Feb 18 2020 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version.

* Mon Aug 05 2019 Andrey Cherepanov <cas@altlinux.org> 6.2-alt1
- New version.

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt2
- fix packing

* Sun Jan 27 2019 Andrey Cherepanov <cas@altlinux.org> 6.1-alt1
- New version.

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 6.0-alt1
- New version.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 5.2-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.

* Mon May 14 2018 Andrey Cherepanov <cas@altlinux.org> 5.1-alt1
- Initial build for Sisyphus
