%define        gemname parser

Name:          gem-parser
Version:       3.1.3.0
Release:       alt1
Summary:       A Ruby parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/whitequark/parser
Vcs:           https://github.com/whitequark/parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel6 >= 6.0
BuildRequires: racc
BuildRequires: gem(rake) >= 13.0.1 gem(rake) < 14
BuildRequires: gem(racc) >= 1.6.0
BuildRequires: gem(cliver) >= 0.3.2 gem(cliver) < 0.4
%if_with check
BuildRequires: gem(bundler) >= 1.15 gem(bundler) < 3
BuildRequires: gem(yard) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(minitest) >= 5.10 gem(minitest) < 6
BuildRequires: gem(simplecov) >= 0.15.1 gem(simplecov) < 1
BuildRequires: gem(gauntlet) >= 0
BuildRequires: gem(ast) >= 1.1 gem(ast) < 3.0
%endif
BuildConflicts: ragel6 >= 7.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency racc >= 1.6.0,racc < 2
%ruby_alias_names parser,parse,ruby-parse
Requires:      gem(ast) >= 1.1 gem(ast) < 3.0
Provides:      gem(parser) = 3.1.3.0

%ruby_on_build_rake_tasks generate_release

%description
Parser is a production-ready Ruby parser written in pure Ruby. It recognizes as
much or more code than Ripper, Melbourne, JRubyParser or ruby_parser, and is
vastly more convenient to use.

You can also use unparser to produce equivalent source code from Parser's ASTs.


%package       -n ruby-parse
Version:       3.1.3.0
Release:       alt1
Summary:       A Ruby parser executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета parser
Group:         Other
BuildArch:     noarch

Requires:      gem(parser) = 3.1.3.0

%description   -n ruby-parse
A Ruby parser executable(s).

Parser is a production-ready Ruby parser written in pure Ruby. It recognizes as
much or more code than Ripper, Melbourne, JRubyParser or ruby_parser, and is
vastly more convenient to use.

You can also use unparser to produce equivalent source code from Parser's ASTs.

%description   -n ruby-parse -l ru_RU.UTF-8
Исполнямка для самоцвета parser.


%package       -n gem-parser-doc
Version:       3.1.3.0
Release:       alt1
Summary:       A Ruby parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(parser) = 3.1.3.0

%description   -n gem-parser-doc
A Ruby parser documentation files.

Parser is a production-ready Ruby parser written in pure Ruby. It recognizes as
much or more code than Ripper, Melbourne, JRubyParser or ruby_parser, and is
vastly more convenient to use.

You can also use unparser to produce equivalent source code from Parser's ASTs.

%description   -n gem-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета parser.


%package       -n gem-parser-devel
Version:       3.1.3.0
Release:       alt1
Summary:       A Ruby parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета parser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(parser) = 3.1.3.0
Requires:      gem(bundler) >= 1.15 gem(bundler) < 3
Requires:      gem(rake) >= 13.0.1 gem(rake) < 14
Requires:      gem(racc) = 1.6.0
Requires:      gem(cliver) >= 0.3.2 gem(cliver) < 0.4
Requires:      gem(yard) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(minitest) >= 5.10 gem(minitest) < 6
Requires:      gem(simplecov) >= 0.15.1 gem(simplecov) < 1
Requires:      gem(gauntlet) >= 0
Requires:      ragel6
Requires:      racc

%description   -n gem-parser-devel
A Ruby parser development package.

Parser is a production-ready Ruby parser written in pure Ruby. It recognizes as
much or more code than Ripper, Melbourne, JRubyParser or ruby_parser, and is
vastly more convenient to use.

You can also use unparser to produce equivalent source code from Parser's ASTs.

%description   -n gem-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета parser.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemlibdir/lib/parser/lexer.rb
%ruby_gemlibdir/lib/parser/ruby31.rb
%ruby_gemspec
%ruby_gemlibdir

%files         -n ruby-parse
%_bindir/ruby-parse
%_bindir/ruby-rewrite

%files         -n gem-parser-doc
%ruby_gemdocdir

%files         -n gem-parser-devel


%changelog
* Tue Dec 20 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.3.0-alt1
- ^ 3.1.2.1 -> 3.1.3.0

* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.2.1-alt1
- ^ 3.1.2.0 -> 3.1.2.1

* Fri Jul 08 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.2.0-alt1.1
- !fix dep to ragel6, racc

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.2.0-alt1
- ^ 3.0.1.1 -> 3.1.2.0

* Thu May 27 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1.1-alt1
- ^ 2.7.2.0 -> 3.0.1.1

* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.2.0-alt1
- ^ 2.7.1.4 -> 2.7.2.0

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.1.4-alt1.1
- ! building by usage of compilation with ragel

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.1.4-alt1
- ^ 2.7.0.4 -> 2.7.1.4

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.0.4-alt1
- updated (^) 2.6.4.1 -> 2.7.0.4
- changed (*) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.4.1-alt1
- updated (^) 2.6.2.0 -> 2.6.4.1

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.2.0-alt1
- updated (^) 2.6.0.0 -> 2.6.2.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0.0-alt1
- added (+) package as a gem with usage Ruby Policy 2.0
