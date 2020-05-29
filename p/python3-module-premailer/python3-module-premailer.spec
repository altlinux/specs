%define _unpackaged_files_terminate_build 1
%define mname premailer

Name: python3-module-%mname
Version: 3.7.0
Release: alt1
Summary: Turns CSS blocks into style attributes
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/peterbe/premailer
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Premailer is a Python library based on libxml which can analyze a HTML document
and extract its CSS style sheets and then for all CSS seletors defined, it finds
the DOM nodes and puts style attributes in instead.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info
%doc LICENSE README.rst

%changelog
* Fri May 29 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.7.0-alt1
- Updated to version 3.7.0
- Some fix spec

* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.1-alt1
- New version

* Sun May 26 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.4.1-alt1
- New version

* Sun Mar 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 3.4.0-alt1
- Initial build for ALT
