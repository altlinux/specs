%define pypi_name cinemagoer

Name: python3-module-%pypi_name
Version: 2022.11.22
Release: alt1
Summary: Retrieve and manage the data of the IMDb movie database
Group: Development/Python
License: GPLv2+
Url: https://cinemagoer.github.io/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: python3-module-%pypi_name-%version.tar

BuildArch: noarch
%add_python3_lib_path %python3_sitelibdir/imdb/locale
BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-dev python3-module-polib
BuildRequires: python3-module-setuptools python3-tools

%description -n python3-module-%pypi_name
IMDbPY is a Python package useful to retrieve and manage the data of
the IMDb movie database about movies, people, characters and companies.

This is the Python 3 build of %pypi_name.

%prep
%setup %setup -n python3-module-%pypi_name-%version

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

%build
%python3_build

%install
%python3_install

%files
%_bindir/imdbpy
%_bindir/*.py
%python3_sitelibdir/imdb/
%python3_sitelibdir/%pypi_name-%version-py*.egg-info


%changelog
* Fri Nov 25 2022 Artyom Bystrov <arbars@altlinux.org> 2022.11.22-alt1
- initial build for ALT Sisyphus

