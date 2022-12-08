%define repo elevate

Name: python3-module-elevate
Version: 0.1.3
Release: alt0.1.git78e82a8
Summary: Python library that re-launches the current process with root
License: MIT
Group: Development/Python3
Url: https://github.com/barneygale/elevate

Source: %url/archive/%version/%repo-%version.tar.gz
# Built from VCS.
# git merge -s recursive upstream --allow-unrelated-histories

BuildArch: noarch

BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-wheel

%description
Elevate is a small Python library that re-launches
the current process with root or admin privileges.

%prep
%setup -n %repo-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc COPYING.txt README.rst
%python3_sitelibdir_noarch/%{repo}*

%changelog
* Thu Dec 08 2022 Leontiy Volodin <lvol@altlinux.org> 0.1.3-alt0.1.git78e82a8
- Initial build for ALT Sisyphus.
- Built as require for howdy.
