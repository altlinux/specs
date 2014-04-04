%define bname Lexical-Persistence
Name: perl-%bname
Version: 1.023
Release: alt1
Summary: Persistent lexical variable values for arbitrary calls
License: Perl (GPL or Artistic)
Group: Development/Perl
URL: http://search.cpan.org/dist/%bname/
Source: http://www.cpan.org/authors/id/R/RC/RCAPUTO/%bname-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-perl
BuildRequires: perl-devel
BuildRequires: perl(Devel/LexAlias.pm) perl(PadWalker.pm)
%{!?_disabe_check:%{!?_disabe_test:BuildRequires: perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm)}}

%description
Lexical::Persistence - Persistent lexical variable values for arbitrary calls.
It does a few things, all related. Note that all the behaviors listed here are
the defaults. Subclasses can override nearly every aspect of
Lexical::Persistence's behavior.
Lexical::Persistence lets your code access persistent data through lexical
variables.


%prep
%setup -q -n %bname-%version


%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build


%install
%makeinstall_std


%check
%make_build test


%files
%doc CHANGES README eg
%perl_vendor_privlib/*
%exclude %_libdir


%changelog
* Fri Apr 04 2014 Led <led@altlinux.ru> 1.023-alt1
- initial build
