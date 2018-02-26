%define pear_name HTML_QuickForm

Name: pear-HTML_QuickForm
Version: 3.2.10
Release: alt3

Summary: The PEAR::HTML_QuickForm package provides methods for creating, validating, processing HTML forms

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_QuickForm

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_QuickForm-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Common >= 1.2.1, pear-core >= 1.4.0

%description
NOTICE: development of HTML_QuickForm version 3 is frozen. Please submit
feature requests for HTML_QuickForm2 package.

The HTML_QuickForm package provides methods to dynamically create,
validate
and render HTML forms.

Features:
* More than 20 ready-to-use form elements.
* XHTML compliant generated code.
* Numerous mixable and extendable validation rules.
* Automatic server-side validation and filtering.
* On request javascript code generation for client-side validation.
* File uploads support.
* Total customization of form rendering.
* Support for external template engines (ITX, Sigma, Flexy, Smarty).
* Pluggable elements, rules and renderers extensions.

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.10-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.10-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.10-alt1
- initial build for ALT Linux Sisyphus

