%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop_challenger

Name:          gem-rubocop-challenger
Version:       2.11.1
Release:       alt1
Summary:       Make a clean your rubocop_todo.yml with CI
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ryz310/rubocop_challenger
Vcs:           https://github.com/ryz310/rubocop_challenger.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(pr_comet) >= 0.5.1
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rainbow) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec_junit_formatter) >= 0
BuildRequires: gem(rubocop) >= 0.87
BuildRequires: gem(rubocop-capybara) >= 0
BuildRequires: gem(rubocop-factory_bot) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rubocop-rspec_rails) >= 0
BuildRequires: gem(rubocop-thread_safety) >= 0
BuildRequires: gem(simplecov) = 0.22.0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(pr_comet) >= 0.8.0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names rubocop_challenger,rubocop-challenger
Requires:      ruby >= 3.0
Requires:      gem(pr_comet) >= 0.5.1
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rainbow) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rspec_junit_formatter) >= 0
Requires:      gem(rubocop) >= 0.87
Requires:      gem(rubocop-capybara) >= 0
Requires:      gem(rubocop-factory_bot) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rails) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rubocop-rspec_rails) >= 0
Requires:      gem(rubocop-thread_safety) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(pr_comet) >= 0.8.0
Provides:      gem(rubocop_challenger) = 2.11.1

%description
Make a clean your rubocop_todo.yml with CI


%package       -n rubocop-challenger
Version:       2.11.1
Release:       alt1
Summary:       Make a clean your rubocop_todo.yml with CI executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubocop_challenger
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop_challenger) = 2.11.1
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rspec_junit_formatter) >= 0

%description   -n rubocop-challenger
Make a clean your rubocop_todo.yml with CI executable(s).

%description   -n rubocop-challenger -l ru_RU.UTF-8
Исполнямка для самоцвета rubocop_challenger.


%if_enabled    doc
%package       -n gem-rubocop-challenger-doc
Version:       2.11.1
Release:       alt1
Summary:       Make a clean your rubocop_todo.yml with CI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop_challenger
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop_challenger) = 2.11.1

%description   -n gem-rubocop-challenger-doc
Make a clean your rubocop_todo.yml with CI documentation files.

%description   -n gem-rubocop-challenger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop_challenger.
%endif


%if_enabled    devel
%package       -n gem-rubocop-challenger-devel
Version:       2.11.1
Release:       alt1
Summary:       Make a clean your rubocop_todo.yml with CI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop_challenger
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop_challenger) = 2.11.1
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(simplecov) = 0.22.0
Conflicts:     gem(rake) >= 14

%description   -n gem-rubocop-challenger-devel
Make a clean your rubocop_todo.yml with CI development package.

%description   -n gem-rubocop-challenger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop_challenger.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rubocop-challenger
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%_bindir/rubocop_challenger

%if_enabled    doc
%files         -n gem-rubocop-challenger-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-challenger-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Wed Nov 05 2025 Pavel Skrylev <majioa@altlinux.org> 2.11.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
