%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname guard

Name:          gem-guard
Version:       2.20.1
Release:       alt1
Summary:       Guard keeps an eye on your file modifications
License:       MIT
Group:         Development/Ruby
Url:           https://guard.github.io/guard/
Vcs:           https://github.com/guard/guard.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(aruba) >= 0.14
BuildRequires: gem(formatador) >= 0.2.4
BuildRequires: gem(guard-cucumber) >= 2.1
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(listen) >= 2.7
BuildRequires: gem(logger) >= 1.6
BuildRequires: gem(lumberjack) >= 1.0.12
BuildRequires: gem(nenv) >= 0.1
BuildRequires: gem(notiffany) >= 0.0.6
BuildRequires: gem(pry) >= 0.13.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0.0
BuildRequires: gem(rubocop) >= 0.54.0
BuildRequires: gem(shellany) >= 0.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(thor) >= 0.18.1
BuildConflicts: gem(aruba) >= 3
BuildConflicts: gem(guard-cucumber) >= 4
BuildConflicts: gem(listen) >= 4.0
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(lumberjack) >= 3
BuildConflicts: gem(nenv) >= 1
BuildConflicts: gem(notiffany) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(shellany) >= 1
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency aruba >= 2.4.1,aruba < 3
%ruby_use_gem_dependency guard-cucumber >= 3.0.0,guard-cucumber < 4
%ruby_use_gem_dependency lumberjack >= 2.0.5,lumberjack < 3
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
Requires:      ruby >= 1.9.3
Requires:      gem(formatador) >= 0.2.4
Requires:      gem(listen) >= 2.7
Requires:      gem(logger) >= 1.6
Requires:      gem(lumberjack) >= 1.0.12
Requires:      gem(nenv) >= 0.1
Requires:      gem(notiffany) >= 0.0.6
Requires:      gem(pry) >= 0.13.0
Requires:      gem(rake) >= 0
Requires:      gem(shellany) >= 0.0
Requires:      gem(thor) >= 0.18.1
Conflicts:     gem(listen) >= 4.0
Conflicts:     gem(logger) >= 2
Conflicts:     gem(lumberjack) >= 3
Conflicts:     gem(nenv) >= 1
Conflicts:     gem(notiffany) >= 1
Conflicts:     gem(shellany) >= 1
Provides:      gem(guard) = 2.20.1

%description
Guard is a command line tool to easily handle events on file system
modifications.


%package       -n guard
Version:       2.20.1
Release:       alt1
Summary:       Guard keeps an eye on your file modifications executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета guard
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard) = 2.20.1
Requires:      gem(rake) >= 0

%description   -n guard
Guard keeps an eye on your file modifications executable(s).

%description   -n guard -l ru_RU.UTF-8
Исполнямка для самоцвета guard.


%if_enabled    doc
%package       -n gem-guard-doc
Version:       2.20.1
Release:       alt1
Summary:       Guard keeps an eye on your file modifications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета guard
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard) = 2.20.1

%description   -n gem-guard-doc
Guard keeps an eye on your file modifications documentation files.

%description   -n gem-guard-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета guard.
%endif


%if_enabled    devel
%package       -n gem-guard-devel
Version:       2.20.1
Release:       alt1
Summary:       Guard keeps an eye on your file modifications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета guard
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard) = 2.20.1
Requires:      gem(aruba) >= 0.14
Requires:      gem(guard-cucumber) >= 2.1
Requires:      gem(guard-rspec) >= 0
Requires:      gem(guard-rubocop) >= 0
Requires:      gem(rspec) >= 3.0.0
Requires:      gem(rubocop) >= 0.54.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(aruba) >= 3
Conflicts:     gem(guard-cucumber) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1

%description   -n gem-guard-devel
Guard keeps an eye on your file modifications development package.

%description   -n gem-guard-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета guard.
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
%doc CHANGELOG.md LICENSE README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n guard
%doc CHANGELOG.md LICENSE README.md CONTRIBUTING.md
%_bindir/guard
%_bindir/_guard-core
%_mandir/guard.*

%if_enabled    doc
%files         -n gem-guard-doc
%doc CHANGELOG.md LICENSE README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-guard-devel
%doc CHANGELOG.md LICENSE README.md CONTRIBUTING.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 2.20.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
