%define pypi_name feedgenerator

Name: python3-module-feedgenerator
Version: 2.1.0
Release: alt1

Summary: Standalone version of Django's feedgenerator module
License: BSD
Group: Development/Python
URL: https://github.com/getpelican/feedgenerator

# https://github.com/getpelican/feedgenerator/archive/refs/tags/2.1.0.tar.gz
Source0: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
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
rm -rf .tox
rm -rf %{pypi_name}.egg-info
rm -rf %{pypi_name}/django/utils/six.py

%build
%python3_build

%install
%python3_install

%check
%{__python3} setup.py test

%files
%doc LICENSE README.rst
%{python3_sitelibdir_noarch}/*

%changelog
* Sat Apr 13 2024 Alexey Appolonov <alexey@altlinux.org> 2.1.0-alt1
- Python 3.6 is no longer supported;
- Description field are used as subtitle for Atom feeds, if provided;
- Preliminary support for adding images to feeds;
- Fixed double subtitles when both description & subtitle are provided;
- Modernized and improved tests.

* Tue May 04 2019 Alexey Appolonov <alexey@altlinux.org> 1.9-alt1
- Initial ALT Linux release.
