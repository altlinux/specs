%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sidekiq

Name:          gem-sidekiq
Version:       7.3.10
Release:       alt1
Summary:       Simple, efficient background processing for Ruby
License:       LGPL-3.0
Group:         Development/Ruby
Url:           http://sidekiq.org
Vcs:           https://github.com/mperham/sidekiq.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(actionmailer) >= 7.1
BuildRequires: gem(actionpack) >= 7.1
BuildRequires: gem(activejob) >= 7.1
BuildRequires: gem(activerecord) >= 7.1
BuildRequires: gem(after_commit_everywhere) >= 0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(connection_pool) >= 2.3.0
BuildRequires: gem(csv) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(maxitest) >= 0
BuildRequires: gem(rack) >= 2.2.4
BuildRequires: gem(railties) >= 7.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redis-client) >= 0.23.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sqlite3) >= 2.2
BuildRequires: gem(standard) >= 0
BuildRequires: gem(vernier) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(yard) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names bare
%ruby_use_gem_dependency rack >= 3.1.7
%ruby_use_gem_dependency railties >= 7.1
%ruby_use_gem_dependency activejob >= 7.1
%ruby_use_gem_dependency activerecord >= 7.1
%ruby_use_gem_dependency actionmailer >= 7.1
%ruby_use_gem_dependency actionpack >= 7.1
%ruby_use_gem_dependency redis-client >= 0.23
%ruby_use_gem_dependency sqlite3 >= 2.2
%ruby_use_gem_dependency connection_pool >= 2.3.0
Requires:      ruby >= 3.2.0
Requires:      gem(base64) >= 0
Requires:      gem(connection_pool) >= 2.3.0
Requires:      gem(logger) >= 0
Requires:      gem(rack) >= 2.2.4
Requires:      gem(redis-client) >= 0.23.0
Requires:      gem(vernier) >= 0
Requires:      gem(webrick) >= 0
Provides:      gem(sidekiq) = 7.3.10

%description
Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.


%package       -n sidekiq
Version:       7.3.10
Release:       alt1
Summary:       Simple, efficient background processing for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sidekiq
Group:         Other
BuildArch:     noarch

Requires:      gem(sidekiq) = 7.3.10
Requires:      gem(redis-client) >= 0.23.0
Requires:      gem(vernier) >= 0
Requires:      gem(webrick) >= 0

%description   -n sidekiq
Simple, efficient background processing for Ruby executable(s).

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n sidekiq -l ru_RU.UTF-8
Исполнямка для самоцвета sidekiq.


%if_enabled    doc
%package       -n gem-sidekiq-doc
Version:       7.3.10
Release:       alt1
Summary:       Simple, efficient background processing for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sidekiq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sidekiq) = 7.3.10

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
Version:       7.3.10
Release:       alt1
Summary:       Simple, efficient background processing for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sidekiq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sidekiq) = 7.3.10
Requires:      gem(actionmailer) >= 7.1
Requires:      gem(actionpack) >= 7.1
Requires:      gem(activejob) >= 7.1
Requires:      gem(activerecord) >= 7.1
Requires:      gem(after_commit_everywhere) >= 0
Requires:      gem(base64) >= 0
Requires:      gem(connection_pool) >= 2.3.0
Requires:      gem(csv) >= 0
Requires:      gem(debug) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(maxitest) >= 0
Requires:      gem(rack) >= 2.2.4
Requires:      gem(railties) >= 7.1
Requires:      gem(rake) >= 0
Requires:      gem(redis-client) >= 0.23.0
Requires:      gem(simplecov) >= 0
Requires:      gem(sqlite3) >= 2.2
Requires:      gem(standard) >= 0
Requires:      gem(vernier) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(yard) >= 0

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
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 7.3.10-alt1
- ^ 7.3.9 -> 7.3.10
- ! relaxed deps to rails, and to rack gems
- v downgraded gem reqs for some rails' ones

* Fri Oct 31 2025 Pavel Skrylev <majioa@altlinux.org> 7.3.9-alt1
- ^ 7.3.8 -> 7.3.9

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
