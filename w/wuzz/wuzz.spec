%global import_path github.com/asciimoo/wuzz

Name: wuzz
Version: 0.5.0
Release: alt1

Summary: Interactive cli tool for HTTP inspection
License: AGPL-3.0
Group: Other
Url: https://%import_path

Packager: Stepan Paksashvili <paksa@altlinux.org>

Source: %name-%version.tar

ExclusiveArch:  %go_arches

BuildRequires(pre): rpm-build-golang

BuildRequires: golang

%description
Interactive cli tool for HTTP inspection.

Wuzz command line arguments are similar to cURL's arguments, so it can be used
to inspect/modify requests copied from the browser's network inspector with the
"copy as cURL" feature.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCE=1
mkdir -p %buildroot{%_bindir,%_sysconfdir/%name}

%golang_install

rm -rf %buildroot%go_root

install -m0644 sample-config.toml %buildroot%_sysconfdir/%name/%name.toml

%pre
%_sbindir/groupadd -r -f %name > /dev/null 2>&1 ||:
%_sbindir/useradd -r -g %name -s /dev/null -c "Wuzz services" %name > /dev/null 2>&1 ||:

%files
%doc LICENSE README.md docs CHANGELOG.md
%config(noreplace) %_sysconfdir/%name/*
%dir %_sysconfdir/%name
%_bindir/wuzz

%changelog
* Fri Mar 17 2023 Stepan Paksashvili <paksa@altlinux.org> 0.5.0-alt1
- Initial build for ALT
