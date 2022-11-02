# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname regexp_parser

Name:          gem-regexp-parser
Version:       2.6.0
Release:       alt1
Summary:       A regular expression parser library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ammar/regexp_parser
Vcs:           https://github.com/ammar/regexp_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel >= 6.0
%if_with check
BuildRequires: gem(ice_nine) >= 0.11.2 gem(ice_nine) < 0.12
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(regexp_property_values) >= 1.3 gem(regexp_property_values) < 2
BuildRequires: gem(rspec) >= 3.10 gem(rspec) < 4
BuildRequires: gem(benchmark-ips) >= 2.1 gem(benchmark-ips) < 3
BuildRequires: gem(gouteur) >= 0
BuildRequires: gem(rubocop) >= 1.7 gem(rubocop) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names regexp_parser,regexp-parser
Obsoletes:     ruby-regexp_parser < %EVR
Provides:      ruby-regexp_parser = %EVR
Provides:      gem(regexp_parser) = 2.6.0

%ruby_on_build_rake_tasks build

%description
A Ruby gem for tokenizing, parsing, and transforming regular expressions.

* Multilayered
 * A scanner/tokenizer based on Ragel
 * A lexer that produces a "stream" of Token objects
 * A parser that produces a "tree" of Expression objects (OO API)
* Runs on Ruby 2.x, 3.x and JRuby runtimes
* Recognizes Ruby 1.8, 1.9, 2.x and 3.x regular expressions See Supported Syntax


%package       -n gem-regexp-parser-doc
Version:       2.6.0
Release:       alt1
Summary:       A regular expression parser library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета regexp_parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(regexp_parser) = 2.6.0

%description   -n gem-regexp-parser-doc
A regular expression parser library for Ruby documentation files.

A Ruby gem for tokenizing, parsing, and transforming regular expressions.

* Multilayered
 * A scanner/tokenizer based on Ragel
 * A lexer that produces a "stream" of Token objects
 * A parser that produces a "tree" of Expression objects (OO API)
* Runs on Ruby 2.x, 3.x and JRuby runtimes
* Recognizes Ruby 1.8, 1.9, 2.x and 3.x regular expressions See Supported Syntax


%description   -n gem-regexp-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета regexp_parser.


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

%files         -n gem-regexp-parser-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- ^ 1.8.2 -> 2.6.0

* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt1
- ^ 1.7.1 -> 1.8.2

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1.1
- ! building by usage of compilation with ragel

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.6.0 -> 1.7.1
- ! spec tags

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- updated to (^) v1.6.0
- fix (!) spec

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- updated to (^) Ruby Policy 2.0
- updated to (^) v1.5.1

* Tue Oct 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- added (+) initial build for Sisyphus
