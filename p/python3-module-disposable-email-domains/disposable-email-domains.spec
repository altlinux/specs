%define _unpackaged_files_terminate_build 1

Name: python3-module-disposable-email-domains

Version: 0.0.265
Release: alt1.git3072547

Summary: Python library with a set of known disposable email domains
License: MIT
Group: Development/Python
Url: https://pypi.org/project/disposable-email-domains/
Vcs: https://github.com/disposable-email-domains/python-disposable-email-domains

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
This module provides a set of known disposable email domains.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc *.md LICENSE.txt
%python3_sitelibdir_noarch/disposable_email_domains
%python3_sitelibdir_noarch/%{pyproject_distinfo disposable_email_domains}

%changelog
* Wed Sep 23 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 0.0.265-alt1.git3072547
- Initial build for Sisyphus.

