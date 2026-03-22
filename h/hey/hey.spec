%global _unpackaged_files_terminate_build 1
%global import_path github.com/rakyll/hey

Name: hey
Version: 0.1.5
Release: alt1

Summary: HTTP load generator, ApacheBench (ab) replacement
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/rakyll/hey
VCS: https://github.com/rakyll/hey

Source: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
hey is a tiny program that sends some load to a web application.

hey was originally called boom and was influenced from Tarek Ziade's
tool at tarekziade/boom. Using the same name was a mistake as it
resulted in cases where binary name conflicts created confusion. To
preserve the name for its original owner, we renamed this project to
hey.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Sun Mar 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.1.5-alt1
- Initial build for ALT.

