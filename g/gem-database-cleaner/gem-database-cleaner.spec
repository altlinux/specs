%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname database_cleaner

Name:          gem-database-cleaner
Version:       2.1.0
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DatabaseCleaner/database_cleaner
Vcs:           https://github.com/databasecleaner/database_cleaner.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(cucumber) >= 3.0
BuildRequires: gem(database_cleaner-active_record) >= 2
BuildRequires: gem(database_cleaner-redis) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(listen) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildConflicts: gem(cucumber) >= 4
BuildConflicts: gem(database_cleaner-active_record) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names database_cleaner,database-cleaner
Requires:      gem(database_cleaner-active_record) >= 2
Conflicts:     gem(database_cleaner-active_record) >= 3
Provides:      gem(database_cleaner) = 2.1.0

%description
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing.


%package       -n gem-database-cleaner-core
Version:       2.1.0
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(database_cleaner-core) = 2.1.0

%description   -n gem-database-cleaner-core
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing.


%if_enabled    doc
%package       -n gem-database-cleaner-core-doc
Version:       2.1.0
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета database_cleaner-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(database_cleaner-core) = 2.1.0

%description   -n gem-database-cleaner-core-doc
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing documentation files.

%description   -n gem-database-cleaner-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета database_cleaner-core.
%endif


%if_enabled    devel
%package       -n gem-database-cleaner-core-devel
Version:       2.1.0
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета database_cleaner-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(database_cleaner-core) = 2.1.0
Requires:      gem(activesupport) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(codecov) >= 0
Requires:      gem(cucumber) >= 3.0
Requires:      gem(database_cleaner-active_record) >= 0
Requires:      gem(database_cleaner-redis) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(listen) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(sqlite3) >= 0
Conflicts:     gem(cucumber) >= 4

%description   -n gem-database-cleaner-core-devel
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing development package.

%description   -n gem-database-cleaner-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета database_cleaner-core.
%endif


%if_enabled    doc
%package       -n gem-database-cleaner-doc
Version:       2.1.0
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета database_cleaner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(database_cleaner) = 2.1.0

%description   -n gem-database-cleaner-doc
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing documentation files.

%description   -n gem-database-cleaner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета database_cleaner.
%endif


%if_enabled    devel
%package       -n gem-database-cleaner-devel
Version:       2.1.0
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета database_cleaner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(database_cleaner) = 2.1.0
Requires:      gem(activesupport) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(codecov) >= 0
Requires:      gem(cucumber) >= 3.0
Requires:      gem(database_cleaner-core) >= 0
Requires:      gem(database_cleaner-redis) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(listen) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(sqlite3) >= 0
Conflicts:     gem(cucumber) >= 4

%description   -n gem-database-cleaner-devel
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing development package.

%description   -n gem-database-cleaner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета database_cleaner.
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
%doc CONTRIBUTE.markdown History.rdoc LICENSE README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-database-cleaner-core
%doc CONTRIBUTE.markdown History.rdoc LICENSE README.markdown
%ruby_gemspecdir/database_cleaner-core-2.1.0.gemspec
%ruby_gemslibdir/database_cleaner-core-2.1.0

%if_enabled    doc
%files         -n gem-database-cleaner-core-doc
%doc CONTRIBUTE.markdown History.rdoc LICENSE README.markdown
%ruby_gemsdocdir/database_cleaner-core-2.1.0
%endif

%if_enabled    devel
%files         -n gem-database-cleaner-core-devel
%doc CONTRIBUTE.markdown History.rdoc LICENSE README.markdown
%endif

%if_enabled    doc
%files         -n gem-database-cleaner-doc
%doc CONTRIBUTE.markdown History.rdoc LICENSE README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-database-cleaner-devel
%doc CONTRIBUTE.markdown History.rdoc LICENSE README.markdown
%endif


%changelog
* Tue Feb 04 2025 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.1 -> 2.1.0

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
