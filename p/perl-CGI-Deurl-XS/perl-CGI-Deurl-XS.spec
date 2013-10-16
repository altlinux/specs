%define module_version 0.07
%define module_name CGI-Deurl-XS
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt2
Summary: Fast decoder for URL parameter strings
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/A/AT/ATHOMASON/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- build for Sisyphus (required for perl update)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.07-alt1.1
- rebuild with new perl

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

