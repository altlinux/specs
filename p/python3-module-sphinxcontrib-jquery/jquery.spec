%def_with check
Name: python3-module-sphinxcontrib-jquery
Version: 4.1
Release: alt3

Summary: jQuery for use in Sphinx themes or extensions
License: 0BSD
URL: https://pypi.org/project/sphinxcontrib-jquery
VCS: https://github.com/sphinx-contrib/jquery
Group: Development/Python3

Source: jquery-%version.tar.gz
# support for Sphinx 7.1
Patch: ed84c0dd67d83ebd542ea855656f4e30a54ba47f.patch
# support for Sphinx 7.2
Patch1: 80d1d3925c17c1860283323972680690f81d7b18.patch
BuildArch: noarch

# Automatically added by buildreq on Sat Mar 25 2023
# optimized out: libgpg-error python3 python3-base python3-dev sh4
BuildRequires: python3-module-flit-core python3-module-pyproject-installer

BuildRequires: rpm-build-python3

%if_with check
BuildRequires: python3-module-sphinx-tests python3-module-pytest
%endif

%description
This package ensures that jQuery is always installed for use in Sphinx
themes or extensions.

%prep
%setup -n jquery-%version
%patch -p1
%patch1 -p1

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
* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 4.1-alt3
- NMU: fixed FTBFS.

* Tue Mar 28 2023 Michael Shigorin <mike@altlinux.org> 4.1-alt2
- NMU:
  + fix build --without check
  + minor spec cleanup

* Sat Mar 25 2023 Fr. Br. George <george@altlinux.org> 4.1-alt1
- Autobuild version bump to 4.1

