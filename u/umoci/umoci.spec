%global import_path github.com/opencontainers/umoci
Name:    umoci
Version: 0.5.1
Release: alt1

Summary: umoci modifies Open Container images
License: Apache-2.0
Group:   Other
Url:     https://umo.ci
Vcs:     https://github.com/opencontainers/umoci

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man

%description
umoci is a reference implementation of the OCI image specification and provides
users with the ability to create, manipulate, and otherwise interact with
container images. It is designed to be as small and unopinonated as possible,
so as to act as a foundation for larger systems to be built on top of.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="${LDFLAGS:-} -X %import_path.version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name
cd -

cd doc/man
for file in *.1.md; do
    go-md2man -in "$file" -out "${file%%.md}"
done


%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

for file in doc/man/*.1; do
    install -Dm 0644 "$file" "%buildroot/%_man1dir/$(basename "$file")"
done

%files
%doc *.md
%_man1dir/*
%_bindir/*

%changelog
* Mon Sep 08 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.1-alt1
- new version 0.5.1

* Thu Jun 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
