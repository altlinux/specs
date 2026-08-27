%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname turn

Name:          gem-turn
Version:       0.9.7.17
Release:       alt0.1
Summary:       Test Reporters (New) -- new output formats for Testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/turn-project/turn
Vcs:           https://github.com/turn-project/turn.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(ansi) >= 1.1
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0
Requires:      gem(ansi) >= 1.1
Requires:      gem(minitest) >= 5
Conflicts:     gem(minitest) >= 7
Provides:      gem(turn) = 0.9.7.17

%ruby_use_gem_version turn:0.9.7.17
%ruby_ignore_path_tokens autotest

%description
Turn provides a set of alternative runners for MiniTest, both colorful and
informative.


%package       -n turn
Version:       0.9.7.17
Release:       alt0.1
Summary:       Test Reporters (New) -- new output formats for Testing executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета turn
Group:         Other
BuildArch:     noarch

Requires:      gem(turn) = 0.9.7.17
Requires:      gem(ansi) >= 1.1
Requires:      gem(minitest) >= 5
Conflicts:     gem(minitest) >= 7

%description   -n turn
Test Reporters (New) -- new output formats for Testing executable(s).

Turn provides a set of alternative runners for MiniTest, both colorful and
informative.

%description   -n turn -l ru_RU.UTF-8
Исполнямка для самоцвета turn.


%if_enabled    doc
%package       -n gem-turn-doc
Version:       0.9.7.17
Release:       alt0.1
Summary:       Test Reporters (New) -- new output formats for Testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета turn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(turn) = 0.9.7.17

%description   -n gem-turn-doc
Test Reporters (New) -- new output formats for Testing documentation
files.

Turn provides a set of alternative runners for MiniTest, both colorful and
informative.

%description   -n gem-turn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета turn.
%endif


%if_enabled    devel
%package       -n gem-turn-devel
Version:       0.9.7.17
Release:       alt0.1
Summary:       Test Reporters (New) -- new output formats for Testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета turn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(turn) = 0.9.7.17
Requires:      gem(bundler) >= 1.3
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-turn-devel
Test Reporters (New) -- new output formats for Testing development
package.

Turn provides a set of alternative runners for MiniTest, both colorful and
informative.

%description   -n gem-turn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета turn.
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
%doc History.txt LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n turn
%doc History.txt LICENSE.txt README.md
%_bindir/turn

%if_enabled    doc
%files         -n gem-turn-doc
%doc History.txt LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-turn-devel
%doc History.txt LICENSE.txt README.md
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.7.17-alt0.1
- ^ 0.9.7 -> 0.9.7p17

* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.7-alt1
- + packaged gem with Ruby Policy 2.0
