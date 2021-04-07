%global import_path github.com/go-bindata/go-bindata

%global _unpackaged_files_terminate_build 1

Name: go-bindata
Version: 3.1.3
Release: alt1
Summary: A small utility which generates Go code from any file
Group: Development/Other
License: CC0-1.0
Url: https://github.com/go-bindata/go-bindata.git
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
%summary

This tool converts any file into managable Go source code. Useful for
embedding binary data into a go program. The file data is optionally gzip
compressed before being converted to a raw byte slice.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare
pushd $BUILDDIR/src/%import_path
go install ./...
popd

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.md
%_bindir/go-bindata

%changelog
* Thu Apr 08 2021 Alexey Shabalin <shaba@altlinux.org> 3.1.3-alt1
- 3.1.3
- Build from gear.

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.7-alt2_14.gita0ff256
- update to new release by fcimport

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 3.0.7-alt2_11.gita0ff256
- NMU: rebuild for aarch64

* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.7-alt1_11.gita0ff256
- new version

