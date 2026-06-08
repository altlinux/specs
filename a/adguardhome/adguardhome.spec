%global _unpackaged_files_terminate_build 1
%global import_path github.com/AdguardTeam/AdGuardHome

Name: adguardhome
Version: 0.108.0.b.88
Release: alt1
Summary: Network-wide ads & trackers blocking DNS server
License: GPL-3.0
Group: System/Servers
Url: https://adguard.com/ru/adguard-home/overview.html
VCS: https://github.com/AdguardTeam/AdGuardHome

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: .twosky.json
Source4: %name.service
Patch: alt-drop-unused-import.patch

# idle time limit exceeded
ExcludeArch: i586

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: npm
BuildRequires: node-cross-env
BuildRequires: node-cross-spawn

%description
Free and open source, powerful network-wide ads & trackers blocking DNS server.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
# npm --prefix client ci
# git add client/node_modules -f && git commit -m "Updated node modules."
%setup -a 1 -a 2
# %patch -p1

%build
export GO111MODULE=on
export GOTOOLCHAIN=local
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export NODE_OPTIONS=--openssl-legacy-provider

# build web
cp %SOURCE3 $PWD
npm --prefix client run build-prod

# build bin
%golang_prepare
cd .gopath/src/%import_path
go build --ldflags "\
         -X %import_path/internal/version.version=%(echo %version | sed 's/\.b/-b/') \
         -X %import_path/internal/version.channel=release" \
         -o=%name

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_sysconfdir \
         %buildroot%_localstatedir/%name
install -m 0755 .gopath/src/%import_path/%name %buildroot%_bindir/%name
install -m 0644 %SOURCE4 %buildroot%_unitdir/%name.service
touch %buildroot%_sysconfdir/%name.yaml

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_localstatedir/%name
%_unitdir/%name.service
%ghost %config(noreplace) %_sysconfdir/%name.yaml

%changelog
* Mon Jun 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0.b.88-alt1
- Updated to version 0.108.0.b.88.

* Sun May 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0.b.85-alt1
- Updated to version 0.108.0.b.85.

* Sun Mar 22 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0.b.83-alt1
- Updated to version 0.108.0.b.83.

* Mon Feb 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0.b.82-alt2
- Fixed internal version of server.

* Mon Feb 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0.b.82-alt1
- Updated to version 0.108.0.b.82.

* Sat Dec 06 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta80
- Updated to version 0.108.0-b.80.

* Sun Nov 23 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta79
- Updated to version 0.108.0-b.79.

* Sun Nov 02 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta78
- Updated to version 0.108.0-b.78.

* Sun Oct 12 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta77
- Updated to version 0.108.0-b.77.

* Thu Aug 14 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta74
- Updated to version 0.108.0-b.74.
- Excluded i586 arch (idle time limit exceeded).

* Wed May 07 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta69
- Updated to version 0.108.0-b.69.

* Fri Apr 25 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta68
- Updated to version 0.108.0-b.68.

* Tue Mar 11 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta64
- Updated to version 0.108.0-b.64.

* Mon Nov 18 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.108.0-alt1.beta60
- Updated to beta version 0.108.0-b.60 (Fixes: CVE-2022-32175).

* Sat Nov 02 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.53-alt1
- Updated to version 0.107.53.

* Sat Sep 28 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.52-alt1
- Updated to version 0.107.52.

* Fri Jun 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.51-alt1
- Updated to version 0.107.51.

* Wed May 29 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.107.50-alt1
- Updated to version 0.107.50.

* Thu May 23 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.107.49-alt1
- Updated to version 0.107.49.

* Fri May 17 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.107.48-alt1
- Updated to version 0.107.48.

* Wed Mar 06 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.45-alt1
- Updated to version 0.107.45.

* Wed Feb 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.44-alt1
- Updated to version 0.107.44.
- Fixed version show.

* Sun Feb 04 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.43-alt1
- Initial build for ALT.
