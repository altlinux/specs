%global import_path github.com/coredns/coredns
Name:     coredns
Version:  1.11.1
Release:  alt1

Summary:  CoreDNS is a DNS server that chains plugins
License:  Apache-2.0
Group:    Other
Url:      https://github.com/coredns/coredns

Source:   %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary.

%prep
%setup
%patch -p1

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
%_bindir/coredns
%doc *.md
%_man1dir/*
%_man5dir/*
%_man7dir/*

%changelog
* Sat May 25 2024 Alexander Stepchenko <geochip@altlinux.org> 1.11.1-alt1
- 1.10.1 -> 1.11.1

* Fri Nov 03 2023 Alexander Stepchenko <geochip@altlinux.org> 1.10.1-alt1
- 1.10.0 -> 1.10.1

* Wed Nov 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus
