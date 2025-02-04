%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rainbow

Name:          gem-rainbow
Version:       3.1.1
Release:       alt1
Summary:       Colorize printed text on ANSI terminals
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sickill/rainbow
Vcs:           https://github.com/sickill/rainbow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(bundler) >= 3
%if_enabled check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(mutant-rspec) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 1.7.0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.4.0
Provides:      gem(rainbow) = 3.1.1

%description
Rainbow is a ruby gem for colorizing printed text on ANSI terminals.

It provides a string presenter object, which adds several methods to your
strings for wrapping them in ANSI escape codes. These codes when printed in a
terminal change text attributes like text color, background color, intensity
etc.


%if_enabled    doc
%package       -n gem-rainbow-doc
Version:       3.1.1
Release:       alt1
Summary:       Colorize printed text on ANSI terminals documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rainbow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rainbow) = 3.1.1

%description   -n gem-rainbow-doc
Colorize printed text on ANSI terminals documentation files.

Rainbow is a ruby gem for colorizing printed text on ANSI terminals.

It provides a string presenter object, which adds several methods to your
strings for wrapping them in ANSI escape codes. These codes when printed in a
terminal change text attributes like text color, background color, intensity
etc.

%description   -n gem-rainbow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rainbow.
%endif


%if_enabled    devel
%package       -n gem-rainbow-devel
Version:       3.1.1
Release:       alt1
Summary:       Colorize printed text on ANSI terminals development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rainbow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rainbow) = 3.1.1
Requires:      gem(bundler) >= 1.3
Requires:      gem(coveralls) >= 0
Requires:      gem(mutant-rspec) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 1.7.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rubocop) >= 2

%description   -n gem-rainbow-devel
Colorize printed text on ANSI terminals development package.

Rainbow is a ruby gem for colorizing printed text on ANSI terminals.

It provides a string presenter object, which adds several methods to your
strings for wrapping them in ANSI escape codes. These codes when printed in a
terminal change text attributes like text color, background color, intensity
etc.

%description   -n gem-rainbow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rainbow.
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
%doc Changelog.md LICENSE README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rainbow-doc
%doc Changelog.md LICENSE README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rainbow-devel
%doc Changelog.md LICENSE README.markdown
%endif


%changelog
* Wed Jan 22 2025 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- ^ 3.1.0 -> 3.1.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.0 -> 3.1.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
