%define pear_name HTML_QuickForm_Controller

Name: pear-HTML_QuickForm_Controller
Version: 1.0.8
Release: alt3

Summary: The add-on to HTML_QuickForm package that allows building of multipage forms

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_QuickForm_Controller

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_QuickForm_Controller-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_QuickForm >= 3.2.5, pear-core >= 1.4.11

%description
The package is essentially an implementation of a PageController pattern.
Architecture:
* Controller class that examines HTTP requests and manages form values
persistence across requests.
* Page class (subclass of QuickForm) representing a single page of the
form.
* Business logic is contained in subclasses of Action class.
Cool features:
* Includes several default Actions that allow easy building of multipage
forms.
* Includes usage examples for common usage cases (single-page form,
wizard, tabbed form).

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- initial build for ALT Linux Sisyphus

