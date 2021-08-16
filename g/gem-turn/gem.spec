%define        gemname turn

Name:          gem-turn
Version:       0.9.7
Release:       alt1
Summary:       Test Reporters (New) -- new output formats for Testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/turn-project/turn
Vcs:           https://github.com/turn-project/turn.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ansi) >= 0
BuildRequires: gem(minitest) >= 4 gem(minitest) < 6
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(indexer) >= 0
BuildRequires: gem(mast) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_ignore_names autotest
Requires:      gem(ansi) >= 0
Requires:      gem(minitest) >= 4 gem(minitest) < 6
Provides:      gem(turn) = 0.9.7


%description
Turn provides a set of alternative runners for MiniTest, both colorful and
informative.


%package       -n turn
Version:       0.9.7
Release:       alt1
Summary:       Test Reporters (New) -- new output formats for Testing executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета turn
Group:         Other
BuildArch:     noarch

Requires:      gem(turn) = 0.9.7

%description   -n turn
Test Reporters (New) -- new output formats for Testing executable(s).

Turn provides a set of alternative runners for MiniTest, both colorful and
informative.

%description   -n turn -l ru_RU.UTF-8
Исполнямка для самоцвета turn.


%package       -n gem-turn-doc
Version:       0.9.7
Release:       alt1
Summary:       Test Reporters (New) -- new output formats for Testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета turn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(turn) = 0.9.7

%description   -n gem-turn-doc
Test Reporters (New) -- new output formats for Testing documentation
files.

Turn provides a set of alternative runners for MiniTest, both colorful and
informative.

%description   -n gem-turn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета turn.


%package       -n gem-turn-devel
Version:       0.9.7
Release:       alt1
Summary:       Test Reporters (New) -- new output formats for Testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета turn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(turn) = 0.9.7
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(indexer) >= 0
Requires:      gem(mast) >= 0

%description   -n gem-turn-devel
Test Reporters (New) -- new output formats for Testing development
package.

Turn provides a set of alternative runners for MiniTest, both colorful and
informative.

%description   -n gem-turn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета turn.


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

%files         -n turn
%doc README.md
%_bindir/turn

%files         -n gem-turn-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-turn-devel
%doc README.md


%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.7-alt1
- + packaged gem with Ruby Policy 2.0
