%global import_path github.com/coredns/coredns
Name:     coredns
Version:  1.10.0
Release:  alt1

Summary:  CoreDNS is a DNS server that chains plugins
License:  Apache-2.0
Group:    Other
Url:      https://github.com/coredns/coredns

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
mkdir -p %buildroot/%_man1dir
install -m 0644 man/core*.1 %buildroot/%_man1dir
mkdir -p %buildroot/%_mandir/man5
install -m 0644 man/core*.5 %buildroot/%_man5dir
mkdir -p %buildroot/%_mandir/man7
install -m 0644 man/core*.7 %buildroot/%_man7dir

export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md
%_man1dir/*
%_man5dir/*
%_man7dir/*

%changelog
* Wed Nov 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus
