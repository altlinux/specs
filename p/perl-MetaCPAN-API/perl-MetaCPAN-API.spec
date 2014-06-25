Name: perl-MetaCPAN-API
Version: 0.44
Release: alt1

Summary: A comprehensive, DWIM-featured API to MetaCPAN
Group: Development/Perl
License: perl

Url: %CPAN MetaCPAN-API
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(URI/Escape.pm) perl(Test/Fatal.pm) perl(Test/TinyMocker.pm) perl(HTTP/Tiny.pm) perl(Module/Build.pm) perl(Try/Tiny.pm) perl-devel perl(Any/Moose.pm) perl(JSON.pm) perl(Mouse.pm)

%description
%summary

%prep
%setup -q
# skip tests that required internet connection
rm t/author.t t/autocomplete.t t/distribution.t t/favorite.t t/fetch.t t/file.t t/module.t t/pod.t t/release.t t/source.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MetaCPAN/API*
%doc Changes LICENSE README

%changelog
* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 0.43-alt1
- initial build for ALTLinux

