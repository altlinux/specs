%define        gemname sqlite3

Name:          gem-sqlite3
Version:       1.5.4
Release:       alt1
Summary:       A Ruby interface for the SQLite database engine
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://github.com/sparklemotion/sqlite3-ruby
Vcs:           https://github.com/sparklemotion/sqlite3-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libsqlite3-devel
BuildRequires: gem(mini_portile2) >= 2.8.0 gem(mini_portile2) < 2.9
%if_with check
BuildRequires: gem(minitest) >= 5.15 gem(minitest) < 6
BuildRequires: gem(rake-compiler) >= 1.1.2 gem(rake-compiler) < 2
BuildRequires: gem(rake-compiler-dock) >= 0.7.2 gem(rake-compiler-dock) < 1.3
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(minitest) >= 5.15 gem(minitest) < 6
BuildRequires: gem(rake-compiler) >= 1.2.0 gem(rake-compiler) < 2
BuildRequires: gem(rake-compiler-dock) >= 1.2.1 gem(rake-compiler-dock) < 1.3
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(mini_portile2) >= 2.8.0 gem(mini_portile2) < 2.9
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(mini_portile2) >= 2.8.0 gem(mini_portile2) < 2.9
Obsoletes:     sqlite3-ruby < %EVR
Provides:      sqlite3-ruby = %EVR
Provides:      gem(sqlite3) = 1.5.4


%description
A Ruby interface for the SQLite database engine.


%package       -n gem-sqlite3-doc
Version:       1.5.4
Release:       alt1
Summary:       A Ruby interface for the SQLite database engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sqlite3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sqlite3) = 1.5.4

%description   -n gem-sqlite3-doc
A Ruby interface for the SQLite database engine documentation files.

%description   -n gem-sqlite3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sqlite3.


%package       -n gem-sqlite3-devel
Version:       1.5.4
Release:       alt1
Summary:       A Ruby interface for the SQLite database engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sqlite3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sqlite3) = 1.5.4
Requires:      gem(minitest) >= 5.15 gem(minitest) < 6
Requires:      gem(rake-compiler) >= 1.2.0 gem(rake-compiler) < 2
Requires:      gem(rake-compiler-dock) >= 1.2.1 gem(rake-compiler-dock) < 1.3
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      libsqlite3-devel

%description   -n gem-sqlite3-devel
A Ruby interface for the SQLite database engine development package.

%description   -n gem-sqlite3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sqlite3.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-sqlite3-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sqlite3-devel
%doc README.md
%ruby_includedir/*


%changelog
* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- ^ 1.4.2.1 -> 1.5.4

* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.2.1-alt1
- ^ 1.4.2 -> 1.4.2.1

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt2
- ! spec tags and syntax

* Thu Dec 19 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- New version.

* Tue Jun 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.4.0 -> 1.4.1

* Tue Jun 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2
- Fix specfile

* Mon Mar 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- Bump to 1.4.0
- Use Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.6
- Rebuild with new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.5
- Package as gem.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt1
- new version 1.3.13

* Wed Sep 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt2
- Rebuild with Ruby 2.3.1

* Tue Sep 13 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.3.0-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.3.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Jun 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.0-alt1
- [1.3.0]

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.5-alt2
- Force encoding to UTF-8

* Sun Aug 16 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.5-alt1
- [1.2.5]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.4-alt1
- [1.2.4]

* Tue Apr 01 2008 Sir Raorn <raorn@altlinux.ru> 1.2.1-alt2
- Rebuilt with rpm-build-ruby

* Wed Jan 09 2008 Sir Raorn <raorn@altlinux.ru> 1.2.1-alt1
- Initial build for ALT Linux
