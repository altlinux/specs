%define pear_name HTML_QuickForm_advmultiselect

Name: pear-HTML_QuickForm_advmultiselect
Version: 1.4.0
Release: alt3

Summary: Element for HTML_QuickForm that emulate a multi-select

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/HTML_QuickForm_advmultiselect

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_QuickForm_advmultiselect-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Common >= 1.2.1, pear-HTML_QuickForm >= 3.2.4
Conflicts: pear-HTML_QuickForm = 3.2.4

%description
The HTML_QuickForm_advmultiselect package adds an element to the
HTML_QuickForm package that is two select boxes next to each other
emulating a multi-select.

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
%pear_dir/HTML/
%pear_datadir/HTML_QuickForm_advmultiselect/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Linux Sisyphus

