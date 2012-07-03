%define pear_name HTML_Template_Sigma

Name: pear-HTML_Template_Sigma
Version: 1.1.6
Release: alt3

Summary: An implementation of Integrated Templates API with template 'compilation' added

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_Template_Sigma

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Template_Sigma-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
HTML_Template_Sigma implements Integrated Templates API designed by Ulf
Wendel.

Features:
* Nested blocks. Nesting is controlled by the engine.
* Ability to include files from within template: <!-- INCLUDE -->
* Automatic removal of empty blocks and unknown variables (methods to
manually tweak/override this are also available)
* Methods for runtime addition and replacement of blocks in templates
* Ability to insert simple function calls into templates:
func_uppercase('Hello world!') and to define callback functions for these
* 'Compiled' templates: the engine has to parse a template file using
regular expressions to find all the blocks and variable placeholders. This
is a very "expensive" operation and is an overkill to do on every page
request: templates seldom change on production websites. Thus this feature:
an internal representation of the template structure is saved into a file
and this file gets loaded instead of the source one on subsequent requests
(unless the source changes)
* PHPUnit-based tests to define correct behaviour
* Usage examples for most of the features are available, look in the docs/
directory

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
%pear_testdir/HTML_Template_Sigma/
%pear_dir/HTML
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- initial build for ALT Linux Sisyphus

