Summary:        Xapian perl bindings

Name:           perl-Search-Xapian
Version:        1.2.25.5
Release:        alt1

Group: Development/Perl
License: Perl
URL: https://metacpan.org/release/Search-Xapian

# https://cpan.metacpan.org/authors/id/O/OL/OLLY/Search-Xapian-%{version}.tar.gz
Source0: %name-%version.tar

BuildRequires: rpm-build-perl
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libxapian-devel
BuildRequires: perl-Devel-Leak
BuildRequires: perl-Test-Pod
#BuildRequires: perl-Test-Pod-Coverage
BuildRequires: perl-devel

%description
This module wraps most methods of most Xapian classes. The missing classes
and methods should be added in the future. It also provides a simplified,
more 'perlish' interface to some common operations, as demonstrated above.

%prep
%setup -q

%build
export TEST_POD=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/*

%changelog
* Tue Apr 05 2022 Igor Vlasenko <viy@altlinux.org> 1.2.25.5-alt1
- New version (1.2.25.5)

* Sun Nov 29 2020 Alexey Gladkov <legion@altlinux.ru> 1.2.25.4-alt1
- New version (1.2.25.4)

* Thu Oct 15 2020 Alexey Gladkov <legion@altlinux.ru> 1.2.25.2-alt1
- First build for ALTLinux.


