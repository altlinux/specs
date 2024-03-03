%define oname readme_renderer

Name: python3-module-readme-renderer
Version: 43.0
Release: alt1

Summary: readme_renderer is a library for rendering "readme" descriptions for Warehouse

License: GPLv3+
Group: Development/Python3
Url: https://github.com/pypa/readme_renderer

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)


%py3_use nh3 >= 0.2.14
%py3_use docutils >= 0.13.1
%py3_use Pygments >= 2.5.1

%description
Readme Renderer is a library that will safely render arbitrary README files into HTML.
It is designed to be used in Warehouse to render the long_description for packages.
It can handle Markdown, reStructuredText (.rst), and plain text.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.dist-info


%changelog
* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 43.0-alt1
- new version 43.0 (with rpmrb script)
- update BR, switch to pyproject_build

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 40.0-alt1
- new version 40.0 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 37.3-alt1
- new version 37.3 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 37.0-alt1
- new version 37.0 (with rpmrb script)

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 29.0-alt1
- initial build for ALT Sisyphus
