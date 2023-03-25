%def_with check
Name: python3-module-sphinxcontrib-jquery
Version: 4.1
Release: alt1
License: 0BSD
Source: jquery-%version.tar.gz
Group: Development/Python3
BuildArch: noarch
Summary: jQuery for use in Sphinx themes or extensions

# Automatically added by buildreq on Sat Mar 25 2023
# optimized out: libgpg-error python3 python3-base python3-dev sh4
BuildRequires: python3-module-flit-core python3-module-pyproject-installer

%if_with check
BuildRequires: python3-module-sphinx-tests python3-module-pytest
%endif

%description
This package ensures that jQuery is always installed for use in Sphinx
themes or extensions.

%prep
%setup -n jquery-%version

%build
%pyproject_build

%install
%pyproject_install

%if_with check
%check
python3 -m pytest tests
%endif

%files
%python3_sitelibdir_noarch/sphinxcontrib/*
%python3_sitelibdir_noarch/sphinxcontrib_*

%changelog
* Sat Mar 25 2023 Fr. Br. George <george@altlinux.org> 4.1-alt1
- Autobuild version bump to 4.1

