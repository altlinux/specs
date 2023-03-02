%define oname google-api-client

%def_with python3

Name: python3-module-%oname
Version: 2.80.0
Release: alt1
Summary: Google API Client Library for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/google-api-python-client/
Packager: Andrey Cherepanov <cas@altlinux.org>

# https://github.com/google/google-api-python-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-httplib2 >= 0.8
BuildRequires: python3-module-oauth2client >= 1.4.6
BuildRequires: python3-module-six >= 1.6.1
BuildRequires: python3-module-uritemplate >= 0.6

%add_python3_req_skip google.appengine.api
%py3_requires google_auth_httplib2

%description
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

%package docs
Summary: Documentation for Google API Client Library for Python
Group: Development/Documentation

%description docs
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

This package contains documentation for Google API Client Library for
Python.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -f docs/build

%files
%doc CHANGELOG.md README.md
%python3_sitelibdir/*

%files docs
%doc docs/*

%changelog
* Thu Mar 02 2023 Andrey Cherepanov <cas@altlinux.org> 2.80.0-alt1
- New version.

* Tue Feb 21 2023 Andrey Cherepanov <cas@altlinux.org> 2.79.0-alt1
- New version.

* Wed Feb 15 2023 Andrey Cherepanov <cas@altlinux.org> 2.78.0-alt1
- New version.

* Wed Feb 08 2023 Andrey Cherepanov <cas@altlinux.org> 2.77.0-alt1
- New version.

* Fri Feb 03 2023 Andrey Cherepanov <cas@altlinux.org> 2.76.0-alt1
- New version.

* Wed Feb 01 2023 Andrey Cherepanov <cas@altlinux.org> 2.75.0-alt1
- New version.

* Wed Jan 25 2023 Andrey Cherepanov <cas@altlinux.org> 2.74.0-alt1
- New version.

* Tue Jan 17 2023 Andrey Cherepanov <cas@altlinux.org> 2.73.0-alt1
- New version.

* Wed Jan 11 2023 Andrey Cherepanov <cas@altlinux.org> 2.72.0-alt1
- New version.

* Thu Jan 05 2023 Andrey Cherepanov <cas@altlinux.org> 2.71.0-alt1
- New version.
- Required google_auth_httplib2 (ALT #44381).

* Wed Dec 14 2022 Andrey Cherepanov <cas@altlinux.org> 2.70.0-alt1
- New version.

* Thu Dec 08 2022 Andrey Cherepanov <cas@altlinux.org> 2.69.0-alt1
- New version.

* Thu Dec 01 2022 Andrey Cherepanov <cas@altlinux.org> 2.68.0-alt1
- New version.

* Thu Nov 17 2022 Andrey Cherepanov <cas@altlinux.org> 2.67.0-alt1
- New version.

* Wed Oct 19 2022 Andrey Cherepanov <cas@altlinux.org> 2.65.0-alt1
- New version.

* Wed Oct 05 2022 Andrey Cherepanov <cas@altlinux.org> 2.64.0-alt1
- New version.

* Wed Sep 28 2022 Andrey Cherepanov <cas@altlinux.org> 2.63.0-alt1
- New version.

* Fri Sep 23 2022 Andrey Cherepanov <cas@altlinux.org> 2.62.0-alt1
- New version.

* Wed Sep 14 2022 Andrey Cherepanov <cas@altlinux.org> 2.61.0-alt1
- New version.

* Wed Sep 07 2022 Andrey Cherepanov <cas@altlinux.org> 2.60.0-alt1
- New version.

* Wed Aug 31 2022 Andrey Cherepanov <cas@altlinux.org> 2.59.0-alt1
- New version.

* Wed Aug 24 2022 Andrey Cherepanov <cas@altlinux.org> 2.58.0-alt1
- New version.

* Wed Aug 17 2022 Andrey Cherepanov <cas@altlinux.org> 2.57.0-alt1
- New version.

* Wed Aug 10 2022 Andrey Cherepanov <cas@altlinux.org> 2.56.0-alt1
- New version.

* Wed Jul 27 2022 Andrey Cherepanov <cas@altlinux.org> 2.55.0-alt1
- New version.

* Tue Jul 19 2022 Andrey Cherepanov <cas@altlinux.org> 2.54.0-alt1
- New version.

* Thu Jul 14 2022 Andrey Cherepanov <cas@altlinux.org> 2.53.0-alt1
- New version.

* Wed Jun 29 2022 Andrey Cherepanov <cas@altlinux.org> 2.52.0-alt1
- New version.

* Wed Jun 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.51.0-alt1
- New version.

* Wed Jun 08 2022 Andrey Cherepanov <cas@altlinux.org> 2.50.0-alt1
- New version.

* Thu May 26 2022 Andrey Cherepanov <cas@altlinux.org> 2.49.0-alt1
- New version.

* Wed May 18 2022 Andrey Cherepanov <cas@altlinux.org> 2.48.0-alt1
- New version.

* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 2.47.0-alt1
- New version.

* Wed Apr 27 2022 Andrey Cherepanov <cas@altlinux.org> 2.46.0-alt1
- New version.

* Tue Apr 19 2022 Andrey Cherepanov <cas@altlinux.org> 2.45.0-alt1
- New version.

* Wed Apr 13 2022 Andrey Cherepanov <cas@altlinux.org> 2.44.0-alt1
- New version.

* Wed Apr 06 2022 Andrey Cherepanov <cas@altlinux.org> 2.43.0-alt1
- New version.

* Wed Mar 23 2022 Andrey Cherepanov <cas@altlinux.org> 2.42.0-alt1
- New version.

* Wed Mar 16 2022 Andrey Cherepanov <cas@altlinux.org> 2.41.0-alt1
- New version.

* Sat Mar 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.40.0-alt1
- New version.

* Wed Mar 02 2022 Andrey Cherepanov <cas@altlinux.org> 2.39.0-alt1
- New version.

* Thu Feb 24 2022 Andrey Cherepanov <cas@altlinux.org> 2.38.0-alt1
- New version.

* Thu Feb 10 2022 Andrey Cherepanov <cas@altlinux.org> 2.37.0-alt1
- New version.

* Wed Jan 19 2022 Andrey Cherepanov <cas@altlinux.org> 2.36.0-alt1
- New version.

* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 2.35.0-alt1
- New version.

* Wed Jan 05 2022 Andrey Cherepanov <cas@altlinux.org> 2.34.0-alt1
- New version.

* Fri Dec 10 2021 Andrey Cherepanov <cas@altlinux.org> 2.33.0-alt1
- New version.

* Fri Dec 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.32.0-alt1
- New version.

* Wed Nov 17 2021 Andrey Cherepanov <cas@altlinux.org> 2.31.0-alt1
- New version.

* Wed Nov 10 2021 Andrey Cherepanov <cas@altlinux.org> 2.30.0-alt1
- New version.

* Wed Nov 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.29.0-alt1
- New version.

* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.28.0-alt1
- New version.

* Wed Oct 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.27.0-alt1
- New version.

* Wed Oct 13 2021 Andrey Cherepanov <cas@altlinux.org> 2.26.1-alt1
- New version.

* Tue Oct 12 2021 Andrey Cherepanov <cas@altlinux.org> 2.25.0-alt1
- New version.

* Wed Oct 06 2021 Andrey Cherepanov <cas@altlinux.org> 2.24.0-alt1
- New version.

* Wed Sep 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.23.0-alt1
- New version.

* Wed Sep 22 2021 Andrey Cherepanov <cas@altlinux.org> 2.22.0-alt1
- New version.

* Wed Sep 15 2021 Andrey Cherepanov <cas@altlinux.org> 2.21.0-alt1
- New version.

* Thu Sep 09 2021 Andrey Cherepanov <cas@altlinux.org> 2.20.0-alt1
- New version.

* Fri Sep 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.19.1-alt1
- New version.

* Wed Sep 01 2021 Andrey Cherepanov <cas@altlinux.org> 2.19.0-alt1
- New version.

* Tue Aug 24 2021 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt1
- New version.

* Wed Aug 18 2021 Andrey Cherepanov <cas@altlinux.org> 2.17.0-alt1
- New version.

* Thu Aug 12 2021 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt1
- New version.

* Wed Jul 28 2021 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt1
- New version.

* Tue Jul 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.14.1-alt1
- New version.

* Wed Jul 21 2021 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- New version.

* Tue Jul 13 2021 Andrey Cherepanov <cas@altlinux.org> 2.13.0-alt1
- New version.

* Thu Jul 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- New version.

* Wed Jun 30 2021 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- New version.

* Wed Jun 23 2021 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.

* Tue Jun 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version.

* Wed Jun 02 2021 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version.

* Wed May 26 2021 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Thu May 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.
- Build only module for python3.

* Thu May 13 2021 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Thu Apr 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Fri Apr 16 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Thu Apr 01 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version.

* Thu Nov 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.8-alt1
- New version.

* Fri Oct 23 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.5-alt1
- New version.

* Wed Oct 21 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.4-alt1
- New version.

* Wed Sep 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.3-alt1
- New version.

* Fri Sep 25 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.2-alt1
- New version.

* Fri Sep 18 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version.
- Fix License tag according to SPDX.

* Thu May 07 2020 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1
- New version.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version.

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.7.12-alt1
- New version.

* Tue Aug 13 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.11-alt1
- New version.

* Sat Jul 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.10-alt1
- New version.

* Thu May 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.9-alt1
- New version.

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.8-alt1
- New version.

* Fri Dec 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.7-alt1
- New version.

* Sun Dec 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- New version.

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version.

* Fri Jul 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1
- New version.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.3-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version.

* Sun Apr 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.7-alt1
- New version.

* Thu Mar 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.6-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.5-alt1
- New version.

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt1.git20140913.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20140913
- Initial build for Sisyphus

