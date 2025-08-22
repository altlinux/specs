%define _unpackaged_files_terminate_build 1
%define import_path github.com/nats-io/natscli

Name: natscli
Version: 0.2.4
Release: alt1

Summary: The NATS Command Line Interface
License: Apache-2.0
Group: Networking/Other
Url: https://nats.io/
Vcs: https://github.com/nats-io/natscli

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
A command line utility to interact with and manage NATS.

%prep
%setup -a1
%autopatch -p1

for file in $(find -name "*\[generated\]*"); do
    mv -v "$file" "${file//\[generated\]/}"
done

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd $BUILDDIR/src/$IMPORT_PATH
%golang_build ./nats

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/nats

%changelog
* Fri Aug 22 2025 Artem Krasovskiy <aibure@altlinux.org> 0.2.4-alt1
- New version 0.2.4

* Fri Jun 27 2025 Artem Krasovskiy <aibure@altlinux.org> 0.2.3-alt1
- Initial build

