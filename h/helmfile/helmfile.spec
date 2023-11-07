Name: helmfile
Version: 0.158.1
Release: alt1

Summary: Deploy Kubernetes Helm Charts

License: MIT
Group: Development/Tools
Url: https://github.com/helmfile/helmfile

# Source-url: https://github.com/helmfile/helmfile/archive/refs/tags/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
# systemd macro
BuildRequires(pre): rpm-build-compat

ExclusiveArch: %go_arches

#BuildRequires: golang-packaging
BuildRequires: xz
BuildRequires: golang >= 1.19

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
