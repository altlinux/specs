%define        gemname term-ansicolor

Name:          gem-term-ansicolor
Version:       1.7.1.1
Release:       alt0.1
Summary:       Ruby library that colors strings using ANSI escape sequences
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://flori.github.io/term-ansicolor/
Vcs:           https://github.com/flori/term-ansicolor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gem_hadar) >= 1.12.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(utils) >= 0
BuildRequires: gem(tins) >= 1.0
BuildConflicts: gem(gem_hadar) >= 2
BuildConflicts: gem(tins) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Requires:      gem(tins) >= 1.0
Conflicts:     gem(tins) >= 2
Obsoletes:     ruby-term-ansicolor < %EVR
Provides:      ruby-term-ansicolor = %EVR
Provides:      gem(term-ansicolor) = 1.7.1.1

%ruby_use_gem_version term-ansicolor:1.7.1.1

%description
This library can be used to color/decolor strings using ANSI escape sequences.


%package       -n term-utils
Version:       1.7.1.1
Release:       alt0.1
Summary:       Ruby library that colors strings using ANSI escape sequences executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета term-ansicolor
Group:         Other
BuildArch:     noarch

Requires:      gem(term-ansicolor) = 1.7.1.1

%description   -n term-utils
Ruby library that colors strings using ANSI escape sequences
executable(s).

This library can be used to color/decolor strings using ANSI escape sequences.

%description   -n term-utils -l ru_RU.UTF-8
Исполнямка для самоцвета term-ansicolor.


%package       -n gem-term-ansicolor-doc
Version:       1.7.1.1
Release:       alt0.1
Summary:       Ruby library that colors strings using ANSI escape sequences documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета term-ansicolor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(term-ansicolor) = 1.7.1.1

%description   -n gem-term-ansicolor-doc
Ruby library that colors strings using ANSI escape sequences documentation
files.

This library can be used to color/decolor strings using ANSI escape sequences.

%description   -n gem-term-ansicolor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета term-ansicolor.


%package       -n gem-term-ansicolor-devel
Version:       1.7.1.1
Release:       alt0.1
Summary:       Ruby library that colors strings using ANSI escape sequences development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета term-ansicolor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(term-ansicolor) = 1.7.1.1
Requires:      gem(gem_hadar) >= 1.12.0
Requires:      gem(simplecov) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(utils) >= 0
Conflicts:     gem(gem_hadar) >= 2

%description   -n gem-term-ansicolor-devel
Ruby library that colors strings using ANSI escape sequences development
package.

This library can be used to color/decolor strings using ANSI escape sequences.

%description   -n gem-term-ansicolor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета term-ansicolor.


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

%files         -n term-utils
%doc README.md
%_bindir/term_cdiff
%_bindir/term_colortab
%_bindir/term_decolor
%_bindir/term_display
%_bindir/term_mandel
%_bindir/term_snow

%files         -n gem-term-ansicolor-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-term-ansicolor-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.7.1.1-alt0.1
- ^ 1.7.1 -> 1.7.1[1]

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1.1
- ! spec

* Fri Mar 01 2019 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- Bump to 1.7.1;
- Use Ruby Policy 2.0.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1.2
- Rebuild for new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.4-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 25 2009 Igor Zubkov <icesik@altlinux.org> 1.0.4-alt1
- build for Sisyphus
