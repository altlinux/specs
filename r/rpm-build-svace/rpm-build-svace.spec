Name: rpm-build-svace
Version: 5.0.260306
Release: alt1

Summary: Downloads and installs svace static analyzer to /opt
License: GPL-2.0-or-later
Group: Development/Other
BuildArch: noarch

Source0: download-svace.sh
Source1: install-svace.sh
Source2: checksums.sha256

%description
RPM package that downloads and installs the svace static analyzer
into /opt during package installation.

Requires network access during installation to download svace from
nextcloud.ispras.ru.

Version can be pinned by writing a version string (e.g. 4.0.250829)
to /etc/rpm-build-svace-version. The file is pre-populated with the package's
svace version and updated on package upgrade (unless manually changed).

If %%post fails (e.g. network unavailable), svace is not installed.
Re-run /usr/libexec/rpm-build-svace/install-svace.sh manually.

%install
install -Dm755 %{SOURCE0} %buildroot/usr/libexec/rpm-build-svace/download-svace.sh
install -Dm755 %{SOURCE1} %buildroot/usr/libexec/rpm-build-svace/install-svace.sh
install -Dm644 %{SOURCE2} %buildroot/usr/libexec/rpm-build-svace/checksums.sha256
install -d %buildroot%_sysconfdir
echo "%version" > %buildroot%_sysconfdir/rpm-build-svace-version

%post
if [ ! -s %_sysconfdir/pki/ca-trust/extracted/pem/tls-ca-bundle.pem ]; then
    update-ca-trust ||:
fi
/usr/libexec/rpm-build-svace/install-svace.sh --verbose ||:

%files
%dir /usr/libexec/rpm-build-svace
/usr/libexec/rpm-build-svace/download-svace.sh
/usr/libexec/rpm-build-svace/install-svace.sh
/usr/libexec/rpm-build-svace/checksums.sha256
%config(noreplace) %_sysconfdir/rpm-build-svace-version

%changelog
* Fri Mar 27 2026 Egor Ignatov <egori@altlinux.org> 5.0.260306-alt1
- Initial build for Sisyphus.
