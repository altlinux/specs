Name: perl-Data-Localize
Version: 0.00025
Release: alt1

Summary: Data::Localize perl module
Group: Development/Perl
License: Perl

Url: %CPAN Data-Localize
Source: %name-%version.tar

BuildRequires: perl-devel perl-Encode perl-Module-Pluggable perl-I18N-LangTags perl-Test-Requires perl-Any-Moose perl-Mouse perl-Config-Any perl-BerkeleyDB perl-Moo perl(Module/Load.pm) perl(Log/Minimal.pm) perl(MooX/Types/MooseLike/Base.pm)

BuildArch: noarch
%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Data/Localize*
%doc Changes 

%changelog
* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.00025-alt1
- new version 0.00025

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 0.00022-alt1
- initial build
