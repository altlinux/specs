Name: rpm-build-svace
Version: 5.0.260414
Release: alt1

Summary: Downloads and installs svace static analyzer to /opt
License: GPL-2.0-or-later
Group: Development/Other
BuildArch: noarch
BuildRequires: jq

Source0: %name-%version.tar

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

%prep
%setup

%build
jq -r '
  [ .[] |
    (.version | gsub(" *\\(.*\\)"; "")) as $ver |
    select(.distros.linux // "" | startswith("https://nextcloud.ispras.ru/")) |
    {version: $ver, url: .distros.linux}
  ] |
  reduce .[] as $item ([]; if [.[] | .version] | index($item.version) | not then . + [$item] else . end) |
  .[] |
  "\(.version) \(.url)"
' releases.json > releases.txt

%install
install -Dm755 altlinux/download-svace.sh %buildroot/usr/libexec/rpm-build-svace/download-svace.sh
install -Dm755 altlinux/install-svace.sh %buildroot/usr/libexec/rpm-build-svace/install-svace.sh
install -Dm644 ./checksums.sha256 %buildroot/usr/libexec/rpm-build-svace/checksums.sha256
install -Dm644 ./releases.txt %buildroot/usr/libexec/rpm-build-svace/releases.txt
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
/usr/libexec/rpm-build-svace/releases.txt
%config(noreplace) %_sysconfdir/rpm-build-svace-version

%changelog
* Fri Apr 24 2026 Egor Ignatov <egori@altlinux.org> 5.0.260414-alt1
- Update to 5.0.260414

* Fri Mar 27 2026 Egor Ignatov <egori@altlinux.org> 5.0.260306-alt1
- Initial build for Sisyphus.
