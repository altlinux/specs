Name: python3-module-intervaltree
Version: 3.0.2
Release: alt1

License: MIT
Group: Development/Python
Url: https://github.com/chaimleib/intervaltree

Summary: A mutable, self-balancing interval tree. Queries may be by point, by range overlap, or by range containment

# Source-url: https://github.com/chaimleib/intervaltree/archive/%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

%description
A mutable, self-balancing interval tree.
Queries may be by point, by range overlap, or by range containment.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- initial build for ALT Sisyphus
