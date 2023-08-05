%def_without check

%define modulename pympler
Name: python3-module-pympler
Version: 1.0.1
Release: alt1

Summary: A development tool to measure, monitor and analyze the memory behavior of Python objects

Url: https://github.com/pympler/pympler
License: Apache-2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url Pympler
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires:  python3-module-setuptools python3-module-wheel


%description
Pympler is a development tool to measure, monitor and
analyze the memory behavior of Python objects in a running Python application.

By pympling a Python application, detailed insight in the size and
the lifetime of Python objects can be obtained. Undesirable
or unexpected runtime behavior like memory bloat and other "pymples" can easily be identified.

Pympler integrates three previously separate projects into a single,
comprehensive profiling tool. Asizeof provides basic size information
for one or several Python objects, muppy is used for on-line monitoring
of a Python application and the class tracker provides off-line analysis
of the lifetime of selected Python objects. A web profiling frontend
exposes process statistics, garbage visualisation and class tracker statistics.

Pympler is written entirely in Python, with no dependencies to external libraries.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Sat Aug 05 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

