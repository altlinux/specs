# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Socket.pm) perl(Socket6.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.03
%define module_name Net-Subnet
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.03
Release: alt1.1
Summary: Fast IP-in-subnet matcher for IPv4 and IPv6, CIDR or mask.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JU/JUERD/%module_name-%module_version.tar.gz
BuildArch: noarch

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
%perl_vendor_privlib/N*

%changelog
* Thu Oct 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.03-alt1.1
- build for ALT

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- initial import by package builder

