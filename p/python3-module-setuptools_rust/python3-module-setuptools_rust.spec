%define modname setuptools_rust

Name: python3-module-%modname
Version: 0.12.1
Release: alt1

Summary: Setuptools helpers for rust Python extensions.

License: MIT
Group: Development/Python3
Url: https://github.com/PyO3/setuptools-rust

Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildRequires: python3-module-setuptools_scm python3-module-wheel python3-module-toml

%description
Compile and distribute Python extensions written in rust as easily as if they
were written in C.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modname/
%python3_sitelibdir/*.egg-*

%changelog
* Fri Jul 30 2021 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt1
- initial build for Sisyphus

* Mon Feb 8 2021 Vladimir Didenko <cow@altlinux.org> 0.11.6-alt1
- initial build for Sisyphus
