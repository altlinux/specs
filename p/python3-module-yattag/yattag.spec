%define _unpackaged_files_terminate_build 1
%define pkgname yattag

Name:    python3-module-%pkgname
Version: 1.16.0
Release: alt1
Summary: Generate HTML or XML in a concise and pythonic way
Group:   Development/Python3

License: LGPL-2.1-only
URL: https://github.com/leforestier/yattag
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Why use a template engine when you can generate HTML or XML documents
with Python in a very readable way?

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v test

%files
%python3_sitelibdir/%pkgname/
%python3_sitelibdir/%{pyproject_distinfo %pkgname}

%changelog
* Wed Aug 07 2024 Anton Vyatkin <toni@altlinux.org> 1.16.0-alt1
- New version 1.16.0.

* Sun Oct 29 2023 Anton Vyatkin <toni@altlinux.org> 1.15.2-alt1
- New version 1.15.2.

* Tue Jul 04 2023 Anton Vyatkin <toni@altlinux.org> 1.15.1-alt1
- New version 1.15.1.

* Tue Apr 11 2023 Anton Vyatkin <toni@altlinux.org> 1.14.0-alt2
- Fix BuildRequires

* Tue Dec 27 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.14.0-alt1
- Initial build
