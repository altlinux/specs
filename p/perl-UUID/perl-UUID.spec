%define _unpackaged_files_terminate_build 1
Name: perl-UUID
Version: 0.27
Release: alt1.1.1
Summary: DCE compatible Universally Unique Identifier library for Perl

Group: Development/Perl
License: GPL or Artistic
Url: http://search.cpan.org/~jrm/UUID/UUID.pm

Source: http://www.cpan.org/authors/id/J/JR/JRM/UUID-%{version}.tar.gz

BuildRequires: libuuid-devel perl(Devel/CheckLib.pm) perl(ExtUtils/MakeMaker.pm)

%description
The UUID library is used to generate unique identifiers for objects that
may be accessible beyond the local system. For instance, they could be
used to generate unique HTTP cookies across multiple web servers without
communication between the servers, and without fear of a name clash.
The generated UUIDs can be reasonably expected to be unique within a
system, and unique across all systems, and are compatible with those
created by the Open Software Foundation (OSF) Distributed Computing
Environment (DCE) utility uuidgen.

%prep
%setup -q -n UUID-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/UUID.pm
%perl_vendor_autolib/UUID

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1
- rebuild with new perl 5.24.1

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Tue Dec 08 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.24-alt1
- initial release
