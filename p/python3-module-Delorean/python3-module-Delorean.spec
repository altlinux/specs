%define _unpackaged_files_terminate_build 1
%define pypi_name Delorean

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Delorean: Time Travel Made Easy
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Delorean
Vcs: https://github.com/myusuf3/delorean.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(nose)
BuildRequires: python3(mock)
BuildRequires: python3(babel)
BuildRequires: python3(humanize)
BuildRequires: python3(tzlocal)
BuildRequires: python3(tzdata)
%endif

BuildArch: noarch

%description
Delorean is a library for clearing up the inconvenient truths that
arise dealing with datetimes in Python. Understanding that timing is
a delicate enough of a problem delorean hopes to provide a cleaner less
troublesome solution to shifting, manipulating, and generating datetimes.

Delorean stands on the shoulders of giants pytz and dateutil

Delorean will provide natural language improvements for manipulating time,
as well as datetime abstractions for ease of use. The overall goal is to
improve datetime manipulations, with a little bit of software and philosophy.

Pretty much make you a badass time traveller.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%_bindir/nosetests3 -v

%files
%doc README.rst LICENSE.txt CHANGES.rst
%python3_sitelibdir/delorean/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
