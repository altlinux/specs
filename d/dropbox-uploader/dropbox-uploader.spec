Name: dropbox-uploader
Version: 0.15
Release: alt1

Summary: A bash script to manage Dropbox from the CLI
License: GPLv3
Group: Networking/File transfer
URL: https://github.com/andreafabrizi/Dropbox-Uploader
Packager: Mikhail Kolchin <mvk@altlinux.org>
BuildArch: noarch

Source: Dropbox-Uploader-%version.tar.gz

Requires: curl

%description
Dropbox Uploader is a BASH script which can be used to upload,
download, list or delete files from Dropbox, an online file sharing,
synchronization and backup service.

%prep
%setup -n Dropbox-Uploader-%version

sed -i 's/dropbox_uploader.sh/dropbox_uploader/' dropShell.sh

%install
install -D -m 0755 dropbox_uploader.sh %buildroot%_bindir/dropbox_uploader
install -D -m 0755 dropShell.sh %buildroot%_bindir/dropShell

%files
%doc CHANGELOG.md README.md
%_bindir/*

%changelog
* Tue Jun 30 2015 Mikhail Kolchin <mvk@altlinux.org> 0.15-alt1
- initial build for ALT Linux Sisyphus
