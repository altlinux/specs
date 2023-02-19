%define        gemname crass

Name:          gem-crass
Version:       1.0.6
Release:       alt1
Summary:       A Ruby CSS parser that's fully compliant with the CSS Syntax Level 3 specification
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rgrove/crass/
Vcs:           https://github.com/rgrove/crass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.0.8
BuildRequires: gem(rake) >= 10.1.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Obsoletes:     ruby-crass < %EVR
Provides:      ruby-crass = %EVR
Provides:      gem(crass) = 1.0.6


%description
Crass is a Ruby CSS parser that's fully compliant with the CSS Syntax Level 3
specification.

Features:
* Pure Ruby, with no runtime dependencies other than Ruby 1.9.x or higher.
* Tokenizes and parses CSS according to the rules defined in the 14 November
  2014 editor's draft of the CSS Syntax Level 3 specification.
* Extremely tolerant of broken or invalid CSS. If a browser can handle it, Crass
  should be able to handle it too.
* Optionally includes comments in the token stream.
* Optionally preserves certain CSS hacks, such as the IE "*" hack, which would
  otherwise be discarded according to CSS3 tokenizing rules.
* Capable of serializing the parse tree back to CSS while maintaining all
  original whitespace, comments, and indentation.


%package       -n gem-crass-doc
Version:       1.0.6
Release:       alt1
Summary:       A Ruby CSS parser that's fully compliant with the CSS Syntax Level 3 specification documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета crass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(crass) = 1.0.6

%description   -n gem-crass-doc
A Ruby CSS parser that's fully compliant with the CSS Syntax Level 3
specification documentation files.

Crass is a Ruby CSS parser that's fully compliant with the CSS Syntax Level 3
specification.

Features:
* Pure Ruby, with no runtime dependencies other than Ruby 1.9.x or higher.
* Tokenizes and parses CSS according to the rules defined in the 14 November
  2014 editor's draft of the CSS Syntax Level 3 specification.
* Extremely tolerant of broken or invalid CSS. If a browser can handle it, Crass
  should be able to handle it too.
* Optionally includes comments in the token stream.
* Optionally preserves certain CSS hacks, such as the IE "*" hack, which would
  otherwise be discarded according to CSS3 tokenizing rules.
* Capable of serializing the parse tree back to CSS while maintaining all
  original whitespace, comments, and indentation.

%description   -n gem-crass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета crass.


%package       -n gem-crass-devel
Version:       1.0.6
Release:       alt1
Summary:       A Ruby CSS parser that's fully compliant with the CSS Syntax Level 3 specification development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета crass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(crass) = 1.0.6
Requires:      gem(minitest) >= 5.0.8
Requires:      gem(rake) >= 10.1.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14

%description   -n gem-crass-devel
A Ruby CSS parser that's fully compliant with the CSS Syntax Level 3
specification development package.

Crass is a Ruby CSS parser that's fully compliant with the CSS Syntax Level 3
specification.

Features:
* Pure Ruby, with no runtime dependencies other than Ruby 1.9.x or higher.
* Tokenizes and parses CSS according to the rules defined in the 14 November
  2014 editor's draft of the CSS Syntax Level 3 specification.
* Extremely tolerant of broken or invalid CSS. If a browser can handle it, Crass
  should be able to handle it too.
* Optionally includes comments in the token stream.
* Optionally preserves certain CSS hacks, such as the IE "*" hack, which would
  otherwise be discarded according to CSS3 tokenizing rules.
* Capable of serializing the parse tree back to CSS while maintaining all
  original whitespace, comments, and indentation.

%description   -n gem-crass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета crass.


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

%files         -n gem-crass-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-crass-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt1
- ^ 1.0.5 -> 1.0.6

* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- ^ 1.0.4 -> 1.0.5

* Tue May 04 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- FTBFS: Set correct python3 library directory for python scripts.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
