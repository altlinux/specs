%define _unpackaged_files_terminate_build 1
%define import_path github.com/openbao/openbao

Name: openbao
Version: 2.5.2
Release: alt1

Summary: Secure secrets and encryption management system
License: MPL-2.0
Group: Development/Other
Url: https://openbao.org/
Vcs: https://github.com/openbao/openbao

Source0: %name-%version.tar
Source1: vendor.tar
Source2: web-ui-assets.tar
Source3: %name.hcl

Patch: %name-%version-alt.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

%description
OpenBao is an open-source secrets management platform designed to securely
store, manage, and distribute sensitive data such as API keys, certificates,
and credentials. It provides centralized control over secrets with encryption,
dynamic secret generation, and detailed audit logging.

%prep
%setup -a1 -a2
%autopatch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export BUILD_TAGS="openbao ui"
export TAGS="${BUILD_TAGS}"
export LDFLAGS="-X github.com/%name/%name/version.fullVersion=%version
-X github.com/%name/%name/version.GitCommit=%version-%release
-X github.com/%name/%name/version.BuildDate=$(date -u +'%%Y-%%m-%%d')"

%golang_prepare
cd .build/src/%import_path

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

mkdir -p %buildroot%_sysconfdir/%name.d/tls
mkdir -p %buildroot%_localstatedir/%name/data

install -Dm755 $BUILDDIR/bin/openbao "%buildroot%_bindir/bao"
install -p -D -m 644 \
	.release/linux/package/usr/lib/systemd/system/%name.service \
	%buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/%name.d/%name.hcl
install -p -D -m 644 .release/linux/package/etc/%name/%name.env \
	%buildroot%_sysconfdir/%name/%name.env

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -d %_localstatedir/%name -s /sbin/nologin \
    -c "Openbao" %name >/dev/null 2>&1 ||:

%post
%post_systemd %name

%preun
%preun_systemd %name
%postun
%systemd_postun_with_restart %name

%files
%_bindir/bao
%doc LICENSE README.md
%_unitdir/%name.service
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name.d
%dir %_sysconfdir/%name.d/tls
%dir %attr(0700, %name, %name) %_localstatedir/%name
%dir %attr(0700, %name, %name) %_localstatedir/%name/data
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name.d/%name.hcl
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.env

%changelog
* Wed Apr 01 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.2-alt1
- Updated to new version v2.5.2.

* Wed Mar 25 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.1-alt2
- Fixed LDFLAGS to set correct version information (Closes: #58272).

* Tue Feb 24 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.1-alt1
- Updated to new version v2.5.1.
- Added openbao.env configuration file.

* Wed Jan 21 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.4.4-alt2
- Added systemd service file support.

* Mon Dec 29 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.4.4-alt1
- Updated to new version v2.4.4.
- Support building package with bundled web ui (Closes: #56797).

* Sun Jun 08 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.
