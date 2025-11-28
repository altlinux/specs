%define _unpackage_files_terminate_build 1
%global import_path github.com/ostafen/digler
# git rev-parse --short 0.1.0-alt1
%global commit_hash 48d6c75

Name: digler
Version: 0.1.0
Release: alt1

Summary: Digler - Go Deep. Get Back Your Data
License: MIT
Group: File tools
URL: https://github.com/ostafen/digler

Source: %name-%version.tar
Source1: vendor.tar
Patch1: alt-fix-appname.patch
Patch2: alt-fix-completions.patch

ExcludeArch: i586
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Digler is a tool for forensic disk analysis and file recovery. It's
designed to help you unearth lost or deleted data from various disk
images and raw devices.

%prep
%setup -a 1
%patch1 -p1
%patch2 -p1

%build
cd cmd && go build -x -o digler
./digler completion bash > %name.bash
./digler completion zsh > _%name
./digler completion fish > %name.fish

%install
mkdir -p %buildroot%_bindir

mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d

install -m 0755 cmd/%name %buildroot%_bindir/%name

install -m 0644 cmd/%name.bash %buildroot%_datadir/bash-completion/completions/%name.bash
install -m 0644 cmd/_%name %buildroot%_datadir/zsh/site-functions/_%name
install -m 0644 cmd/%name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%doc LICENSE
%_datadir/bash-completion/completions/%name.bash
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Fri Sep 19 2025 Vladislav Eliseev <general@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
