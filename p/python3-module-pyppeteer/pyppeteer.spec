#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename pyppeteer

Name: python3-module-%modulename
Version: 2.0.0
Release: alt1
Summary: A python headless chrome/chromium automation library
Group: Development/Python3
License: MIT

URL: https://pypi.org/project/pyppeteer
VCS: https://github.com/pyppeteer/pyppeteer

Source: %name-%version.tar

BuildArch: noarch

Buildrequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
Buildrequires: python3-module-poetry-core

%description
Pyppeteer is a headless chrome/chromium automation library
(unofficial port of puppeteer).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md LICENSE
%_bindir/%modulename-install
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Fri Dec 26 2025 Polina Poidenko <polipoki@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
