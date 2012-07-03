Name: perl-Module-Manifest
Version: 1.08
Release: alt1
Summary: Module::Manifest - Parse and examine a Perl distribution MANIFEST file

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/Module-Manifest/

Source: Module-Manifest-%version.tar
Patch:  Module-Manifest-%version-%release.patch
BuildArch: noarch
BuildRequires: perl-devel perl-Test-Exception perl-Test-Warn perl-Params-Util

%description
%summary

%prep
%setup -q -n Module-Manifest-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Manifest.pm
%doc LICENSE Changes README

%changelog
* Tue Nov 23 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1
- initial build
