%define pear_name HTML_Table_Matrix

Name: pear-HTML_Table_Matrix
Version: 1.0.9
Release: alt3

Summary: Autofill a table with data

License: PHP License v3.0
Group: Development/Other
Url: http://pear.php.net/package/HTML_Table_Matrix

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Table_Matrix-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Table

%description
HTML_Table_Matrix is an extension to HTML_Table which allows you to easily
fill up a table with data.
Features:
- It uses Filler classes to determine how the data gets filled in the
table. With a custom Filler, you can fill data in up, down, forwards,
backwards, diagonally, randomly or any other way you like.
- Comes with Fillers to fill left-to-right-top-to-bottom and
right-to-left-top-to-bottom.
- Abstract Filler methods keep the code clean & easy to understand.
- Table height or width may be omitted, and it will figure out the correct
table size based on the data you provide.
- It integrates handily with Pager to create pleasant pageable table
layouts, such as for an image gallery. Just specify a height or width,
Filler, and feed it the data returned from Pager.
- Table may be constrained to a specific height or width, and excess data
will be ignored.
- Fill offset may be specified, to leave room for a table header, or other
elements in the table.
- Fully documented with PHPDoc.
- Includes fully functional example code.

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
%pear_dir/HTML
%pear_dir/doc
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- initial build for ALT Linux Sisyphus

