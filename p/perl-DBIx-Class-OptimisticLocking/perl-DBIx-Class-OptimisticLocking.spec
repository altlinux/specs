%define _unpackaged_files_terminate_build 1

Name: perl-DBIx-Class-OptimisticLocking
Version: 0.02
Release: alt1
Summary: Optimistic locking support for DBIx::Class
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/DBIx-Class-OptimisticLocking/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(DBIx/Class.pm)
BuildRequires: perl(DBIx/Class/Schema.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(Pod/Coverage/TrustPod.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Pod/Coverage.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(base.pm)
BuildRequires: perl(lib.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)

%description
Optimistic locking is an alternative to using exclusive locks when you have
the possibility of concurrent, conflicting updates in your database.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
# incorrect fsf address reported upstream
# https://rt.cpan.org/Ticket/Display.html?id=106640
%perl_vendorlib/DBIx*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.02-alt1
- initial build for ALT
