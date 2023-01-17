%define  modulename shtab
%def_with check

Name:    python3-module-%modulename
Version: 1.5.8
Release: alt1

Summary: Automagic shell tab completion for Python CLI applications
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/iterative/shtab

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-cov python3-module-pytest-timeout
%endif

BuildArch: noarch

Source:  %name-%version.tar
# Fix version detection
Patch:   python3-module-shtab-1.5.8-alt-version-detection-fix.patch

%description
%summary.

%prep
%setup
%patch -p1
sed -i 's/VERSION_UNKNOWN/%version/' setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc README.rst CONTRIBUTING.md LICENCE docs/index.md docs/use.md examples

%changelog
* Tue Nov 29 2022 Alexander Stepchenko <geochip@altlinux.org> 1.5.8-alt1
- Initial build for ALT.
