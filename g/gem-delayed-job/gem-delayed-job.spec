%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname delayed_job

Name:          gem-delayed-job
Version:       4.1.11
Release:       alt1
Summary:       Database-backed asynchronous priority queue system -- Extracted from Shopify
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/collectiveidea/delayed_job
Vcs:           https://github.com/collectiveidea/delayed_job.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(psych) >= 0
BuildRequires: gem(actionmailer) >= 3.0
BuildRequires: gem(activerecord) >= 3.0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-lcov) >= 0
BuildRequires: gem(zeitwerk) >= 0
BuildRequires: gem(rubocop) >= 0.25
BuildRequires: gem(activesupport) >= 3.0
BuildConflicts: gem(actionmailer) >= 8.0
BuildConflicts: gem(activerecord) >= 8.0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(activesupport) >= 8.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(activesupport) >= 3.0
Conflicts:     gem(activesupport) >= 8.0
Provides:      gem(delayed_job) = 4.1.11


%description
Delayed_job (or DJ) encapsulates the common pattern of asynchronously executing
longer tasks in the background. It is a direct extraction from Shopify where the
job table is responsible for a multitude of core tasks.


%if_enabled    doc
%package       -n gem-delayed-job-doc
Version:       4.1.11
Release:       alt1
Summary:       Database-backed asynchronous priority queue system -- Extracted from Shopify documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета delayed_job
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(delayed_job) = 4.1.11

%description   -n gem-delayed-job-doc
Database-backed asynchronous priority queue system -- Extracted from Shopify
documentation files.

Delayed_job (or DJ) encapsulates the common pattern of asynchronously executing
longer tasks in the background. It is a direct extraction from Shopify where the
job table is responsible for a multitude of core tasks.

%description   -n gem-delayed-job-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета delayed_job.
%endif


%if_enabled    devel
%package       -n gem-delayed-job-devel
Version:       4.1.11
Release:       alt1
Summary:       Database-backed asynchronous priority queue system -- Extracted from Shopify development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета delayed_job
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(delayed_job) = 4.1.11
Requires:      gem(rake) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(railties) >= 3.0
Requires:      gem(psych) >= 0
Requires:      gem(actionmailer) >= 3.0
Requires:      gem(activerecord) >= 3.0
Requires:      gem(net-smtp) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-lcov) >= 0
Requires:      gem(zeitwerk) >= 0
Requires:      gem(rubocop) >= 0.25
Conflicts:     gem(railties) >= 8.0
Conflicts:     gem(actionmailer) >= 8.0
Conflicts:     gem(activerecord) >= 8.0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-delayed-job-devel
Database-backed asynchronous priority queue system -- Extracted from Shopify
development package.

Delayed_job (or DJ) encapsulates the common pattern of asynchronously executing
longer tasks in the background. It is a direct extraction from Shopify where the
job table is responsible for a multitude of core tasks.

%description   -n gem-delayed-job-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета delayed_job.
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
%files         -n gem-delayed-job-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-delayed-job-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 4.1.11-alt1
- + packaged gem with Ruby Policy 2.0
