%def_without db
%define module Logoved-DB

Name: perl-%module
Version: 0.004
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: perl library for Logoved framework and DB
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
#Url: http://git.altlinux.org/people/viy/packages/logoved.git
Url: http://wiki.altlinux.org/Logoved

BuildRequires: perl-devel perl(Logoved/Stream.pm) perl(autodie.pm) perl(Source/Shared/CLI.pm)

%if_with db
Requires: logoved-db = %EVR
%endif

%description
perl library for Logoved framework and DB.

%package -n logoved
Summary: Logoved is a tool for build log analysis and processing.
Group: Development/Perl
Requires: perl-%module = %EVR

%description -n logoved
Logoved is a tool for build log analysis and processing.

%if_with db
%package -n logoved-db
Summary: Database for Logoved.
Group: Development/Perl

%description -n logoved-db
Logoved Database.
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build 

%install
%perl_vendor_install

%if_with db
mkdir -p %buildroot%_datadir/logoved
cp -a db %buildroot%_datadir/logoved/
%endif

%files
#doc Changes
#doc README
%perl_vendor_privlib/Logoved*

%files -n logoved
%_bindir/logoved-*

%if_with db
%_datadir/logoved
%endif

%changelog
* Thu Jan 03 2019 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- new version
- note: DB is constantly updated, it is not packaged yet.
  use git repo for Logoved DB.

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- bugfix release

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- Sisyphus release (closes: #35459)
- note: DB is constantly updated, it is not packaged yet.
- use git repo for Logoved DB.

* Wed Oct 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial rpm build

