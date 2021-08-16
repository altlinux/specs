%define        gemname database_cleaner

Name:          gem-database-cleaner
Version:       2.0.1
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DatabaseCleaner/database_cleaner
Vcs:           https://github.com/databasecleaner/database_cleaner.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(database_cleaner-active_record) >= 2.0.0 gem(database_cleaner-active_record) < 2.1
Provides:      gem(database_cleaner) = 2.0.1


%description
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing.


%package       -n gem-database-cleaner-core
Version:       2.0.1
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(database_cleaner-core) = 2.0.1

%description   -n gem-database-cleaner-core
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing.


%package       -n gem-database-cleaner-core-doc
Version:       2.0.1
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета database_cleaner-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(database_cleaner-core) = 2.0.1

%description   -n gem-database-cleaner-core-doc
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing documentation files.

Strategies for cleaning databases. Can be used to ensure a clean slate for
testing.

%description   -n gem-database-cleaner-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета database_cleaner-core.


%package       -n gem-database-cleaner-doc
Version:       2.0.1
Release:       alt1
Summary:       Strategies for cleaning databases. Can be used to ensure a clean slate for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета database_cleaner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(database_cleaner) = 2.0.1

%description   -n gem-database-cleaner-doc
Strategies for cleaning databases. Can be used to ensure a clean slate for
testing documentation files.

Strategies for cleaning databases. Can be used to ensure a clean slate for
testing.

%description   -n gem-database-cleaner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета database_cleaner.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-database-cleaner-core
%doc README.markdown
%ruby_gemspecdir/database_cleaner-core-2.0.1.gemspec
%ruby_gemslibdir/database_cleaner-core-2.0.1

%files         -n gem-database-cleaner-core-doc
%doc README.markdown
%ruby_gemsdocdir/database_cleaner-core-2.0.1

%files         -n gem-database-cleaner-doc
%ruby_gemdocdir


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
