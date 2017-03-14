Name: ruby-odbc
Version: 0.99998
Release: alt1

Summary: ODBC extension for Ruby
License: GPL
Group: Development/Ruby
Url: http://www.ch-werner.de/rubyodbc

Source: %name-%version.tar

BuildRequires: libruby-devel libunixODBC-devel ruby-tool-setup

%description
This is an ODBC binding for Ruby. So far it has been tested with
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (local), unixODBC 2.1.0 on Linux 2.2-x86
 - Ruby 1.6.4, MySQL 3.22/MyODBC (local), libiodbc 2.50 on Linux 2.2-x86
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (remote), MS Jet Engine, MSVC++ 6.0
   on Windows NT4SP6
 - Ruby 1.6.[3-5], MySQL 3.22/MyODBC (remote), MS Jet Engine, cygwin,
   on Windows NT4SP6 and 2000
 - Ruby 1.8.4, SQLite/ODBC 0.67, libiodbc 3.52.4 on Fedora Core 3 x86

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc README doc/
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1
- New version
- Rebuild with new %%ruby_sitearchdir location

* Thu Sep 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.99997-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.99992-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.99992-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.99992-alt1
- 0.99992 release.

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9997-alt1
- 0.9997 release.
- Also build UTF-8 version.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9995-alt1
- 0.9995 release.

* Wed Jan 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9994-alt1
- 0.9994 release.

* Fri Dec 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.9993-alt1
- Initial ALTLinux package.
