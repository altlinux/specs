Name: perl-MooseX-Clone
Version: 0.05
Release: alt1

Summary: MooseX::Clone - fine grained cloning support for Moose objects
Group: Development/Perl
License: Perl

Url: %CPAN MooseX-Clone
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(namespace/clean.pm) perl-devel perl(Hash/Util/FieldHash/Compat.pm) perl(Test/use/ok.pm) perl(Data/Visitor.pm) perl(Moose.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MooseX/Clone*
%doc Changes

%changelog
* Thu Sep 05 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build for ALTLinux

