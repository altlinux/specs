%define        pkgname parser

Name:          gem-%pkgname
Version:       2.7.2.0
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
BuildRequires: gem(bundler) >= 1.15 gem(bundler) < 3.0.0
BuildRequires: racc gem(racc) >= 1.4.15
BuildRequires: gem(cliver) >= 0.3.2
BuildRequires: gem(gauntlet)
BuildRequires: gem(kramdown)
BuildRequires: gem(minitest) >= 5.1
BuildRequires: gem(rake) >= 13.0.1
BuildRequires: gem(simplecov) >= 0.15.1
BuildRequires: gem(yard)
BuildRequires: ragel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Parser is a production-ready Ruby parser written in pure Ruby. It recognizes as
much or more code than Ripper, Melbourne, JRubyParser or ruby_parser, and is
vastly more convenient to use.

You can also use unparser to produce equivalent source code from Parser's ASTs.


%package       -n ruby-parse
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямки для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n ruby-parse
Executable file for %gemname gem.

%description   -n ruby-parse -l ru_RU.UTF-8
Исполнямки для самоцвета %gemname.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --pre=build --use=parser --alias=parse

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n ruby-parse
%_bindir/ruby-parse
%_bindir/ruby-rewrite


%changelog
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
