%define _unpackaged_files_terminate_build 1
%define pypi_name email_validator

%def_without check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: A robust email syntax and deliverability validation library for Python
License: CC0-1.0
Group: Development/Python3
Url: https://pypi.org/project/email-validator

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(dns)
BuildRequires: python3(idna)
%endif

BuildArch: noarch

%description
A robust email address syntax and deliverability validation library
for Python by Joshua Tauberer.

This library validates that a string is of the form name@example.com.
This is the sort of validation you would want for an email-based login
form on a website.

Key features:

    Checks that an email address has the correct syntax --- good for login
    forms or other uses related to identifying users.

    Gives friendly error messages when validation fails (appropriate to show
    to end users).

    (optionally) Checks deliverability: Does the domain name resolve?
    And you can override the default DNS resolver.

    Supports internationalized domain names and (optionally) internationalized
    local parts, but blocks unsafe characters.

    Normalizes email addresses (super important for internationalized
    addresses! see below).

The library is NOT for validation of the To: line in an email message
(e.g. My Name <my@address.com>), which flanker is more appropriate for.
And this library does NOT permit obsolete forms of email addresses,
so if you need strict validation against the email specs exactly, use pyIsEmail.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# some tests require connection to a DNS server, so they are disabled
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- 1.2.1 -> 1.3.0

* Sun Aug 07 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus
