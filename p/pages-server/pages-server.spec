%define _unpackaged_files_terminate_build 1
%global import_path codeberg.org/Codeberg/pages-server

%define _pseudouser_user _pages
%define _pseudouser_group _pages
%define _pseudouser_home %_localstatedir/%name

Name:       pages-server
Version:    6.2
Release:    alt1

Summary:    The Codeberg Pages Server with custom domain support

License:    EUPL-1.2
Group:      Other
Url:        https://codeberg.page
Vcs:        https://codeberg.org/Codeberg/pages-server.git

Source0:    %name-%version.tar
Source1:    %name.service

Patch:      %name-%version-%release.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires:      rpm-build-golang golang >= 1.23

%description
Codeberg Pages allows you to easily publish static websites with a
human-friendly address ({username}.codeberg.page) via Git on Codeberg.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"                   
export IMPORT_PATH="%import_path"               
export GOPATH="$BUILDDIR:%go_path"    

%golang_prepare
pushd $BUILDDIR/src/%import_path
%gobuild -tags='sqlite sqlite_unlock_notify netgo' -o %name  .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export IMPORT_PATH="%import_path"
%golang_install

mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_pseudouser_home

install -Dm644 %SOURCE1 %buildroot%_unitdir/%name.service
install -m644 example_config.toml %buildroot%_sysconfdir/%name/config.toml

mkdir -p %buildroot%_bindir/
cd .build/src/%import_path
install -p -m755 %name %buildroot%_bindir/%name

%post
%post_systemd_postponed %name.service

%preun
%preun_systemd %name.service

%pre
groupadd -r -f %_pseudouser_user 2>/dev/null ||:
useradd -r -g %_pseudouser_group -M -d %_pseudouser_home -s /dev/null \
  -c 'Codeberg Pages Server' %_pseudouser_user 2>/dev/null ||:

%files
%_bindir/%name
%dir %attr(0770, root, %_pseudouser_group) %_localstatedir/%name
%dir %attr(0750, root, %_pseudouser_group) %_sysconfdir/%name
%config(noreplace) %attr(640, root, %_pseudouser_group) %_sysconfdir/%name/config.toml
%_unitdir/%name.service
%doc *.md LICENSE

%changelog
* Thu Jan 30 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 6.2-alt1
- 6.2 

* Wed Nov 27 2024 Konstantin Kozoriz <kozorizki@altlinux.org> 6.1-alt1
- Initial build.
