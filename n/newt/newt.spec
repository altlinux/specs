%define _unpackaged_files_terminate_build 1
%def_with check

Name: newt
Version: 1.17.0
Release: alt1

Summary: Tunneled network connector for Pangolin
License: AGPL-3.0
Group: Networking/Other
VCS: https://github.com/fosrl/newt
Url: https://docs.pangolin.net

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
Newt is a  fully user space WireGuard tunnel client  and TCP/UDP proxy, designed
to securely expose private resources controlled  by Pangolin. By using Newt, you
don't need to manage complex WireGuard tunnels and NATing.

%prep
%setup -a1
%patch0 -p1

%build
LDFLAGS="$LDFLAGS -X main.newtPlatform=$(go env GOOS)_$(go env GOARCH)"
%gobuild -o ./bin/newt

%install
install -vDm 755 ./bin/newt \
        %buildroot/%_bindir/newt

%check
%gotest ./...

%files
%doc README.md
%_bindir/newt

%changelog
* Thu Sep 17 2026 Egor Ignatov <egori@altlinux.org> 1.17.0-alt1
- First build for ALT.
