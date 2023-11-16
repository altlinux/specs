%define _unpackaged_files_terminate_build 1
%define oname scooby

Name: python3-module-%oname
Version: 0.9.2
Release: alt1
Summary: This is a lightweight tool for easily reporting your Python environment's package versions and hardware resources.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/scooby/
VCS: https://github.com/banesullivan/scooby.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
Requires: python3-module-psutil
Requires: python3-module-numexpr

%description
Scooby is a lightweight module that could easily be added as
a dependency to Python projects for environment reporting when
debugging. Simply add scooby to your dependencies and implement
a function to have scooby report on the aspects of the
environment you care most about. Comes with a command-line interface.

%prep
%setup
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Oct 19 2023 Elizaveta Morozova <morozovaes@altlinux.org> 0.9.2-alt1
- Initial build for ALT.


