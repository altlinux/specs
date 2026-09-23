%define _unpackaged_files_terminate_build 1
%def_with check

Name: gerbil
Version: 1.5.2
Release: alt1

Summary: A simple WireGuard interface management server for Pangolin
License: AGPL-3.0
Group: Networking/Other
VCS: https://github.com/fosrl/gerbil
Url: https://docs.pangolin.net

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
Gerbil is a  simple WireGuard interface management server written  in Go. Gerbil
makes it  easy to create  WireGuard interfaces as well  as add and  remove peers
with an HTTP API.

%prep
%setup -a1
%patch0 -p1

%build
%gobuild -o ./gerbil

%install
install -vDm 755 ./gerbil \
        %buildroot/%_bindir/gerbil

%check
%gotest ./...

%files
%doc README.md docs/observability.md
%_bindir/gerbil

%changelog
* Wed Sep 23 2026 Egor Ignatov <egori@altlinux.org> 1.5.2-alt1
- New version 1.5.2.

* Thu Sep 17 2026 Egor Ignatov <egori@altlinux.org> 1.5.1-alt1
- First build for ALT.
