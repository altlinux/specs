%define        gemname database_cleaner-active_record

Name:          gem-database-cleaner-active-record
Version:       2.0.1
Release:       alt1
Summary:       Strategies for cleaning databases using ActiveRecord. Can be used to ensure a clean state for testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DatabaseCleaner/database_cleaner-active_record
Vcs:           https://github.com/databasecleaner/database_cleaner-active_record.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(database_cleaner-core) >= 2.0.0 gem(database_cleaner-core) < 2.1
BuildRequires: gem(activerecord) >= 5.a
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(mysql2) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(sqlite3) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(database_cleaner-core) >= 2.0.0 gem(database_cleaner-core) < 2.1
Requires:      gem(activerecord) >= 5.a
Provides:      gem(database_cleaner-active_record) = 2.0.1


%description
Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing.


%package       -n gem-database-cleaner-active-record-doc
Version:       2.0.1
Release:       alt1
Summary:       Strategies for cleaning databases using ActiveRecord. Can be used to ensure a clean state for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета database_cleaner-active_record
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(database_cleaner-active_record) = 2.0.1

%description   -n gem-database-cleaner-active-record-doc
Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing documentation files.

Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing.

%description   -n gem-database-cleaner-active-record-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета database_cleaner-active_record.


%package       -n gem-database-cleaner-active-record-devel
Version:       2.0.1
Release:       alt1
Summary:       Strategies for cleaning databases using ActiveRecord. Can be used to ensure a clean state for testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета database_cleaner-active_record
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(database_cleaner-active_record) = 2.0.1
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(appraisal) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 0
Requires:      gem(mysql2) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(sqlite3) >= 0

%description   -n gem-database-cleaner-active-record-devel
Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing development package.

Strategies for cleaning databases using ActiveRecord. Can be used to ensure a
clean state for testing.

%description   -n gem-database-cleaner-active-record-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета database_cleaner-active_record.


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

%files         -n gem-database-cleaner-active-record-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-database-cleaner-active-record-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
