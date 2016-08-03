Name: seafile-ceph-tools
Version: 0.0
Release: alt1

Summary: Some tools for working with the ceph backend of Seafile

Group: Networking/File transfer
License: MIT
Url: https://github.com/hu-berlin-cms/seafile-ceph-tools

# Source-git: https://github.com/hu-berlin-cms/seafile-ceph-tools.git
Source: %name-%version.tar

BuildArch: noarch

%description
Helper scripts for Seafile using Ceph as storage backend.

seafile-ceph-usage (usage statistics for seafile)
seafile-ceph2fs (Seafile objects ceph -> filesystem)

%prep
%setup

%install
mkdir -p %buildroot/%_bindir/
cp -a seafile-ceph* %buildroot/%_bindir/

%files
%docdir README.md
%_bindir/seafile-ceph*

%changelog
* Thu Aug 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt1
- initial build for ALT Linux Sisyphus
