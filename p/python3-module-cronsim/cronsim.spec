Name: python3-module-cronsim
Version: 2.6
Release: alt1

Summary: A cron expression parser and evaluator
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/cronsim/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/cronsim
%python3_sitelibdir/cronsim-%version.dist-info

%changelog
* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.6-alt1
- 2.6 released

