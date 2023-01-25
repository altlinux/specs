%define _unpackaged_files_terminate_build 1
%define modname premailer
%def_with check

Name: python3-module-%modname
Version: 3.10.0
Release: alt1
Summary: Turns CSS blocks into style attributes
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/peterbe/premailer
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools)

%if_with check
BuildRequires: python3(cachetools)
BuildRequires: python3(cssutils)
BuildRequires: python3(cssselect)
BuildRequires: python3(lxml)
BuildRequires: python3(nose)
BuildRequires: python3(mock)
BuildRequires: python3(requests)
%endif

%description
Premailer is a Python library based on libxml which can analyze a HTML document
and extract its CSS style sheets and then for all CSS seletors defined, it finds
the DOM nodes and puts style attributes in instead.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run nosetests

%files
%python3_sitelibdir/%modname
%python3_sitelibdir/%{pyproject_distinfo %modname}

%changelog
* Wed Jan 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.10.0-alt1
- Updated to version 3.10.0
- Use pyproject macroses for build
- Enabled tests

* Fri May 29 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.7.0-alt1
- Updated to version 3.7.0
- Some fix spec

* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.1-alt1
- New version

* Sun May 26 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.4.1-alt1
- New version

* Sun Mar 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.4.0-alt1
- Initial build for ALT
