%define oname asks

Name: python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: asks - async http

License: MIT
Group: Development/Python3
Url: https://github.com/theelous3/asks

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: pytest3

# generated by 'epm restore --dry-run' from asks/setup.py install_requires
%py3_use h11
# before python 3.6
#py3_use async-generator
%py3_use anyio >= 2.0

%description
asks is an async requests-like HTTP lib, for use in conjunction with the wonderful curio and trio async libs.

asks aims to have a mostly familiar API, using simple functions/methods like get() for getting and post() for posting.
At the heart of asks is a session class which
makes interacting with the web in a sustained and fluid way fast, efficient, and simple.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version 3.0.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.4.12-alt1
- initial build for ALT Sisyphus
