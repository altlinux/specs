%define pear_name Text_Wiki_Mediawiki

Name: pear-Text_Wiki_Mediawiki
Version: 0.2.0
Release: alt2

Summary: Mediawiki parser for Text_Wiki

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Text_Wiki_Mediawiki

Packager: Alexandra Panyukova <mex3@altlinux.ru>

Source: Text_Wiki_Mediawiki.tar.gz

BuildArchitectures: noarch

Requires: pear-Text_Wiki
BuildRequires: pear-core rpm-build-pear php5

%description
Parses Mediawiki mark-up to tokenize the text for Text_Wiki renderings.

%prep
%setup -c

%build
cd %pear_name
%pear_build

%install
cd %pear_name
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%pear_dir/Text
%pear_xmldir/%pear_name.xml

%changelog
* Thu Jan 28 2010 Alexandra Panyukova <mex3@altlinux.org> 0.2.0-alt2
- adding php to BuildRequires

* Sun Jan 17 2010 Alexandra Panyukova <mex3@altlinux.ru> 0.2.0-alt1
- initial build