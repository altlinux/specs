%define pypi_name zxcvbn

%def_disable check

Name: python3-module-%pypi_name
Version: 4.4.28
Release: alt1

Summary: A realistic password strength estimator
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%pypi_name
Vcs: https://github.com/dwolfhub/zxcvbn-python.git

Source: https://pypi.io/packages/source/z/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-setuptools

%description
This is a Python implementation of the library created by the team at
Dropbox.

While there may be other Python ports available, this one is the most up
to date and is recommended by the original developers of zxcvbn at this
time.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Wed Jun 28 2023 Yuri N. Sedunov <aris@altlinux.org> 4.4.28-alt1
- first build for Sisyphus



