%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sidekiq

Name:          gem-sidekiq
Version:       7.3.8
Release:       alt1
Summary:       Simple, efficient background processing for Ruby
License:       LGPL-3.0
Group:         Development/Ruby
Url:           http://sidekiq.org
Vcs:           https://github.com/mperham/sidekiq.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(after_commit_everywhere) >= 0
BuildRequires: gem(connection_pool) >= 2.3.0
BuildRequires: gem(rack) >= 2.2.4
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redis-client) >= 0.22.2
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sqlite3) >= 1.4
BuildRequires: gem(standard) >= 0
BuildRequires: gem(actionmailer) >= 7.1.0
BuildRequires: gem(actionpack) >= 7.1.0
BuildRequires: gem(activejob) >= 7.1.0
BuildRequires: gem(activerecord) >= 7.1.0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(csv) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(maxitest) >= 0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(railties) >= 7.1.0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(actionmailer) >= 7.2
BuildConflicts: gem(actionpack) >= 7.2
BuildConflicts: gem(activejob) >= 7.2
BuildConflicts: gem(activerecord) >= 7.2
BuildConflicts: gem(railties) >= 7.2
BuildConflicts: gem(sqlite3) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names bare
Requires:      ruby >= 2.7.0
Requires:      gem(base64) >= 0
Requires:      gem(connection_pool) >= 2.3.0
Requires:      gem(logger) >= 0
Requires:      gem(rack) >= 2.2.4
Requires:      gem(redis-client) >= 0.22.2
Provides:      gem(sidekiq) = 7.3.8

%description
Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.


%package       -n sidekiq
Version:       7.3.8
Release:       alt1
Summary:       Simple, efficient background processing for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sidekiq
Group:         Other
BuildArch:     noarch

Requires:      gem(sidekiq) = 7.3.8

%description   -n sidekiq
Simple, efficient background processing for Ruby executable(s).

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n sidekiq -l ru_RU.UTF-8
Исполнямка для самоцвета sidekiq.


%if_enabled    doc
%package       -n gem-sidekiq-doc
Version:       7.3.8
Release:       alt1
Summary:       Simple, efficient background processing for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sidekiq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sidekiq) = 7.3.8

%description   -n gem-sidekiq-doc
Simple, efficient background processing for Ruby documentation files.

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n gem-sidekiq-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sidekiq.
%endif


%if_enabled    devel
%package       -n gem-sidekiq-devel
Version:       7.3.8
Release:       alt1
Summary:       Simple, efficient background processing for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sidekiq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sidekiq) = 7.3.8
Requires:      gem(maxitest) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(actionmailer) >= 7.1
Requires:      gem(actionpack) >= 7.1
Requires:      gem(activejob) >= 7.1
Requires:      gem(activerecord) >= 7.1
Requires:      gem(after_commit_everywhere) >= 0
Requires:      gem(csv) >= 0
Requires:      gem(railties) >= 7.1
Requires:      gem(rake) >= 0
Requires:      gem(sqlite3) >= 1.7
Requires:      gem(yard) >= 0
Conflicts:     gem(actionmailer) >= 8
Conflicts:     gem(actionpack) >= 8
Conflicts:     gem(activejob) >= 8
Conflicts:     gem(activerecord) >= 8
Conflicts:     gem(railties) >= 8
Conflicts:     gem(sqlite3) >= 2

%description   -n gem-sidekiq-devel
Simple, efficient background processing for Ruby development package.

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n gem-sidekiq-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sidekiq.
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
%doc LICENSE.txt README.md COMM-LICENSE.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n sidekiq
%doc LICENSE.txt README.md COMM-LICENSE.txt
%_bindir/sidekiq
%_bindir/sidekiqmon

%if_enabled    doc
%files         -n gem-sidekiq-doc
%doc LICENSE.txt README.md COMM-LICENSE.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sidekiq-devel
%doc LICENSE.txt README.md COMM-LICENSE.txt
%endif


%changelog
* Wed Jan 22 2025 Pavel Skrylev <majioa@altlinux.org> 7.3.8-alt1
- ^ 6.5.12 -> 7.3.8

* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 6.5.12-alt1
- ^ 6.4.1 -> 6.5.12

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 6.4.1-alt1
- ^ 5.2.8 -> 6.4.1

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1.1
- * gem deps for rack to ~> 2.0

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
