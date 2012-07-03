%define dist Class-DBI
Name: perl-%dist
Version: 3.0.17
Release: alt2

Summary: Simple Database Abstraction
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-v%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Class-Accessor perl-Class-Trigger perl-Clone perl-DBD-Pg perl-DBD-SQLite perl-DBD-mysql perl-Date-Simple perl-Ima-DBI perl-Test-Pod perl-Test-Pod-Coverage perl-Time-Piece perl-UNIVERSAL-moniker

%description
Class::DBI provides a convenient abstraction layer to a database.
It not only provides a simple database to object mapping layer, but can
be used to implement several higher order database functions (triggers,
referential integrity, cascading delete etc.), at the application level,
rather than at the database.

%prep
%setup -q -n %dist-v%version

# don't check installed version
sed -i 's/^eval "require/eval "die/' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 3.0.17-alt2
- rebuilt as plain src.rpm

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 3.0.17-alt1
- v3.0.16 -> v3.0.17
- back from v-string versioning to version.pm object
- reverted part of $sth->finish change

* Mon Aug 06 2007 Alexey Tourbin <at@altlinux.ru> 3.0.16-alt1
- v3.0.15 -> v3.0.16

* Sun Oct 22 2006 Alexey Tourbin <at@altlinux.ru> 3.0.15-alt1
- v3.0.14 -> v3.0.15
- imported sources into git and built with gear
- placed explicit $sth->finish calls to workaround bugs in DBD::SQLite 1.13

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 3.0.14-alt1
- v3.0.8 -> v3.0.14

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 3.0.8-alt1
- 0.96 -> v3.0.8
- use v-string (v3.0.8) instead of version object for now

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 0.96-alt1
- initial revision
