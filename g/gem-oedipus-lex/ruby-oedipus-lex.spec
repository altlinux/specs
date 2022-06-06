%define        gemname oedipus_lex

Name:          gem-oedipus-lex
Version:       2.6.0
Release:       alt1
Summary:       This is not your father's lexer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/oedipus_lex
Vcs:           https://github.com/seattlerb/oedipus_lex.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names oedipus_lex,oedipus-lex
Obsoletes:     ruby-oedipus-lex < %EVR
Provides:      ruby-oedipus-lex = %EVR
Provides:      gem(oedipus_lex) = 2.6.0


%description
Oedipus Lex is a lexer generator in the same family as Rexical and Rex. Oedipus
Lex is my independent lexer fork of Rexical. Rexical was in turn a fork of Rex.
We've been unable to contact the author of rex in order to take it over, fix it
up, extend it, and relicense it to MIT. So, Oedipus was written clean-room in
order to bypass licensing constraints (and because bootstrapping is fun).


%package       -n gem-oedipus-lex-doc
Version:       2.6.0
Release:       alt1
Summary:       This is not your father's lexer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oedipus_lex
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oedipus_lex) = 2.6.0

%description   -n gem-oedipus-lex-doc
This is not your father's lexer documentation files.

Oedipus Lex is a lexer generator in the same family as Rexical and Rex. Oedipus
Lex is my independent lexer fork of Rexical. Rexical was in turn a fork of Rex.
We've been unable to contact the author of rex in order to take it over, fix it
up, extend it, and relicense it to MIT. So, Oedipus was written clean-room in
order to bypass licensing constraints (and because bootstrapping is fun).

%description   -n gem-oedipus-lex-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oedipus_lex.


%package       -n gem-oedipus-lex-devel
Version:       2.6.0
Release:       alt1
Summary:       This is not your father's lexer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oedipus_lex
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oedipus_lex) = 2.6.0

%description   -n gem-oedipus-lex-devel
This is not your father's lexer development package.

Oedipus Lex is a lexer generator in the same family as Rexical and Rex. Oedipus
Lex is my independent lexer fork of Rexical. Rexical was in turn a fork of Rex.
We've been unable to contact the author of rex in order to take it over, fix it
up, extend it, and relicense it to MIT. So, Oedipus was written clean-room in
order to bypass licensing constraints (and because bootstrapping is fun).

%description   -n gem-oedipus-lex-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oedipus_lex.


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

%files         -n gem-oedipus-lex-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-oedipus-lex-devel
%doc README.rdoc


%changelog
* Wed Apr 06 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- ^ 2.5.2 -> 2.6.0

* Thu Nov 12 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- ^ 2.5.1 -> 2.5.2
- ! fake provides

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- > Ruby Policy 2.0
- ^ 2.5.0 -> 2.5.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
