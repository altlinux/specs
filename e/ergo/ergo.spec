%global import_path github.com/ergochat/ergo
%global _unpackaged_files_terminate_build 1
%global commit d25fc2a758c3d355017a39f9676def2f74c0baa3

Name:    ergo
Version: 2.14.0
Release: alt1

Summary: A modern IRC server (daemon/ircd) written in Go
License: MIT
Group:   Development/Other
Url:     https://github.com/ergochat/ergo

Source: %name-%version.tar
Source2: %name.service

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.23.0
BuildRequires: /proc

%description
Ergo (formerly known as Oragono) is a modern IRCD
(IRC server software) written in Go.

%prep
%setup

sed -i -e 's|path: languages|path: %_localstatedir/%name/languages|g' default.yaml

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X main.version=v%version -X main.commit=%commit"

%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
mkdir -p %buildroot%_localstatedir/%name/languages
install -Dm 0644 languages/*.lang.json %buildroot%_localstatedir/%name/languages/
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm 0640 default.yaml %buildroot%_sysconfdir/%name/ircd.yaml

%pre
groupadd -r -f _%name 2>/dev/null ||:
useradd -r -g _%name -c 'Ergo daemon' \
        -s /bin/bash  -d %_localstatedir/%name _%name 2>/dev/null ||:

%files
%doc README.md DEVELOPING.md CHANGELOG.md
%_bindir/%name
%dir %attr(0750,_%name,_%name) %_localstatedir/%name
%dir %attr(0750,_%name,_%name) %_localstatedir/%name/languages
%_localstatedir/%name/languages/*
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/ircd.yaml
%_unitdir/%name.service

%changelog
* Wed Dec 25 2024 Nadezhda Fedorova <fedor@altlinux.org> 2.14.0-alt1
- Initial build for ALTLinux.
