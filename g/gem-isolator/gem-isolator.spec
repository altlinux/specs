%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname isolator

Name:          gem-isolator
Version:       1.0.1
Release:       alt1
Summary:       Detect non-atomic interactions within DB transactions
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/palkan/isolator
Vcs:           https://github.com/palkan/isolator.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(debug) >= 0
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-rails) >= 3.0
BuildRequires: gem(minitest) >= 5.10.0
BuildRequires: gem(sidekiq) >= 5.0
BuildRequires: gem(webmock) >= 3.1
BuildRequires: gem(test_after_commit) >= 1.1
BuildRequires: gem(resque) >= 0
BuildRequires: gem(fakeredis) >= 0
BuildRequires: gem(resque-scheduler) >= 0
BuildRequires: gem(sucker_punch) >= 0
BuildRequires: gem(database_cleaner) >= 0
BuildRequires: gem(database_cleaner-active_record) >= 0
BuildRequires: gem(after_commit_everywhere) >= 0
BuildRequires: gem(uniform_notifier) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(standard) >= 1.28
BuildRequires: gem(rubocop-md) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rails) >= 6.1.3.2
BuildRequires: gem(sqlite3) >= 1.4.0
BuildRequires: gem(sniffer) >= 0.5.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(sidekiq) >= 7
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(test_after_commit) >= 2
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(rails) >= 8
BuildConflicts: gem(sqlite3) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
%ruby_use_gem_dependency sidekiq >= 6.4.1,sidekiq < 7
%ruby_use_gem_dependency sqlite3 >= 1.4,sqlite3 < 2
Requires:      gem(sniffer) >= 0.5.0
Provides:      gem(isolator) = 1.0.1


%description
Detect non-atomic interactions within DB transactions.


%if_enabled    doc
%package       -n gem-isolator-doc
Version:       1.0.1
Release:       alt1
Summary:       Detect non-atomic interactions within DB transactions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета isolator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(isolator) = 1.0.1

%description   -n gem-isolator-doc
Detect non-atomic interactions within DB transactions documentation files.

%description   -n gem-isolator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета isolator.
%endif


%if_enabled    devel
%package       -n gem-isolator-devel
Version:       1.0.1
Release:       alt1
Summary:       Detect non-atomic interactions within DB transactions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета isolator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(isolator) = 1.0.1
Requires:      gem(debug) >= 0
Requires:      gem(bundler) >= 1.16
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-rails) >= 3.0
Requires:      gem(minitest) >= 5.10.0
Requires:      gem(sidekiq) >= 5.0
Requires:      gem(webmock) >= 3.1
Requires:      gem(test_after_commit) >= 1.1
Requires:      gem(resque) >= 0
Requires:      gem(fakeredis) >= 0
Requires:      gem(resque-scheduler) >= 0
Requires:      gem(sucker_punch) >= 0
Requires:      gem(database_cleaner) >= 0
Requires:      gem(database_cleaner-active_record) >= 0
Requires:      gem(after_commit_everywhere) >= 0
Requires:      gem(uniform_notifier) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(net-smtp) >= 0
Requires:      gem(standard) >= 1.28
Requires:      gem(rubocop-md) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rails) >= 6.1.3.2
Requires:      gem(sqlite3) >= 1.4.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(sidekiq) >= 7
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(test_after_commit) >= 2
Conflicts:     gem(standard) >= 2
Conflicts:     gem(rails) >= 8
Conflicts:     gem(sqlite3) >= 2

%description   -n gem-isolator-devel
Detect non-atomic interactions within DB transactions development package.

%description   -n gem-isolator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета isolator.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-isolator-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-isolator-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
