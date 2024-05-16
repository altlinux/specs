%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname delayed_job_active_record

Name:          gem-delayed-job-active-record
Version:       4.1.8
Release:       alt1
Summary:       ActiveRecord backend for DelayedJob
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/collectiveidea/delayed_job_active_record
Vcs:           https://github.com/collectiveidea/delayed_job_active_record.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mysql2) >= 0.4.5
BuildRequires: gem(pg) >= 0.18
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-lcov) >= 0.8.0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(activerecord) >= 3.0
BuildRequires: gem(delayed_job) >= 3.0
BuildConflicts: gem(mysql2) >= 1
BuildConflicts: gem(pg) >= 2
BuildConflicts: gem(activerecord) >= 8.0
BuildConflicts: gem(delayed_job) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency mysql2 >= 0.5.5,mysql2 < 1
%ruby_use_gem_dependency pg >= 1.3.5,pg < 2
Requires:      gem(activerecord) >= 3.0
Requires:      gem(delayed_job) >= 3.0
Conflicts:     gem(activerecord) >= 8.0
Conflicts:     gem(delayed_job) >= 5
Provides:      gem(delayed_job_active_record) = 4.1.8


%description
ActiveRecord backend for Delayed::Job, originally authored by Tobias Ljutke


%if_enabled    doc
%package       -n gem-delayed-job-active-record-doc
Version:       4.1.8
Release:       alt1
Summary:       ActiveRecord backend for DelayedJob documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета delayed_job_active_record
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(delayed_job_active_record) = 4.1.8

%description   -n gem-delayed-job-active-record-doc
ActiveRecord backend for DelayedJob documentation files.

ActiveRecord backend for Delayed::Job, originally authored by Tobias Ljutke

%description   -n gem-delayed-job-active-record-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета delayed_job_active_record.
%endif


%if_enabled    devel
%package       -n gem-delayed-job-active-record-devel
Version:       4.1.8
Release:       alt1
Summary:       ActiveRecord backend for DelayedJob development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета delayed_job_active_record
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(delayed_job_active_record) = 4.1.8
Requires:      gem(rake) >= 0
Requires:      gem(mysql2) >= 0.4.5
Requires:      gem(pg) >= 0.18
Requires:      gem(sqlite3) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-lcov) >= 0.8.0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rails) >= 0
Requires:      gem(rubocop-rspec) >= 0
Conflicts:     gem(mysql2) >= 1
Conflicts:     gem(pg) >= 2

%description   -n gem-delayed-job-active-record-devel
ActiveRecord backend for DelayedJob development package.

ActiveRecord backend for Delayed::Job, originally authored by Tobias Ljutke

%description   -n gem-delayed-job-active-record-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета delayed_job_active_record.
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
%files         -n gem-delayed-job-active-record-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-delayed-job-active-record-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 4.1.8-alt1
- + packaged gem with Ruby Policy 2.0
