%define _unpackaged_files_terminate_build 1
%define pypi_name email-validator
%define mod_name email_validator

# tests require connection to the Internet
%def_without check

Name: python3-module-%pypi_name
Version: 2.2.0
Release: alt1

Summary: A robust email syntax and deliverability validation library for Python
License: CC0-1.0
Group: Development/Python3
Url: https://pypi.org/project/email-validator
Vcs: https://github.com/JoshData/python-email-validator

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A robust email address syntax and deliverability validation library
for Python by Joshua Tauberer.

This library validates that a string is of the form name@example.com.
This is the sort of validation you would want for an email-based login
form on a website.

Key features:

* Checks that an email address has the correct syntax --- good for
  login forms or other uses related to identifying users.

* Gives friendly error messages when validation fails (appropriate
  to show to end users).

* (optionally) Checks deliverability: Does the domain name resolve?
  And you can override the default DNS resolver.

* Supports internationalized domain names and (optionally)
  internationalized local parts, but blocks unsafe characters.

* Normalizes email addresses (super important for internationalized
  addresses!).

The library is NOT for validation of the To: line in an email message
(e.g. My Name <my@address.com>), which flanker is more appropriate for.
And this library does NOT permit obsolete forms of email addresses,
so if you need strict validation against the email specs exactly,
use pyIsEmail.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test_requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 03 2024 Alexandr Shashkin <dutyrok@altlinux.org> 2.2.0-alt1
- Updated to 2.2.0.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.1-alt1
- Updated to 2.1.1.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.0.post1-alt1
- Updated to 2.1.0.post1.

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.0.post2-alt1
- New version.
- Reformat description.

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- 1.2.1 -> 1.3.0

* Sun Aug 07 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus
