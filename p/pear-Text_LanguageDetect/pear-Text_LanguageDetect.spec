%define pear_name Text_LanguageDetect

Name: pear-Text_LanguageDetect
Version: 0.2.3
Release: alt1

Summary: Language detection class

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
Text_LanguageDetect can identify 52 human languages from text samples and
return confidence scores for each.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_datadir/Text_LanguageDetect/
%pear_dir/Text/LanguageDetect/
%pear_dir/Text/LanguageDetect.php
%pear_testdir/Text_LanguageDetect/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

