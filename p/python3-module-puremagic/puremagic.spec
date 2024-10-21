%define pypi_name puremagic

%def_with check

Name:    python3-module-%pypi_name
Version: 1.28
Release: alt1

Summary: Pure python implementation of identifying files based off their magic numbers

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/puremagic
VCS:     https://github.com/cdgriffith/puremagic

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
puremagic is a pure python module that will identify a file based off it's
magic numbers.

It is designed to be minimalistic and inherently cross platform compatible.
It is also designed to be a stand in for python-magic, it incorporates
the functions from_file(filename[, mime]) and from_string(string[, mime])
however the magic_file() and magic_string() are more powerful and will also
display confidence and duplicate matches.

It does NOT try to match files off non-magic string. In other words it will not
search for a string within a certain window of bytes like others might.

Advantages over using a wrapper for 'file' or 'libmagic':
* Faster
* Lightweight
* Cross platform compatible
* No dependencies

Disadvantages:
* Does not have as many file types
* No multilingual comments
* Duplications due to small or reused magic numbers

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 21 2024 Grigory Ustinov <grenka@altlinux.org> 1.28-alt1
- Initial build for Sisyphus.
