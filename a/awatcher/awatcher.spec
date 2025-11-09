%global _unpackaged_files_terminate_build 1

Name: awatcher
Version: 0.3.3
Release: alt1
Summary: Activity and idle watchers
License: MPL-2.0
Group: System/Servers
Url: https://github.com/2e3s/awatcher

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel
BuildRequires: libxkbcommon-devel

%description
Awatcher is a window activity and idle watcher
with an optional tray and UI for statistics.

%prep
%setup -a 1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/ActivityWatch/aw-server-rust?rev=656f3c9"]
git = "https://github.com/ActivityWatch/aw-server-rust"
rev = "656f3c9"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-protocols?rev=8e84152"]
git = "https://github.com/pop-os/cosmic-protocols"
rev = "8e84152"
replace-with = "vendored-sources"
EOF

%build
%rust_build --features=default

%install
%rust_install
mkdir -p %buildroot%_userunitdir
cp config/awatcher.service %buildroot%_userunitdir

%files
%_bindir/awatcher
%_userunitdir/awatcher.service
%doc LICENSE

%changelog
* Sun Nov 09 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.3-alt1
- Updated to version 0.3.3.

* Sun Aug 17 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.2-alt1
- Updated to version 0.3.2.

* Wed Jun 18 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.1-alt1
- Initial build for ALT.
