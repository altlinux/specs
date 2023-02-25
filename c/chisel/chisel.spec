%global import_path github.com/jpillora/chisel
%def_without check

Name: chisel
Version: 1.8.1
Release: alt1

Summary: TCP tunnel over HTTP

License: MIT
Group: Networking/Other
Url: https://github.com/jpillora/chisel

# Source-url: https://github.com/jpillora/chisel/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
# ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar


BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
A fast TCP tunnel over HTTP.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
#gocheck

%files
%doc example README.md
%_bindir/%name

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Mon Feb 14 2022 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version 1.7.7 (with rpmrb script)

* Sat Sep 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt1
- initial build for ALT Sisyphus

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.6-1
- Update to latest upstream release 1.7.6 (#1930557)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.4-1
- Update to latest upstream release 1.7.4 (#1916086)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.3-1
- Update to latest upstream release 1.7.3 (#1898460)

* Sun Oct 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.2-1
- Update ot latest upstream release 1.7.2 (#1889172)

* Mon Sep 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.1-1
- Update ot latest upstream release 1.7.1 (#1880651)

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Update ot latest upstream release 1.7.0 (#1880651)

* Fri Sep 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Update ot latest upstream release 1.6.0

* Fri Jul 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update ot latest upstream release 1.5.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Initial package for Fedora
