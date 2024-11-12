%define oname caldav

Name: python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: A CalDAV (RFC4791) client library for Python

License: GPL-3.0-only
Group: Development/Python
Url: https://github.com/python-caldav/caldav/

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(build)
BuildRequires: python3(setuptools_scm)

%description
A CalDAV (RFC4791) client library for Python.

%prep
%setup -n %oname-%version

%build
%pyproject_scm_init %version
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Tue Nov 12 2024 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- new version

* Wed Jan 24 2024 Vladimir Didenko <cow@altlinux.org> 1.3.9-alt1
- new version

* Thu Sep 7 2023 Vladimir Didenko <cow@altlinux.org> 1.3.6-alt1
- new version

* Mon Mar 20 2023 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- new version

* Tue Feb 14 2023 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- new version

* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.org> 0.11.0-alt1
- new version

* Fri Oct 28 2022 Vladimir Didenko <cow@altlinux.org> 0.10.0-alt1
- new version

* Thu Jun 30 2022 Vladimir Didenko <cow@altlinux.org> 0.9.1-alt1
- new version

* Tue Mar 29 2022 Vladimir Didenko <cow@altlinux.org> 0.8.2-alt1
- new version

* Thu Mar 3 2022 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt1
- initial build for Sisyphus
