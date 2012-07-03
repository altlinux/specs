%define dist DBI
Name: perl-%dist
Version: 1.616
Release: alt2

Summary: Database independent interface for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

# requires Apache; not required by any package
%add_findreq_skiplist */DBI/ProfileDumper/Apache.pm
# requires Coro::Select
%add_findreq_skiplist */DBD/Gofer/Transport/corostream.pm

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Devel-Leak perl-JSON-XS perl-List-MoreUtils perl-MLDBM perl-PlRPC perl-SQL-Statement perl-Test-Pod perl-Test-Pod-Coverage

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide
a consistent database interface, independent of the actual database
being used.

# required to build binary DBI drivers
%package devel
Summary: DBI development files
Group: Development/Perl
Requires: %name = %version-%release

%description devel
This package contains DBI header files and additional modules
required to build DBI binary drivers.

# profiler
%package Profile
Summary: Performance profiling and benchmarking for the DBI
Group: Development/Perl
Requires: %name = %version-%release

%description Profile
The DBI::Profile module provides a simple interface to collect
and report performance and benchmarking data from the DBI.
DBI::ProfileDumper is a subclass of DBI::Profile which dumps
profile data to disk instead of printing a summary to your screen.
You can then use %_bindir/dbiprof to analyze the data in a number
of interesting ways, or you can roll your own analysis using
DBI::ProfileData.

# requires MLDBM
%package -n perl-DBD-DBM
Summary: DBI driver for DBM and MLDBM files
Group: Development/Perl
Requires: perl-DBD-File = %version-%release

%description -n perl-DBD-DBM
DBD::DBM is a database management sytem that can work right out
of the box.  The module uses a DBM file storage layer.  DBM file
storage is common on many platforms and files can be created with
it in many languges.

# required by perl-DBD-DBM, DBD::AnyData, and DBD::CSV
%package -n perl-DBD-File
Summary: Base class for writing DBI drivers
Group: Development/Perl
Requires: %name = %version-%release
Requires: perl(SQL/Statement.pm) >= 1.280
Conflicts: perl(DBD/CSV.pm) <= 0.290

%description -n perl-DBD-File
DBD::File module is a base class for writing DBI drivers
that work with plain files, for example CSV files.

# requires PlRPC
%package -n perl-DBD-Proxy
Summary: A proxy driver for the DBI
Group: Development/Perl
Requires: %name = %version-%release

%description -n perl-DBD-Proxy
DBD::Proxy is a Perl module for connecting to a database
via a remote DBI driver.

# requires PlRPC
%package ProxyServer
Summary: A server for the DBD::Proxy driver
Group: Development/Perl
Requires: %name = %version-%release

%description ProxyServer
DBI::ProxyServer is a module for implementing a proxy
for the DBI proxy driver, DBD::Proxy. It allows access
to databases over the network.

# Gofer is "next big thing"
%package Gofer
Summary: DBI::Gofer proxy server classes
Group: Development/Perl
Requires: %name = %version-%release

%description Gofer
DBI::Gofer::Execute accepts remote DBI::Gofer::Request object,
executes the requested DBI method calls, and returns
a DBI::Gofer::Response object.

%package -n perl-DBD-Gofer
Summary: A stateless-proxy driver for communicating with a remote DBI
Group: Development/Perl
Requires: %name-Gofer = %version-%release

%description -n perl-DBD-Gofer
DBD::Gofer is a DBI database driver that forwards requests to another
DBI driver, usually in a seperate process, often on a separate machine.
It tries to be as transparent as possible so it appears that you are
using the remote driver directly.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

rm blib/lib/DBI/PurePerl.pm
rm blib/lib/DBI/W32ODBC.pm
rm blib/lib/Win32/DBIODBC.pm
rm blib/lib/Bundle/DBI.pm
rm blib/lib/dbixs_rev.pl
mv blib/lib/DBI/FAQ.{pm,pod}

%install
%perl_vendor_install

%files
	%perl_vendor_archlib/DBI.pm
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/Sponge.pm
%dir	%perl_vendor_autolib/DBI
	%perl_vendor_autolib/DBI/DBI.so
%dir	%perl_vendor_archlib/DBI
%dir	%perl_vendor_archlib/DBI/Const
	%perl_vendor_archlib/DBI/Const/GetInfo*
%dir	%perl_vendor_archlib/DBI/Util
	%perl_vendor_archlib/DBI/Util/*.pm
%doc	%perl_vendor_archlib/DBI/Changes.pod
%doc	%perl_vendor_archlib/DBI/FAQ.pod

%files devel
	%_bindir/dbilogstrip
%dir	%perl_vendor_archlib/DBI
%dir	%perl_vendor_archlib/DBI/DBD
	%perl_vendor_archlib/DBI/DBD.pm
	%perl_vendor_archlib/DBI/DBD/Metadata.pm
%dir	%perl_vendor_autolib/DBI
	%perl_vendor_autolib/DBI/*.h
	%perl_vendor_autolib/DBI/Driver.xst
# extras
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/ExampleP.pm
	%perl_vendor_archlib/DBD/NullP.pm

%files Profile
	%_bindir/dbiprof
%dir	%perl_vendor_archlib/DBI
	%perl_vendor_archlib/DBI/Profile*

%files -n perl-DBD-DBM
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/DBM.pm

%files -n perl-DBD-File
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/File.pm
%dir	%perl_vendor_archlib/DBD/File
%doc	%perl_vendor_archlib/DBD/File/*.pod
%dir	%perl_vendor_archlib/DBI/SQL
	%perl_vendor_archlib/DBI/SQL/Nano.pm
%dir	%perl_vendor_archlib/DBI/DBD
	%perl_vendor_archlib/DBI/DBD/SqlEngine.pm
%dir	%perl_vendor_archlib/DBI/DBD/SqlEngine
	%perl_vendor_archlib/DBI/DBD/SqlEngine/*.pod

%files -n perl-DBD-Proxy
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/Proxy.pm

%files ProxyServer
	%_bindir/dbiproxy
%dir	%perl_vendor_archlib/DBI
	%perl_vendor_archlib/DBI/ProxyServer.pm

%files Gofer
%dir	%perl_vendor_archlib/DBI
	%perl_vendor_archlib/DBI/Gofer*

%files -n perl-DBD-Gofer
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/Gofer*

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.616-alt2
- rebuilt for perl-5.14

* Sun Feb 13 2011 Alexey Tourbin <at@altlinux.ru> 1.616-alt1
- 1.611 -> 1.616
- packaged DBI/DBD/SqlEngine.pm into perl-DBD-File

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.611-alt1.1
- rebuilt for perl-5.12

* Mon May 03 2010 Alexey Tourbin <at@altlinux.ru> 1.611-alt1
- 1.609 -> 1.611

* Fri Jun 12 2009 Alexey Tourbin <at@altlinux.ru> 1.609-alt1
- 1.608 -> 1.609

* Mon May 11 2009 Alexey Tourbin <at@altlinux.ru> 1.608-alt1
- 1.607 -> 1.608

* Fri Apr 17 2009 Alexey Tourbin <at@altlinux.ru> 1.607-alt2
- perl-DBI: own DBI dir

* Sun Jul 27 2008 Alexey Tourbin <at@altlinux.ru> 1.607-alt1
- 1.605 -> 1.607

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 1.605-alt1
- 1.604 -> 1.605

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.604-alt1
- 1.602 -> 1.604

* Sat Mar 01 2008 Alexey Tourbin <at@altlinux.ru> 1.602-alt1
- 1.58 -> 1.602

* Wed Jul 04 2007 Alexey Tourbin <at@altlinux.ru> 1.58-alt1
- 1.53 -> 1.58
- fixed $_ clobbering (cpan #27946, #27947)
- fixed dbiprof script (cpan #27948)
- packaged perl-DBI-Gofer and perl-DBD-Gofer
- packaged %_bindir/dbilogstrip into perl-DBI-devel
- moved DBI/Const/GetInfo* from perl-DBI-devel to perl-DBI,
  to meet recent DBD::mysql dependences
- also moved DBI::FAQ from perl-DBI-devel to perl-DBI

* Tue Nov 14 2006 Alexey Tourbin <at@altlinux.ru> 1.53-alt1
- 1.52 -> 1.53

* Wed Aug 09 2006 Alexey Tourbin <at@altlinux.ru> 1.52-alt1
- 1.51 -> 1.52

* Wed Jun 07 2006 Alexey Tourbin <at@altlinux.ru> 1.51-alt1
- 1.50 -> 1.51

* Sun Apr 16 2006 Alexey Tourbin <at@altlinux.ru> 1.50-alt1
- 1.48 -> 1.50

* Wed Jun 08 2005 Alexey Tourbin <at@altlinux.ru> 1.48-alt2
- moved DBD::Sponge from %name-devel to %name

* Wed Mar 16 2005 Alexey Tourbin <at@altlinux.ru> 1.48-alt1
- 1.47 -> 1.48

* Thu Feb 03 2005 Alexey Tourbin <at@altlinux.ru> 1.47-alt1
- 1.46 -> 1.47
- alt-tmp-pidfile.patch not needed anymore (CAN-2005-0077)

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1.46-alt1
- 1.45 -> 1.46
- subpackages: perl-DBI-devel, perl-DBI-Profile, perl-DBD-DBM,
  perl-DBD-File, perl-DBD-Proxy, and perl-DBI-ProxyServer
- disabled DBI::PurePerl
- manual pages not packaged (use perldoc)

* Wed Oct 06 2004 Alexey Tourbin <at@altlinux.ru> 1.45-alt1
- 1.43 -> 1.45

* Tue Jul 06 2004 Alexey Tourbin <at@altlinux.ru> 1.43-alt1
- 1.42 -> 1.43

* Sun Mar 14 2004 Alexey Tourbin <at@altlinux.ru> 1.42-alt1
- 1.42
- create .svn magic dir to enable excessive testing
- test base extended (BuildRequires: perl-DBM perl-MLDBM)

* Wed Feb 25 2004 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.41

* Sat Feb 07 2004 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- 1.40

* Sun Nov 30 2003 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.39

* Mon Sep 08 2003 Alexey Tourbin <at@altlinux.ru> 1.38-alt1
- 1.38
- test base extended (BuildRequires: perl-DBD-Pg perl-DBD-mysql)
- t/80proxy.t test disabled

* Sat Jun 21 2003 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.37
- alt-changes-pod.patch: install Changes.pod rather than Changes.pm
- alt-buildreq.patch: don't look for previous DBI installations
- buildreq applied (t/80proxy.t test skipped under buildreq)

* Mon Apr 28 2003 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.35 (memory leak fixed, misc. fixes and updates)

* Wed Mar 05 2003 Alexey Tourbin <at@altlinux.ru> 1.34-alt1
- 1.34 (see Changelog)
- ignore perl(Apache.pm) dependency

* Fri Oct 25 2002 Alexey Tourbin <at@altlinux.ru> 1.25-alt2
- rebuilt for perl-5.8 with new rpm macros

* Fri Jun 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.25-alt1
- 1.25

* Thu Mar 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.21-alt1
- 1.21

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.14-ipl7mdk
- Rebuilt with new perl again

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.14-ipl6mdk
- Rebuilt with perl-5.6.1

* Sun Mar 18 2001 Mikhail Zabaluev <zabaluev@parascript.com> ipl5mdk
- Spec file cleanup
- Updated descriptions and URL
- Enhanced filelist, added binaries

* Sun Jan 21 2001 Alexander Bokovoy <ab@avilink.net> ipl4mdk
- Rebuild from scratch using MZh's spec skeleton file
