%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-odbc

Name:          gem-ruby-odbc
Version:       0.999991
Release:       alt1
Summary:       ODBC extension for Ruby
License:       GPLv2 or Ruby
Group:         Development/Ruby
Url:           http://www.ch-werner.de/rubyodbc
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libunixODBC-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-odbc < %EVR
Provides:      ruby-odbc = %EVR
Provides:      gem(ruby-odbc) = 0.999991


%description
This is an ODBC binding for Ruby. So far it has been tested with
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (local), unixODBC 2.1.0 on Linux 2.2-x86
 - Ruby 1.6.4, MySQL 3.22/MyODBC (local), libiodbc 2.50 on Linux 2.2-x86
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (remote), MS Jet Engine, MSVC++ 6.0
   on Windows NT4SP6
 - Ruby 1.6.[3-5], MySQL 3.22/MyODBC (remote), MS Jet Engine, cygwin,
   on Windows NT4SP6 and 2000
 - Ruby 1.8.4, SQLite/ODBC 0.67, libiodbc 3.52.4 on Fedora Core 3 x86


%if_enabled    doc
%package       -n gem-ruby-odbc-doc
Version:       0.999991
Release:       alt1
Summary:       ODBC extension for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-odbc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-odbc) = 0.999991

%description   -n gem-ruby-odbc-doc
ODBC extension for Ruby documentation files.

This is an ODBC binding for Ruby. So far it has been tested with
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (local), unixODBC 2.1.0 on Linux 2.2-x86
 - Ruby 1.6.4, MySQL 3.22/MyODBC (local), libiodbc 2.50 on Linux 2.2-x86
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (remote), MS Jet Engine, MSVC++ 6.0
   on Windows NT4SP6
 - Ruby 1.6.[3-5], MySQL 3.22/MyODBC (remote), MS Jet Engine, cygwin,
   on Windows NT4SP6 and 2000
 - Ruby 1.8.4, SQLite/ODBC 0.67, libiodbc 3.52.4 on Fedora Core 3 x86

%description   -n gem-ruby-odbc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-odbc.
%endif


%if_enabled    devel
%package       -n gem-odbc-devel
Version:       0.999991
Release:       alt1
Summary:       ODBC extension for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-odbc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-odbc) = 0.999991

%description   -n gem-odbc-devel
ODBC extension for Ruby development package.

This is an ODBC binding for Ruby. So far it has been tested with
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (local), unixODBC 2.1.0 on Linux 2.2-x86
 - Ruby 1.6.4, MySQL 3.22/MyODBC (local), libiodbc 2.50 on Linux 2.2-x86
 - Ruby 1.[6-8], MySQL 3.22/MyODBC (remote), MS Jet Engine, MSVC++ 6.0
   on Windows NT4SP6
 - Ruby 1.6.[3-5], MySQL 3.22/MyODBC (remote), MS Jet Engine, cygwin,
   on Windows NT4SP6 and 2000
 - Ruby 1.8.4, SQLite/ODBC 0.67, libiodbc 3.52.4 on Fedora Core 3 x86

%description   -n gem-odbc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-odbc.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-ruby-odbc-doc
%doc README
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-odbc-devel
%doc README
%endif


%changelog
* Sun Aug 04 2024 Pavel Skrylev <majioa@altlinux.org> 0.999991-alt1
- ^ 0.99999 -> 0.999991
- - drop tainted methods in favor of pure locale ones

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.99999-alt2
- * license
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.99999-alt1
- > Ruby Policy 2.0
- ^ 0.99998 -> 0.99999

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.99998-alt1.1
- Rebuild with Ruby 2.4.1

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
