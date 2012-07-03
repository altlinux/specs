%define pear_name PEAR_PackageFileManager

Name: pear-PEAR_PackageFileManager
Version: 1.6.3
Release: alt3

Summary: PEAR_PackageFileManager takes an existing package.xml file and updates it with a new filelist and changelog

License: PHP License 3.01
Group: Development/Other
Url: http://pear.php.net/package/PEAR_PackageFileManager

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PEAR_PackageFileManager-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package revolutionizes the maintenance of PEAR packages.  With a few
parameters,
the entire package.xml is automatically updated with a listing of all
files in a package.
Features include
 - manages the new package.xml 2.0 format in PEAR 1.4.0
 - can detect PHP and extension dependencies using PHP_CompatInfo
 - reads in an existing package.xml file, and only changes the
release/changelog
 - a plugin system for retrieving files in a directory.  Currently four
plugins
   exist, one for standard recursive directory content listing, one that
   reads the CVS/Entries files and generates a file listing based on the
contents
   of a checked out CVS repository, one that reads Subversion entries
files, and
   one that queries a Perforce repository.
 - incredibly flexible options for assigning install roles to
files/directories
 - ability to ignore any file based on a * ? wildcard-enabled string(s)
 - ability to include only files that match a * ? wildcard-enabled
string(s)
 - ability to manage dependencies
 - can output the package.xml in any directory, and read in the
package.xml
   file from any directory.
 - can specify a different name for the package.xml file

PEAR_PackageFileManager is fully unit tested.
The new PEAR_PackageFileManager2 class is not.

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
%pear_dir/PEAR
%pear_testdir/PEAR_PackageFileManager/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- initial build for ALT Linux Sisyphus

