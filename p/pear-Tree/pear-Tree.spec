%define pear_name Tree

Name: pear-Tree
Version: 0.3.3
Release: alt1

Summary: Generic tree management, currently supports DB and XML as data sources

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Tree

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Tree-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides methods to read and manipulate trees, which are stored in the DB
or an XML file. The trees can be stored in the DB either as nested trees.
Or as simple trees ('brain dead method'), which use parentId-like
structure.
Currently XML data can only be read from a file and accessed.
The package offers a big number of methods to access and manipulate trees.
For example methods like: getRoot, getChild[ren[Ids]], getParent[s[Ids]],
getPath[ById] and many more.

There are two ways of retreiving the data from the place where they
are stored, one is by reading the entire tree into the memory - the
Memory way. The other is reading the tree nodes as needed (very useful
in combination with huge trees and the nested set model).  The package
is designed that way that it is possible to convert/copy tree data from
either structure to another (from XML into DB).

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
%pear_dir/Tree/
%pear_testdir/Tree/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt1
- new version 0.3.3 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt2
- update according to rpm-build-pear 0.3

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux Sisyphus

