%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-sprint

Name:          gem-minitest-sprint
Version:       1.3.0
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-sprint
Vcs:           https://github.com/seattlerb/minitest-sprint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(path_expander) >= 1.1
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(path_expander) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(path_expander) >= 1.1
Conflicts:     gem(path_expander) >= 2
Provides:      gem(minitest-sprint) = 1.3.0


%description
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures.


%package       -n minitest
Version:       1.3.0
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitest-sprint
Group:         Other
BuildArch:     noarch

Requires:      gem(minitest-sprint) = 1.3.0

%description   -n minitest
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures executable(s).

%description   -n minitest -l ru_RU.UTF-8
Исполнямка для самоцвета minitest-sprint.


%if_enabled    doc
%package       -n gem-minitest-sprint-doc
Version:       1.3.0
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-sprint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-sprint) = 1.3.0

%description   -n gem-minitest-sprint-doc
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures documentation files.

%description   -n gem-minitest-sprint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-sprint.
%endif


%if_enabled    devel
%package       -n gem-minitest-sprint-devel
Version:       1.3.0
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-sprint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-sprint) = 1.3.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-minitest-sprint-devel
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures development package.

%description   -n gem-minitest-sprint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-sprint.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n minitest
%doc README.rdoc
%_bindir/minitest

%if_enabled    doc
%files         -n gem-minitest-sprint-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-sprint-devel
%doc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.2 -> 1.3.0

* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with Ruby Policy 2.0
