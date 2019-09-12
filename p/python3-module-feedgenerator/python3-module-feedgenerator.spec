%define pypi_name feedgenerator
%define commit 78b5100f8d9594afb2df9038e01ecc43ecb4abae
%define shortcommit %(c=%{commit}; echo ${c:0:7})

Name: python3-module-feedgenerator
Version: 1.9
Release: alt1

Summary: Standalone version of Django's feedgenerator module
License: BSD
Group: Development/Python
URL: https://github.com/getpelican/%{pypi_name}

# https://github.com/getpelican/%{pypi_name}/archive/%{commit}/%{pypi_name}-%{shortcommit}.tar.gz
Source0: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-pytz

Requires: python3-module-six
Requires: python3-module-pytz

%description
FeedGenerator is a standalone version of Django's feedgenerator module.
It has evolved over time, including an update for Py3K and numerous other
enhancements.

%prep
%setup
rm -rf .tox
rm -rf feedgenerator.egg-info
rm -rf feedgenerator/django/utils/six.py

for f in feedgenerator/django/utils/*py;
do
    sed -i -e 's/from . import six/import six/' -e 's/from .six \(import .*$\)/from six \1/'  $f
done

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
* Tue May 04 2019 Alexey Appolonov <alexey@altlinux.org> 1.9-alt1
- Initial ALT Linux release.
