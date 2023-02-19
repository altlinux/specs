# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname ruby-ll

Name:          gem-ruby-ll
Version:       2.1.2
Release:       alt1.3
Summary:       An LL(1) parser generator for Ruby
License:       MPL-2.0
Group:         Development/Ruby
Url:           https://gitlab.com/yorickpeterse/ruby-ll
Vcs:           https://gitlab.com/yorickpeterse/ruby-ll.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel6
BuildRequires: gem(rake-compiler) >= 0
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(ast) >= 0
BuildRequires: gem(ansi) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(benchmark-ips) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ast) >= 0
Requires:      gem(ansi) >= 0
Provides:      gem(ruby-ll) = 2.1.2

%ruby_on_build_rake_tasks lexer,parser

%description
ruby-ll is a high performance LL(1) table based parser generator for Ruby. The
parser driver is written in C/Java to ensure good runtime performance, the
compiler is written entirely in Ruby.

ruby-ll was written to serve as a fast and easy to use alternative to Racc for
the various parsers used in Oga. However, ruby-ll isn't limited to just Oga, you
can use it to write a parser for any language that can be represented using an
LL(1) grammar.

ruby-ll is self-hosting, this allows one to use ruby-ll to modify its own
parser. Self-hosting was achieved by bootstrapping the parser using a Racc
parser that outputs the same AST as the ruby-ll parser. The Racc parser remains
in the repository for historical purposes and in case it's ever needed again, it
can be found in bootstrap/parser.y.


%package       -n ruby-ll
Version:       2.1.2
Release:       alt1.3
Summary:       An LL(1) parser generator for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-ll
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-ll) = 2.1.2

%description   -n ruby-ll
An LL(1) parser generator for Ruby executable(s).

ruby-ll is a high performance LL(1) table based parser generator for Ruby. The
parser driver is written in C/Java to ensure good runtime performance, the
compiler is written entirely in Ruby.

ruby-ll was written to serve as a fast and easy to use alternative to Racc for
the various parsers used in Oga. However, ruby-ll isn't limited to just Oga, you
can use it to write a parser for any language that can be represented using an
LL(1) grammar.

ruby-ll is self-hosting, this allows one to use ruby-ll to modify its own
parser. Self-hosting was achieved by bootstrapping the parser using a Racc
parser that outputs the same AST as the ruby-ll parser. The Racc parser remains
in the repository for historical purposes and in case it's ever needed again, it
can be found in bootstrap/parser.y.

%description   -n ruby-ll -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-ll.


%package       -n gem-ruby-ll-doc
Version:       2.1.2
Release:       alt1.3
Summary:       An LL(1) parser generator for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-ll
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-ll) = 2.1.2

%description   -n gem-ruby-ll-doc
An LL(1) parser generator for Ruby documentation files.

ruby-ll is a high performance LL(1) table based parser generator for Ruby. The
parser driver is written in C/Java to ensure good runtime performance, the
compiler is written entirely in Ruby.

ruby-ll was written to serve as a fast and easy to use alternative to Racc for
the various parsers used in Oga. However, ruby-ll isn't limited to just Oga, you
can use it to write a parser for any language that can be represented using an
LL(1) grammar.

ruby-ll is self-hosting, this allows one to use ruby-ll to modify its own
parser. Self-hosting was achieved by bootstrapping the parser using a Racc
parser that outputs the same AST as the ruby-ll parser. The Racc parser remains
in the repository for historical purposes and in case it's ever needed again, it
can be found in bootstrap/parser.y.

%description   -n gem-ruby-ll-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-ll.


%package       -n gem-ruby-ll-devel
Version:       2.1.2
Release:       alt1.3
Summary:       An LL(1) parser generator for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-ll
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-ll) = 2.1.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(yard) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(benchmark-ips) >= 2.0
Requires:      gem(rake-compiler) >= 0
Requires:      ragel6
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(benchmark-ips) >= 3

%description   -n gem-ruby-ll-devel
An LL(1) parser generator for Ruby development package.

ruby-ll is a high performance LL(1) table based parser generator for Ruby. The
parser driver is written in C/Java to ensure good runtime performance, the
compiler is written entirely in Ruby.

ruby-ll was written to serve as a fast and easy to use alternative to Racc for
the various parsers used in Oga. However, ruby-ll isn't limited to just Oga, you
can use it to write a parser for any language that can be represented using an
LL(1) grammar.

ruby-ll is self-hosting, this allows one to use ruby-ll to modify its own
parser. Self-hosting was achieved by bootstrapping the parser using a Racc
parser that outputs the same AST as the ruby-ll parser. The Racc parser remains
in the repository for historical purposes and in case it's ever needed again, it
can be found in bootstrap/parser.y.

%description   -n gem-ruby-ll-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-ll.


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
%ruby_gemextdir

%files         -n ruby-ll
%doc README.md
%_bindir/ruby-ll

%files         -n gem-ruby-ll-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ruby-ll-devel
%doc README.md
%ruby_includedir/*


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1.3
- ! closes build reqs under check condition

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1.2
- ! spec tag

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1.1
- ! spec according to changelog rules

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- + packaged as a gem with usage Ruby Policy 2.0
