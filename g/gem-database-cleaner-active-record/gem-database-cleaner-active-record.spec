%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname database_cleaner-active_record

Name:          gem-database-cleaner-active-record
Version:       2.2.0
Release:       alt1
Summary:       Strategies for cleaning databases using ActiveRecord. Can be used to ensure a clean state for testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DatabaseCleaner/database_cleaner-active_record
Vcs:           https://github.com/databasecleaner/database_cleaner-active_record.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activerecord) >= 5
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(database_cleaner-core) >= 2.0.0
BuildRequires: gem(mysql2) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rails) >= 5.2
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(trilogy) >= 0
BuildConflicts: gem(database_cleaner-core) >= 3
BuildConflicts: gem(rails) >= 8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rails >= 7.1,rails < 8
%ruby_use_gem_dependency database_cleaner-core >= 2.2,database_cleaner-core < 3
%ruby_alias_names database_cleaner-active_record,database-cleaner-active-record
Requires:      gem(activerecord) >= 5
Requires:      gem(database_cleaner-core) >= 2.0.0
Conflicts:     gem(database_cleaner-core) >= 3
Provides:      gem(database_cleaner-active_record) = 2.2.0

%description
Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing.


%if_enabled    doc
%package       -n gem-database-cleaner-active-record-doc
Version:       2.2.0
Release:       alt1
Summary:       Strategies for cleaning databases using ActiveRecord. Can be used to ensure a clean state for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета database_cleaner-active_record
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(database_cleaner-active_record) = 2.2.0

%description   -n gem-database-cleaner-active-record-doc
Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing documentation files.

%description   -n gem-database-cleaner-active-record-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета database_cleaner-active_record.
%endif


%if_enabled    devel
%package       -n gem-database-cleaner-active-record-devel
Version:       2.2.0
Release:       alt1
Summary:       Strategies for cleaning databases using ActiveRecord. Can be used to ensure a clean state for testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета database_cleaner-active_record
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(database_cleaner-active_record) = 2.2.0
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(codecov) >= 0
Requires:      gem(mysql2) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(rails) >= 5.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(trilogy) >= 0
Conflicts:     gem(rails) >= 8

%description   -n gem-database-cleaner-active-record-devel
Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing development package.

%description   -n gem-database-cleaner-active-record-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета database_cleaner-active_record.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-database-cleaner-active-record-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-database-cleaner-active-record-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Tue Feb 04 2025 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 2.0.1 -> 2.2.0

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
