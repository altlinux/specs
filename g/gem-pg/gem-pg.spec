%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pg

Name:          gem-pg
Version:       1.5.6
Release:       alt1
Summary:       Ruby interface to PostgreSQL RDBMS
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://bitbucket.org/ged/ruby-pg/
Vcs:           https://bitbucket.org/ged/ruby-pg.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: postgresql-devel
BuildRequires: uni2ascii
%if_enabled check
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(rake-compiler-dock) >= 1.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(rspec) >= 3.5
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Obsoletes:     ruby-pg < %EVR
Provides:      ruby-pg = %EVR
Provides:      gem(pg) = 1.5.6


%description
This is the extension library to access a PostgreSQL database from Ruby. This
library works with PostgreSQL 6.4-8.x; it probably works with 6.3 or earlier
with slight modification, but not tested at all.


%if_enabled    doc
%package       -n gem-pg-doc
Version:       1.5.6
Release:       alt1
Summary:       Ruby interface to PostgreSQL RDBMS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pg
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pg) = 1.5.6

%description   -n gem-pg-doc
Ruby interface to PostgreSQL RDBMS documentation files.

This is the extension library to access a PostgreSQL database from Ruby. This
library works with PostgreSQL 6.4-8.x; it probably works with 6.3 or earlier
with slight modification, but not tested at all.

%description   -n gem-pg-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pg.
%endif


%if_enabled    devel
%package       -n gem-pg-devel
Version:       1.5.6
Release:       alt1
Summary:       Ruby interface to PostgreSQL RDBMS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pg
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pg) = 1.5.6
Requires:      gem(bundler) >= 1.16
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(rake-compiler-dock) >= 1.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(rspec) >= 3.5
Requires:      postgresql-devel
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rspec) >= 4

%description   -n gem-pg-devel
Ruby interface to PostgreSQL RDBMS development package.

This is the extension library to access a PostgreSQL database from Ruby. This
library works with PostgreSQL 6.4-8.x; it probably works with 6.3 or earlier
with slight modification, but not tested at all.

%description   -n gem-pg-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pg.
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
%doc README-OS_X.rdoc README-Windows.rdoc README.ja.md README.md misc/postgres/README.txt
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-pg-doc
%doc README-OS_X.rdoc README-Windows.rdoc README.ja.md README.md misc/postgres/README.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pg-devel
%doc README-OS_X.rdoc README-Windows.rdoc README.ja.md README.md misc/postgres/README.txt
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.6-alt1
- ^ 1.3.5 -> 1.5.6

* Fri May 13 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt1
- ^ 1.3.4 -> 1.3.5

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.4-alt1
- ^ 1.2.3 -> 1.3.4

* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.3-alt1.1
- + ignore names to spec

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.3-alt1
- ^ 1.1.4 -> 1.2.3
- ! spec tags and syntax

* Mon Dec 09 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt2
- added (+) postgresql-devel to gem-pg-devel
- added (+) some translations
- fixed (*) some syntax issues, licence (TODO)

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- Bump to 1.1.4
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.5
- Rebuild with new Ruby autorequirements.
- Disable debuginfo.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Tue Sep 13 2016 Denis Medvedev <nbr@altlinux.org> 0.19.0-alt1
- new version

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.9.0-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Sun Dec 08 2012 Led <led@altlinux.ru> 0.9.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed build doc
- fixed build with libruby 1.9.x

* Fri Jun 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.9.0-alt1
- [0.9.0] (closes: #23616)

* Mon Aug 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.0-alt2
- Applied m17n patch by Yuki Sonoda and Nikolai Lugovoi

* Wed May 13 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.0-alt1
- [0.8.0]

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 0.7.9.2008.08.17-alt1
- Built for Sisyphus
