Name:    python3-module-google-api-core
Version: 2.19.2
Release: alt1

Summary: Core Library for Google Client Libraries
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/python-api-core

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source: python-api-core-%version.tar
Patch0: 0001-fix-resolve-issue-handling-protobuf-responses-in-res.patch

%description
%summary

This library is not meant to stand-alone. Instead it defines common
helpers used by all Google API clients. For more information, see the
documentation at https://googleapis.dev/python/google-api-core/latest.

%prep
%setup -n python-api-core-%version
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/google/api_core
%python3_sitelibdir/*.egg-info

%changelog
* Wed Aug 28 2024 Andrey Cherepanov <cas@altlinux.org> 2.19.2-alt1
- New version.

* Tue Jun 25 2024 Andrey Cherepanov <cas@altlinux.org> 2.19.1-alt1
- New version.

* Wed May 01 2024 Andrey Cherepanov <cas@altlinux.org> 2.19.0-alt1
- New version.

* Fri Mar 22 2024 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt1
- New version.

* Thu Feb 15 2024 Andrey Cherepanov <cas@altlinux.org> 2.17.1-alt1
- New version.

* Fri Feb 09 2024 Andrey Cherepanov <cas@altlinux.org> 2.17.0-alt1
- New version.

* Sat Feb 03 2024 Andrey Cherepanov <cas@altlinux.org> 2.16.2-alt1
- New version.

* Wed Jan 31 2024 Andrey Cherepanov <cas@altlinux.org> 2.16.1-alt1
- New version.

* Tue Jan 30 2024 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt1
- New version.

* Fri Dec 08 2023 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt1
- New version.

* Sat Nov 11 2023 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- New version.

* Wed Nov 08 2023 Andrey Cherepanov <cas@altlinux.org> 2.13.0-alt1
- New version.

* Tue Oct 17 2023 Grigory Ustinov <grenka@altlinux.org> 2.12.0-alt2
- Dropped dependency on distutils.

* Tue Sep 26 2023 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- New version.

* Thu Jun 15 2023 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Fri Dec 02 2022 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- New version.

* Sat Oct 08 2022 Andrey Cherepanov <cas@altlinux.org> 2.10.2-alt1
- New version.

* Thu Sep 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.10.1-alt1
- New version.

* Fri Sep 02 2022 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version.

* Wed Jun 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.8.2-alt1
- New version.

* Fri May 27 2022 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- New version.

* Thu May 19 2022 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version.

* Tue May 03 2022 Andrey Cherepanov <cas@altlinux.org> 2.7.3-alt1
- New version.

* Thu Apr 14 2022 Andrey Cherepanov <cas@altlinux.org> 2.7.2-alt1
- New version.

* Sat Mar 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- New version.

* Tue Mar 08 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Fri Mar 04 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Thu Feb 03 2022 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.

* Wed Jan 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Mon Dec 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- New version.

* Thu Dec 16 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version.

* Fri Dec 10 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Wed Nov 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- New version.

* Fri Oct 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- New version.

* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Thu Oct 14 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- New version.

* Wed Oct 06 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Wed Sep 01 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Thu Aug 19 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Aug 17 2021 Andrey Cherepanov <cas@altlinux.org> 1.31.2-alt1
- New version.

* Wed Jul 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.31.1-alt1
- New version.

* Sat Jul 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.31.0-alt1
- New version.

* Wed Jun 09 2021 Andrey Cherepanov <cas@altlinux.org> 1.30.0-alt1
- New version.

* Thu Jun 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.29.0-alt1
- New version.

* Fri May 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.28.0-alt1
- New version.

* Tue May 18 2021 Andrey Cherepanov <cas@altlinux.org> 1.27.0-alt1
- New version.

* Tue Mar 30 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.3-alt1
- New version.

* Wed Mar 24 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.2-alt1
- New version.

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.1-alt1
- New version.

* Thu Feb 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.26.0-alt1
- New version.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- Initial build for Sisyphus
