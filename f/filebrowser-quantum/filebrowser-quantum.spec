%global _unpackaged_files_terminate_build 1
%global import_path github.com/gtsteffaniak/filebrowser
%global commit_hash 4072e46e4
%global short_name filebrowser

Name: filebrowser-quantum
Version: 1.4.0
Release: alt1
Summary: The best free self-hosted web-based file manager
License: Apache-2.0
Group: System/Servers
Url: https://filebrowserquantum.com
VCS: https://github.com/gtsteffaniak/filebrowser

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: %short_name.service
Source4: %short_name.sysusers
Source5: %short_name.sysconfig

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: esbuild
BuildRequires: rollup-native
BuildRequires: npm

Requires: ffmpeg
Requires: ffprobe

%description
FileBrowser Quantum provides an easy way to access and manage
your files from the web. It has a modern responsive interface
that has many advanced features to manage users, access, sharing,
and file preview and editing.
This version is called "Quantum" because it packs tons of advanced
features into a tiny and easy-to-run file. Unlike the majority of
alternative options, FileBrowser Quantum is simple to install and
easy to configure.

%prep
%setup -a 1 -a 2
ln -sv %_bindir/esbuild frontend
ln -svf %_bindir/rollup frontend/node_modules/.bin/rollup
sed -i "s/0.25.12/$(rpm -q --qf '%{VERSION}' esbuild)/g" frontend/node_modules/esbuild/lib/main.js
sed -i '/port/s/80/8080/' backend/config.yaml

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export ESBUILD_BINARY_PATH=./esbuild

npm --prefix frontend run build

cd backend
%golang_prepare
cd ../.gopath/src/%import_path
go build -o filebrowser --ldflags="\
         -X '%import_path/backend/common/version.CommitSHA=%commit_hash' \
         -X '%import_path/backend/common/version.Version=%version'"

%install
install -Dm 0755 .gopath/src/%import_path/%short_name %buildroot%_bindir/%short_name
install -Dm 0644 backend/config.yaml %buildroot%_sysconfdir/%short_name/config.yaml
install -Dm 0644 %SOURCE3 %buildroot%_unitdir/%short_name.service
install -Dm 0644 %SOURCE4 %buildroot%_sysusersdir/%short_name.conf
install -Dm 0600 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%short_name
mkdir -p %buildroot%_sharedstatedir/%short_name

%pre
%sysusers_create_package %short_name %SOURCE4

%post
%post_service %short_name

%preun
%preun_service %short_name

%files
%_bindir/%short_name
%_sysusersdir/%short_name.conf
%_unitdir/%short_name.service
%config(noreplace) %_sysconfdir/sysconfig/%short_name
%config(noreplace) %_sysconfdir/%short_name/config.yaml
%dir %_sysconfdir/%short_name
%dir %attr(0750, _%short_name, _%short_name) %_sharedstatedir/%short_name

%changelog
* Fri Jun 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.4.0-alt1
- Updated to version 1.4.0.

* Sun May 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.3.3-alt1
- Updated to version 1.3.3.

* Tue Apr 21 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.3.0-alt1
- Initial build for ALT.
