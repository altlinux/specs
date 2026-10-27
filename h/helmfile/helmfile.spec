Name: helmfile
Version: 1.8.2
Release: alt1

Summary: Deploy Kubernetes Helm Charts

License: MIT
Group: Development/Tools
Url: https://github.com/helmfile/helmfile

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/helmfile/helmfile/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
# systemd macro
BuildRequires(pre): rpm-build-compat

ExclusiveArch: %go_arches

#BuildRequires: golang-packaging
BuildRequires: xz
BuildRequires: golang >= 1.27.1

Requires: helm >= 3.11.1

%description
Helmfile is a declarative spec for deploying helm charts. It lets you...

 * Keep a directory of chart value files and maintain changes in version control.
 * Apply CI/CD to configuration changes.
 * Periodically sync to avoid skew in environments.

To avoid upgrades for each iteration of helm, the helmfile executable
delegates to helm - as a result, helm must be installed.

%prep
%setup -a1

%build
#modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%_sourcedir/%name.changes")"
#SOURCE_DATE_EPOCH=$(date -u -d "${modified}" "+%s")
#export SOURCE_DATE_EPOCH
#rm -f source_date_epoch
#echo SOURCE_DATE_EPOCH=$SOURCE_DATE_EPOCH > source_date_epoch
go build -mod=vendor -buildmode=pie

%install
#. ./source_date_epoch
#export SOURCE_DATE_EPOCH
make TAG=v%version install
mkdir -p %buildroot%_bindir
install -m755 ${HOME}/go/bin/helmfile %buildroot/%_bindir/helmfile

%files
%doc README.md
%_bindir/helmfile

%changelog
* Tue Oct 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2

* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1
- security fixes:
  + CVE-2026-56854: fix source-address critical option bypass in golang.org/x/crypto/ssh.
  + CVE-2026-56852: fix infinite loop on invalid input in golang.org/x/text.
  + CVE-2026-84303, GHSA-qc2q-p7wx-3px3: fix xDS RBAC header matching bypass in grpc-go.
  + CVE-2026-84304, GHSA-vp52-pcj8-j9qc: fix OOM via HTTP/2 DATA frame fragmentation in grpc-go.
  + CVE-2026-84445, GHSA-2v4p-qf9q-27wj: fix server panic on missing authority/Host in grpc-go.
  + GHSA-hrxh-6v49-42gf: fix xDS RBAC and HTTP/2 transport vulnerabilities in grpc-go.
  + CVE-2026-85732, GHSA-h7vf-4x9w-h99v: fix blind SSRF via pagination Link header in oras-go.
  + CVE-2026-81870, GHSA-8wmf-6v46-5gfg: fix endpoint URL leak in exporter logs in opentelemetry-go sdk.

* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0

* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1

* Sun Feb 16 2025 Vitaly Lipatov <lav@altlinux.ru> 0.171.0-alt1
- new version 0.171.0 (with rpmrb script)

* Sat Jan 25 2025 Vitaly Lipatov <lav@altlinux.ru> 0.170.1-alt1
- new version 0.170.1 (with rpmrb script)

* Mon Dec 09 2024 Vitaly Lipatov <lav@altlinux.ru> 0.169.2-alt1
- new version 0.169.2 (with rpmrb script)

* Mon Dec 02 2024 Vitaly Lipatov <lav@altlinux.ru> 0.169.1-alt1
- new version 0.169.1 (with rpmrb script)

* Wed Feb 28 2024 Vitaly Lipatov <lav@altlinux.ru> 0.162.0-alt1
- new version 0.162.0 (with rpmrb script)

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 0.159.0-alt1
- new version 0.159.0 (with rpmrb script)

* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 0.158.1-alt1
- new version 0.158.1 (with rpmrb script)

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 0.157.0-alt1
- new version 0.157.0 (with rpmrb script)

* Tue Aug 01 2023 Vitaly Lipatov <lav@altlinux.ru> 0.155.1-alt1
- new version 0.155.1 (with rpmrb script)

* Tue May 30 2023 Vitaly Lipatov <lav@altlinux.ru> 0.154.0-alt1
- new version 0.154.0 (with rpmrb script)

* Mon May 08 2023 Vitaly Lipatov <lav@altlinux.ru> 0.153.1-alt1
- new version 0.153.1 (with rpmrb script)

* Mon May 08 2023 Vitaly Lipatov <lav@altlinux.ru> 0.150.0-alt1
- initial build for ALT Sisyphus (thanks, OpenSUSE!)
