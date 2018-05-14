%define  modulename rst.linker

Name:    python3-module-%modulename
Version: 1.9
Release: alt1

Summary: rst.linker provides a routine for adding links and performing other custom replacements to reStructuredText files as a Sphinx extension
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/rst.linker

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%{summary}.

%prep
%setup -n %modulename-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%files
%python3_sitelibdir/rst/*.py
%python3_sitelibdir/rst/__pycache__/*
%python3_sitelibdir/rst.linker*
%python3_sitelibdir/*.egg-info

%changelog
* Mon May 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.9-alt1
- Initial build for Sisyphus
