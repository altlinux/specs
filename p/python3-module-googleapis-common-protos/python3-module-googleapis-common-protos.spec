Name:    python3-module-googleapis-common-protos
Version: 1.74.0
Release: alt1

Summary: Common protobufs used in Google APIs
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/google-cloud-python

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: python-api-common-protos-%version.tar

%py3_provides google.longrunning google.rpc

%description
googleapis-common-protos contains the python classes generated from the common
protos in the googleapis/api-common-protos repository.

%prep
%setup -n python-api-common-protos-%version

%build
cd packages/googleapis-common-protos
%pyproject_build

%install
cd packages/googleapis-common-protos
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Fri Apr 03 2026 Andrey Cherepanov <cas@altlinux.org> 1.74.0-alt1
- New version.

* Fri Mar 27 2026 Andrey Cherepanov <cas@altlinux.org> 1.73.1-alt1
- New version.

* Fri Mar 06 2026 Andrey Cherepanov <cas@altlinux.org> 1.73.0-alt1
- New version.

* Fri Nov 07 2025 Andrey Cherepanov <cas@altlinux.org> 1.72.0-alt1
- New version.

* Tue Oct 21 2025 Andrey Cherepanov <cas@altlinux.org> 1.71.0-alt1
- New version.

* Sun Sep 21 2025 Andrey Cherepanov <cas@altlinux.org> 1.70.0-alt1
- New version.
- New upstream URL https://github.com/googleapis/google-cloud-python.

* Wed Nov 13 2024 Andrey Cherepanov <cas@altlinux.org> 1.66.0-alt1
- New version.

* Tue Aug 27 2024 Andrey Cherepanov <cas@altlinux.org> 1.65.0-alt1
- New version.

* Tue Aug 27 2024 Andrey Cherepanov <cas@altlinux.org> 1.64.0-alt1
- New version.

* Tue Jun 25 2024 Andrey Cherepanov <cas@altlinux.org> 1.63.2-alt1
- New version.

* Mon Jun 03 2024 Andrey Cherepanov <cas@altlinux.org> 1.63.1-alt1
- New version.

* Tue Mar 12 2024 Andrey Cherepanov <cas@altlinux.org> 1.63.0-alt1
- New version.

* Fri Dec 08 2023 Andrey Cherepanov <cas@altlinux.org> 1.62.0-alt1
- New version.

* Fri Oct 13 2023 Andrey Cherepanov <cas@altlinux.org> 1.61.0-alt1
- New version.

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 1.60.0-alt1
- New version.

* Tue Jun 13 2023 Andrey Cherepanov <cas@altlinux.org> 1.59.1-alt1
- New version.

* Wed Mar 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.59.0-alt1
- New version.

* Mon Jan 09 2023 Andrey Cherepanov <cas@altlinux.org> 1.58.0-alt1
- New version.

* Thu Jan 05 2023 Andrey Cherepanov <cas@altlinux.org> 1.57.1-alt1
- New version.

* Wed Nov 16 2022 Andrey Cherepanov <cas@altlinux.org> 1.57.0-alt1
- New version.

* Fri Jul 15 2022 Andrey Cherepanov <cas@altlinux.org> 1.56.4-alt1
- New version.

* Wed Jun 22 2022 Andrey Cherepanov <cas@altlinux.org> 1.56.3-alt1
- New version.

* Fri May 27 2022 Andrey Cherepanov <cas@altlinux.org> 1.56.2-alt1
- New version.

* Fri May 13 2022 Andrey Cherepanov <cas@altlinux.org> 1.56.1-alt1
- New version.

* Fri Mar 18 2022 Andrey Cherepanov <cas@altlinux.org> 1.56.0-alt1
- New version.

* Thu Feb 24 2022 Andrey Cherepanov <cas@altlinux.org> 1.55.0-alt1
- New version.

* Fri Dec 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.54.0-alt1
- New version.

* Wed May 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.53.0-alt1
- Initial build for Sisyphus
