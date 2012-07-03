%define pear_name File_Fortune

Name: pear-File_Fortune
Version: 1.0.0
Release: alt3

Summary: File_Fortune provides an interface for reading from and writing to fortune files

License: New BSD License
Group: Development/Other
Url: http://pear.php.net/package/File_Fortune

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/File_Fortune-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
File_Fortune provides a PHP interface to reading fortune files. With it,
you may
retrieve a single fortune, a random fortune, or all fortunes in the file.

Additionally, it offers the ability to access fortune files as if they
were a
native array, including updating and deleting items. All write operations
will
produce a binary header file to allow compatability with the fortune and
fortune-mod programs (as well as other fortune interfaces).

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
%pear_datadir/File_Fortune/examples
%pear_dir/File
%pear_testdir/File_Fortune/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

