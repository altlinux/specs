# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname regexp_parser

Name:          gem-regexp-parser
Version:       2.12.0
Release:       alt1
Summary:       A regular expression parser library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ammar/regexp_parser
Vcs:           https://github.com/ammar/regexp_parser.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires: ragel6 >= 6.0
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 2.1
BuildRequires: gem(gouteur) >= 1.2
BuildRequires: gem(leto) >= 2.1
BuildRequires: gem(rake) >= 13.1
BuildRequires: gem(regexp_property_values) >= 1.5
BuildRequires: gem(rspec) >= 3.10
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(gouteur) >= 2
BuildConflicts: gem(leto) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(regexp_property_values) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names regexp_parser,regexp-parser
Requires:      ruby >= 2.0.0
Obsoletes:     ruby-regexp_parser < %EVR
Provides:      ruby-regexp_parser = %EVR
Provides:      gem(regexp_parser) = 2.12.0

%ruby_on_build_rake_tasks build

%description
A Ruby gem for tokenizing, parsing, and transforming regular expressions.

* Multilayered * A scanner/tokenizer based on Ragel * A lexer that produces a
"stream" of Token objects * A parser that produces a "tree" of Expression
objects (OO API)
* Runs on Ruby 2.x, 3.x and JRuby runtimes
* Recognizes Ruby 1.8, 1.9, 2.x and 3.x regular expressions See Supported Syntax


%if_enabled    doc
%package       -n gem-regexp-parser-doc
Version:       2.12.0
Release:       alt1
Summary:       A regular expression parser library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета regexp_parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(regexp_parser) = 2.12.0

%description   -n gem-regexp-parser-doc
A regular expression parser library for Ruby documentation files.

A Ruby gem for tokenizing, parsing, and transforming regular expressions.

* Multilayered * A scanner/tokenizer based on Ragel * A lexer that produces a
"stream" of Token objects * A parser that produces a "tree" of Expression
objects (OO API)
* Runs on Ruby 2.x, 3.x and JRuby runtimes
* Recognizes Ruby 1.8, 1.9, 2.x and 3.x regular expressions See Supported Syntax

%description   -n gem-regexp-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета regexp_parser.
%endif


%if_enabled    devel
%package       -n gem-regexp-parser-devel
Version:       2.12.0
Release:       alt1
Summary:       A regular expression parser library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета regexp_parser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(regexp_parser) = 2.12.0
Requires:      gem(gouteur) >= 1.2
Conflicts:     gem(gouteur) >= 2

%description   -n gem-regexp-parser-devel
A regular expression parser library for Ruby development package.

A Ruby gem for tokenizing, parsing, and transforming regular expressions.

* Multilayered * A scanner/tokenizer based on Ragel * A lexer that produces a
"stream" of Token objects * A parser that produces a "tree" of Expression
objects (OO API)
* Runs on Ruby 2.x, 3.x and JRuby runtimes
* Recognizes Ruby 1.8, 1.9, 2.x and 3.x regular expressions See Supported Syntax

%description   -n gem-regexp-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета regexp_parser.
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
%doc LICENSE CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-regexp-parser-doc
%doc LICENSE CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-regexp-parser-devel
%doc LICENSE CHANGELOG.md README.md
%endif


%changelog
* Fri Sep 04 2026 Pavel Skrylev <majioa@altlinux.org> 2.12.0-alt1
- ^ 2.11.3 -> 2.12.0
- ! gixed spec to build required task (close ALT #60269)

* Thu Oct 23 2025 Pavel Skrylev <majioa@altlinux.org> 2.11.3-alt1
- ^ 2.6.1 -> 2.11.3

* Tue Dec 20 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.1-alt1
- ^ 2.6.0 -> 2.6.1

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
