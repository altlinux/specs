%define oname icinga2api

Name: python3-module-%oname
Version: 0.6.1
Release: alt1

Summary: Python Icinga 2 API
License: 2-Clause BSD
Group: Development/Python3
Url: https://github.com/tobiasvdk/icinga2api

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel

BuildArch: noarch

%description
icinga2api is a Python module to interact with the Icinga 2 RESTful API.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%python3_sitelibdir/*

%changelog
* Mon Mar 29 2021 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus.
