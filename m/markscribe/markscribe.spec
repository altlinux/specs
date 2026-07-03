%define _unpackage_files_terminate_build 1
%global import_path github.com/muesli/marscribe

Name: markscribe
Version: 0.6.0
Release: alt1

Summary: Your personal markdown scribe
License: MIT
Group: Text tools
URL: https://github.com/muesli/markscribe
VCS: https://github.com/muesli/markscribe

Source: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary with template-engine and Git(Hub) & RSS powers.

%prep
%setup -q -a 1

%build
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
go build -x -o %name

%install
install -Dm 0755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc LICENSE

%changelog
* Thu Jul 02 2026 Vladislav Eliseev <general@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.
