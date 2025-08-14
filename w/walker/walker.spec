%global _unpackaged_files_terminate_build 1

Name: walker
Version: 0.13.26
Release: alt1
Summary: Multi-Purpose Launcher with a lot of features
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/abenz1267/walker

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: libgtk4-devel
BuildRequires: libgtk4-layer-shell-devel
BuildRequires: libgirepository1.0-devel
BuildRequires: libvips-devel

%description
Walker is a highly extendable application launcher
that doesn't hold back on features and usability.
Fast. Unclutters your brain. Improves your workflow.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
%setup -a 1

%build
cd cmd && go build -x -o walker

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_sysconfdir/xdg/walker
install -m 0755 cmd/walker %buildroot%_bindir/walker
install -m 0644 internal/config/config.default.toml \
                %buildroot%_sysconfdir/xdg/walker/config.toml

%files
%_bindir/walker
%_sysconfdir/xdg/walker
%doc LICENSE

%changelog
* Wed Aug 13 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.13.26-alt1
- Updated to version 0.13.26.

* Tue Aug 12 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.13.25-alt1
- Initial build for ALT.
