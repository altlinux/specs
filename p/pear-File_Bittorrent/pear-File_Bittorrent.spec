%define pear_name File_Bittorrent

Name: pear-File_Bittorrent
Version: 1.1.0
Release: alt3

Summary: Decode and Encode data in Bittorrent format

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/File_Bittorrent

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/File_Bittorrent-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-PHP_Compat >= 1.1.0, pear-core >= 1.4.2

%description
This package consists of three classes which handles the encoding and
decoding of data in Bittorrent format.
        You can also extract useful informations from .torrent files,
create .torrent files and query the torrent's scrape page to get its
statistics.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/File
%pear_testdir/File_Bittorrent/Tests
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

