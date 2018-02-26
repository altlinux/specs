%define pear_name VFS

Name: pear-VFS
Version: 0.2.0
Release: alt1

Summary: Virtual File System API

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

Requires: pear-core >= 1.4.0b1

%description
This package provides a Virtual File System API, with backends for:

* SQL
* FTP
* Local filesystems
* Hybrid SQL and filesystem
* Samba
* SSH2/SFTP

Reading, writing and listing of files are all supported, and there are
both object-based and array-based interfaces to directory listings.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%_bindir/vfs
%pear_datadir/VFS/
%pear_dir/VFS/
%pear_dir/VFS.php
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

