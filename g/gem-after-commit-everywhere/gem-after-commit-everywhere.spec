%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname after_commit_everywhere

Name:          gem-after-commit-everywhere
Version:       1.4.0
Release:       alt1
Summary:       Executes code after database commit wherever you want in your application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Envek/after_commit_everywhere
Vcs:           https://github.com/envek/after_commit_everywhere.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(isolator) >= 0.7
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-rails) >= 0
BuildRequires: gem(rubocop) >= 0.81.0
BuildRequires: gem(sqlite3) >= 1.3.6
BuildRequires: gem(yard) >= 0
BuildRequires: gem(activerecord) >= 4.2
BuildRequires: gem(activesupport) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(isolator) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(sqlite3) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency isolator < 2
Requires:      gem(activerecord) >= 4.2
Requires:      gem(activesupport) >= 0
Provides:      gem(after_commit_everywhere) = 1.4.0


%description
Brings before_commit, after_commit, and after_rollback transactional callbacks
outside of your ActiveRecord models.


%if_enabled    doc
%package       -n gem-after-commit-everywhere-doc
Version:       1.4.0
Release:       alt1
Summary:       Executes code after database commit wherever you want in your application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета after_commit_everywhere
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(after_commit_everywhere) = 1.4.0

%description   -n gem-after-commit-everywhere-doc
Executes code after database commit wherever you want in your application
documentation files.

Brings before_commit, after_commit, and after_rollback transactional callbacks
outside of your ActiveRecord models.

%description   -n gem-after-commit-everywhere-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета after_commit_everywhere.
%endif


%if_enabled    devel
%package       -n gem-after-commit-everywhere-devel
Version:       1.4.0
Release:       alt1
Summary:       Executes code after database commit wherever you want in your application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета after_commit_everywhere
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(after_commit_everywhere) = 1.4.0
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 2.0
Requires:      gem(isolator) >= 0.7
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rails) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-rails) >= 0
Requires:      gem(rubocop) >= 0.81.0
Requires:      gem(sqlite3) >= 1.3.6
Requires:      gem(yard) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(isolator) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(sqlite3) >= 2

%description   -n gem-after-commit-everywhere-devel
Executes code after database commit wherever you want in your application
development package.

Brings before_commit, after_commit, and after_rollback transactional callbacks
outside of your ActiveRecord models.

%description   -n gem-after-commit-everywhere-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета after_commit_everywhere.
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
%files         -n gem-after-commit-everywhere-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-after-commit-everywhere-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with Ruby Policy 2.0
