%define _unpackaged_files_terminate_build 1

%define import_path github.com/BurntSushi/toml-test

Name: golang-github-burntsushi-toml-test
Version: 1.1.0
Release: alt2

Summary: Language agnostic test suite for TOML
License: MIT
Group: Development/Other
Url: https://github.com/BurntSushi/toml-test.git

Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-golang

Provides: toml-test = %EVR

%description
toml-test is a higher-order program that tests other TOML decoders or
encoders. Tests are divided into two groups: invalid TOML data and valid TOML
data. Decoders that reject invalid TOML data pass invalid TOML tests. Decoders
that accept valid TOML data and output precisely what is expected pass valid
tests.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/toml-test

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_datadir/toml-test
cp -a tests %buildroot%_datadir/toml-test/

%files
%doc COPYING README.md
%_bindir/toml-test
%_datadir/toml-test/

%changelog
* Wed Mar 16 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt2
- Fixed FTBFS (dropped extra build dep on removed burntsushi-toml).

* Tue Feb 01 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 0.2.0 -> 1.1.0.

* Wed Apr 07 2021 Leontiy Volodin <lvol@altlinux.org> 0.2.0-alt4.git9767d20
- Updated to the latest git snapshot.
- Fixed build with golang 1.16.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.2.0-alt3.git39bb76d
- Restored for Sisyphus.

* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2.git39bb76d
- Updated to the latest git snapshot (need for python-toml).

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_0.13.git85f50d0
- fc update

* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_0.12.git85f50d0
- new version

