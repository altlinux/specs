%define pypi_name feedgenerator

Name: python3-module-feedgenerator
Version: 2.1.0
Release: alt1.1

Summary: Standalone version of Django's feedgenerator module
License: BSD
Group: Development/Python
URL: https://pypi.org/project/feedgenerator
VCS: https://github.com/getpelican/feedgenerator

# https://github.com/getpelican/feedgenerator/archive/refs/tags/2.1.0.tar.gz
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytz

Requires: python3-module-pytz

%description
FeedGenerator is a standalone version of Django's feedgenerator module.
It has evolved over time, including an update for Py3K and numerous other
enhancements.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Sat Oct 26 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.1
- NMU:
  + fixed FTBFS.
  + Moved on modern pyproject macros.
  + Cleaned up spec a little bit.

* Sat Apr 13 2024 Alexey Appolonov <alexey@altlinux.org> 2.1.0-alt1
- Python 3.6 is no longer supported;
- Description field are used as subtitle for Atom feeds, if provided;
- Preliminary support for adding images to feeds;
- Fixed double subtitles when both description & subtitle are provided;
- Modernized and improved tests.

* Tue May 04 2019 Alexey Appolonov <alexey@altlinux.org> 1.9-alt1
- Initial ALT Linux release.
