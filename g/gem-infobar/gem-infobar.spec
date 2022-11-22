%define        gemname infobar

Name:          gem-infobar
Version:       0.7.0
Release:       alt2
Summary:       Gem to display information about computations
License:       Unlicense
Group:         Development/Ruby
Url:           http://flori.github.com/infobar
Vcs:           https://github.com/flori/infobar.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gem_hadar) >= 1.11.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(tins) >= 1.28.0
BuildRequires: gem(term-ansicolor) >= 1.4
BuildRequires: gem(complex_config) >= 0.10
BuildRequires: gem(more_math) >= 0
BuildConflicts: gem(gem_hadar) >= 2
BuildConflicts: gem(tins) >= 2
BuildConflicts: gem(term-ansicolor) >= 2
BuildConflicts: gem(complex_config) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Requires:      gem(tins) >= 1.28.0
Requires:      gem(term-ansicolor) >= 1.4
Requires:      gem(complex_config) >= 0.10
Requires:      gem(more_math) >= 0
Conflicts:     gem(tins) >= 2
Conflicts:     gem(term-ansicolor) >= 2
Conflicts:     gem(complex_config) >= 1
Provides:      gem(infobar) = 0.7.0


%description
This gem displays progress of computations and additional information to the
terminal.


%package       -n gem-infobar-doc
Version:       0.7.0
Release:       alt2
Summary:       Gem to display information about computations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета infobar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(infobar) = 0.7.0

%description   -n gem-infobar-doc
Gem to display information about computations documentation files.

This gem displays progress of computations and additional information to the
terminal.

%description   -n gem-infobar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета infobar.


%package       -n gem-infobar-devel
Version:       0.7.0
Release:       alt2
Summary:       Gem to display information about computations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета infobar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(infobar) = 0.7.0
Requires:      gem(gem_hadar) >= 1.11.0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(rspec) >= 0
Conflicts:     gem(gem_hadar) >= 2

%description   -n gem-infobar-devel
Gem to display information about computations development package.

This gem displays progress of computations and additional information to the
terminal.

%description   -n gem-infobar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета infobar.


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

%files         -n gem-infobar-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-infobar-devel
%doc README.md


%changelog
* Tue Nov 22 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt2
- ! spec to conform proper handle requires/conflicts
- ! rename spec

* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0
