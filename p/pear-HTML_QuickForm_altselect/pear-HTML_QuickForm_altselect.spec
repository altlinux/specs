%define pear_name HTML_QuickForm_altselect

Name: pear-HTML_QuickForm_altselect
Version: 1.0.0
Release: alt3

Summary: An alternative to HTML_QuickForm_select using radio buttons and checkboxes

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/HTML_QuickForm_altselect

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_QuickForm_altselect-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Common >= 1.2.1, pear-HTML_QuickForm >= 3.2.5, pear-core >= 1.4.0b1

%description
A QuickForm plugin that extends the select element and turns its options
into checkboxes or radio buttons depending on whether the multiple html
attribute was set or not. For extra options not listed, you can also render
an 'Other' textfield.

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
%pear_testdir/HTML_QuickForm_altselect/
%pear_dir/HTML
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

