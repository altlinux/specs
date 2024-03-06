%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name grapheme

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: A Python package for working with user perceived characters
License: MIT
Group: Development/Python
Url: https://pypi.org/project/grapheme/
Vcs: https://github.com/alvinlindstam/grapheme

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Unicode strings are made up of a series of unicode characters,
but a unicode character does not always map to a user perceived character.
Some human perceived characters are represented as two
or more unicode characters.

However, all built in python string functions and string methods
work with single unicode characters without considering their
connection to each other.
This library implements the unicode default rules for extended
grapheme clusters, and provides a set of functions for
string manipulation based on graphemes.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Feb 29 2024 Alexander Kuznetov <kuznetsovam@altlinux.ru> 0.6.0-alt1
- Initial build.
