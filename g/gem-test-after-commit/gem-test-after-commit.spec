%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname test_after_commit

Name:          gem-test-after-commit
Version:       1.2.2
Release:       alt1
Summary:       makes after_commit callbacks testable in Rails 3+ with transactional_fixtures
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/test_after_commit
Vcs:           https://github.com/grosser/test_after_commit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(wwtd) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rails-observers) >= 0
BuildRequires: gem(activerecord) >= 3.2
BuildConflicts: gem(activerecord) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activerecord < 7
Requires:      gem(activerecord) >= 3.2
Conflicts:     gem(activerecord) >= 7
Provides:      gem(test_after_commit) = 1.2.2


%description
makes after_commit callbacks testable in Rails 3+ with transactional_fixtures.


%if_enabled    doc
%package       -n gem-test-after-commit-doc
Version:       1.2.2
Release:       alt1
Summary:       makes after_commit callbacks testable in Rails 3+ with transactional_fixtures documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test_after_commit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test_after_commit) = 1.2.2

%description   -n gem-test-after-commit-doc
makes after_commit callbacks testable in Rails 3+ with transactional_fixtures
documentation files.

%description   -n gem-test-after-commit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test_after_commit.
%endif


%if_enabled    devel
%package       -n gem-test-after-commit-devel
Version:       1.2.2
Release:       alt1
Summary:       makes after_commit callbacks testable in Rails 3+ with transactional_fixtures development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test_after_commit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test_after_commit) = 1.2.2
Requires:      gem(wwtd) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rails-observers) >= 0

%description   -n gem-test-after-commit-devel
makes after_commit callbacks testable in Rails 3+ with transactional_fixtures
development package.

%description   -n gem-test-after-commit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test_after_commit.
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
%doc Readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-test-after-commit-doc
%doc Readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-test-after-commit-devel
%doc Readme.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with Ruby Policy 2.0
