%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: aardvark-dns
Version: 1.9.0
Release: alt1
License: Apache-2.0
Summary: Authoritative DNS server for A/AAAA container records
Group: Development/Other
Url: https://github.com/containers/%name
Vcs: https://github.com/containers/%name
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
%summary.

Forwards other request to configured resolvers.
Read more about configuration in `src/backend/mod.rs`.

%prep
%setup
%patch -p1
mkdir -p .cargo
cat >.cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc README.md
%_libexecdir/podman/%name

%changelog
* Tue Dec 05 2023 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- New version 1.9.0.

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Wed Jul 05 2023 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- New version 1.7.0.

* Mon Apr 17 2023 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- New version 1.6.0.

* Mon Feb 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Tue Jan 10 2023 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Jul 31 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
- Initial build.
