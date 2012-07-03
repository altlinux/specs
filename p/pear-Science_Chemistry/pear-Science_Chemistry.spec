%define pear_name Science_Chemistry

Name: pear-Science_Chemistry
Version: 1.1.0
Release: alt3

Summary: Classes to manipulate chemical objects: atoms, molecules, etc

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Science_Chemistry

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Science_Chemistry-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
General classes to represent Atoms, Molecules and Macromolecules.  Also
parsing code for PDB, CML and XYZ file formats.  Examples of parsing and
conversion to/from chemical structure formats. Includes a utility class
with
information on the Elements in the Periodic Table.

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
%pear_dir/Science/
%pear_datadir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

