%define  modulename google-auth-library-python

Name:    python3-module-%modulename
Version: 2.25.2
Release: alt1

Summary: Google Auth Python Library
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/google-auth-library-python

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%add_python3_req_skip requests.packages.urllib3.util.ssl_

%description
This library simplifies using Google's various server-to-server authentication
mechanisms to access Google APIs.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.md

%changelog
* Sat Dec 09 2023 Andrey Cherepanov <cas@altlinux.org> 2.25.2-alt1
- New version.

* Wed Dec 06 2023 Andrey Cherepanov <cas@altlinux.org> 2.25.1-alt1
- New version.

* Fri Dec 01 2023 Andrey Cherepanov <cas@altlinux.org> 2.24.0-alt1
- New version.

* Wed Nov 01 2023 Andrey Cherepanov <cas@altlinux.org> 2.23.4-alt1
- New version.

* Tue Oct 10 2023 Andrey Cherepanov <cas@altlinux.org> 2.23.3-alt1
- New version.

* Fri Sep 29 2023 Andrey Cherepanov <cas@altlinux.org> 2.23.2-alt1
- New version.

* Wed Sep 27 2023 Andrey Cherepanov <cas@altlinux.org> 2.23.1-alt1
- New version.

* Mon Sep 11 2023 Andrey Cherepanov <cas@altlinux.org> 2.23.0-alt1
- New version.

* Wed Jul 12 2023 Andrey Cherepanov <cas@altlinux.org> 2.22.0-alt1
- New version.

* Mon Jun 26 2023 Andrey Cherepanov <cas@altlinux.org> 2.21.0-alt1
- New version.

* Wed Jun 14 2023 Andrey Cherepanov <cas@altlinux.org> 2.20.0-alt1
- New version.

* Thu Jun 08 2023 Andrey Cherepanov <cas@altlinux.org> 2.19.1-alt1
- New version.

* Fri May 26 2023 Andrey Cherepanov <cas@altlinux.org> 2.19.0-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 2.18.1-alt1
- New version.

* Thu May 11 2023 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt1
- New version.

* Tue Apr 18 2023 Andrey Cherepanov <cas@altlinux.org> 2.17.3-alt1
- New version.

* Thu Apr 06 2023 Andrey Cherepanov <cas@altlinux.org> 2.17.2-alt1
- new version 2.17.2

* Fri Mar 31 2023 Andrey Cherepanov <cas@altlinux.org> 2.17.1-alt1
- New version.

* Wed Mar 29 2023 Andrey Cherepanov <cas@altlinux.org> 2.17.0-alt1
- New version.

* Sat Mar 25 2023 Andrey Cherepanov <cas@altlinux.org> 2.16.3-alt1
- New version.

* Fri Mar 03 2023 Andrey Cherepanov <cas@altlinux.org> 2.16.2-alt1
- New version.

* Sat Feb 18 2023 Andrey Cherepanov <cas@altlinux.org> 2.16.1-alt1
- New version.

* Tue Jan 10 2023 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt1
- New version.

* Fri Dec 02 2022 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt1
- New version.

* Tue Nov 08 2022 Andrey Cherepanov <cas@altlinux.org> 2.14.1-alt1
- New version.

* Tue Nov 01 2022 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- New version.

* Tue Oct 18 2022 Andrey Cherepanov <cas@altlinux.org> 2.13.0-alt1
- New version.

* Wed Sep 28 2022 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- New version.

* Fri Sep 23 2022 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Sun Aug 21 2022 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- New version.

* Sat Aug 06 2022 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version.

* Fri Jul 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.1-alt1
- New version.

* Wed Jun 29 2022 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.

* Wed Jun 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version.

* Wed Jun 08 2022 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version.

* Fri Apr 22 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- New version.

* Fri Apr 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version.

* Wed Apr 13 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version.

* Thu Apr 07 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.3-alt1
- New version.

* Thu Mar 17 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version.

* Wed Mar 16 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Tue Feb 01 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Wed Jan 26 2022 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.

* Tue Jan 25 2022 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- New version.

* Sat Jan 22 2022 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Tue Nov 02 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- New version.

* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- New version.

* Tue Oct 26 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version.

* Fri Oct 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Wed Sep 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- New version.

* Tue Sep 28 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Wed Sep 15 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Wed Sep 01 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version.

* Fri Aug 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Wed Aug 18 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Aug 17 2021 Andrey Cherepanov <cas@altlinux.org> 1.35.0-alt1
- New version.

* Wed Jul 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.34.0-alt1
- New version.

* Wed Jul 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.33.1-alt1
- New version.

* Thu Jul 15 2021 Andrey Cherepanov <cas@altlinux.org> 1.33.0-alt1
- New version.

* Thu Jul 01 2021 Andrey Cherepanov <cas@altlinux.org> 1.32.1-alt1
- New version.

* Tue Jun 22 2021 Andrey Cherepanov <cas@altlinux.org> 1.32.0-alt1
- New version.

* Fri Jun 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.31.0-alt1
- New version.

* Wed Jun 09 2021 Andrey Cherepanov <cas@altlinux.org> 1.30.2-alt1
- New version.

* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.30.1-alt1
- New version.

* Sat Apr 27 2019 Anton Midyukov <antohami@altlinux.org> 1.6.3-alt1
- Initial build for Sisyphus
