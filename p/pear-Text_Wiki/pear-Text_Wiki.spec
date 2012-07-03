%define pear_name Text_Wiki

Name: pear-Text_Wiki
Version: 1.2.0
Release: alt3

Summary: Transforms Wiki and BBCode markup into XHTML, LaTeX or plain text markup. This is the base engine for all of the Text_Wiki sub-classes

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Text_Wiki

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Text_Wiki-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The text transformation is done in 2 steps.
The chosen parser uses markup rules to tokenize the tags and content.
Renderers output the tokens and text into the requested format.
The tokenized form replaces the tags by a protected byte value associated
to an index in an options table. This form shares up to 50 rules by all
parsers and renderers.
The package is intented for versatile transformers as well as converters.
Text_Wiki is delivered with its own parser, which is used by Yawiki or
Horde's Wicked and three basic renderers: XHTML , LaTeX and plain text.
Strong sanitizing of XHTML is default.
Parsers (* and Renderers) exist for BBCode, Cowiki (*), Dokuwiki (*),
Mediawiki and Tikiwiki (*).
It is highly configurable and can be easily extended.

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
%pear_dir/Text
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

