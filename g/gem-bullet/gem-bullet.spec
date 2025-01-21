%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname bullet

Name:          gem-bullet
Version:       8.0.0
Release:       alt1
Summary:       help to kill N+1 queries and unused eager loading
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flyerhzm/bullet
Vcs:           https://github.com/flyerhzm/bullet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 3.0.0
BuildRequires: gem(uniform_notifier) >= 1.11
BuildConflicts: gem(uniform_notifier) >= 2
%if_enabled check
BuildRequires: gem(activerecord-import) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(sqlite3) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      rubygems >= 1.3.6
Requires:      gem(activesupport) >= 3.0.0
Requires:      gem(uniform_notifier) >= 1.11
Conflicts:     gem(uniform_notifier) >= 2
Provides:      bullet = %EVR
Provides:      gem(bullet) = 8.0.0

%description
help to kill N+1 queries and unused eager loading.


%if_enabled    doc
%package       -n gem-bullet-doc
Version:       8.0.0
Release:       alt1
Summary:       help to kill N+1 queries and unused eager loading documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bullet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bullet) = 8.0.0

%description   -n gem-bullet-doc
help to kill N+1 queries and unused eager loading documentation files.

%description   -n gem-bullet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bullet.
%endif


%if_enabled    devel
%package       -n gem-bullet-devel
Version:       8.0.0
Release:       alt1
Summary:       help to kill N+1 queries and unused eager loading development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bullet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bullet) = 8.0.0
Requires:      gem(activerecord-import) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(guard) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(rails) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(sqlite3) >= 0

%description   -n gem-bullet-devel
help to kill N+1 queries and unused eager loading development package.

%description   -n gem-bullet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bullet.
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
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-bullet-doc
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bullet-devel
%doc CHANGELOG.md MIT-LICENSE README.md
%endif


%changelog
* Mon Jan 20 2025 Pavel Skrylev <majioa@altlinux.org> 8.0.0-alt1
- ^ 6.1.5 -> 8.0.0

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.5-alt1
- ^ 6.1.4 -> 6.1.5

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 6.1.4-alt1
- + packaged gem with Ruby Policy 2.0
