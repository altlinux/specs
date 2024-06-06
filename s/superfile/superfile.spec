%define _unpackaged_files_terminate_build 1
%global import_path github.com/MHNightCat/superfile

Name: superfile
Version: 1.1.3
Release: alt2

Summary: Pretty fancy and modern terminal file manager
License: MIT
Group: File tools
Url: https://terminaltrove.com/superfile/
VCS: https://github.com/MHNightCat/superfile
Source: %name-%version.tar
Source1: vendor.tar
Patch1: alt-disabled-checking-upstream-version.patch

BuildRequires: rpm-build-golang
BuildRequires: golang

%description
superfile features a clipboard viewer, processes list, a detailed
display of metadata attributes associated with a file, themes, custom
fonts and the navigation and management of files without leaving the terminal.

%description -l ru_RU.UTF-8
В superfile есть средство просмотра буфера обмена, список процессов,
подробное отображение атрибутов метаданных, связанных с файлом, темы,
пользовательские шрифты, навигация и управление файлами, не выходя из терминала.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
%setup -a 1
%patch1 -p1

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
go build --ldflags "-w \
         -X main.Version=%version" \
         --race=0 --tags= --trimpath -o=%name -v=0 -x=0

%install
mkdir -p %buildroot%_bindir
install -m 0755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%doc README.md LICENSE changelog.md

%changelog
* Thu Jun 06 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.1.3-alt2
- Disable comparison of release with upstream version.

* Thu Jun 06 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.1.3-alt1
- Updated to version 1.1.3.

* Tue May 14 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.1.2-alt1
- Initial build for ALT.
