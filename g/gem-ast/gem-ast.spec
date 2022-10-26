%define        gemname ast

Name:          gem-ast
Version:       2.4.2
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees
License:       MIT
Group:         Development/Ruby
Url:           https://whitequark.github.io/ast/
Vcs:           https://github.com/whitequark/ast.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 12.3 gem(rake) < 14
BuildRequires: gem(bacon) >= 1.2 gem(bacon) < 2
BuildRequires: gem(bacon-colored_output) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0.8.23 gem(coveralls) < 0.9
BuildRequires: gem(yard) >= 0
BuildRequires: gem(kramdown) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(ast) = 2.4.2


%description
AST is a small library for working with immutable abstract syntax trees.


%package       -n gem-ast-doc
Version:       2.4.2
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ast
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ast) = 2.4.2

%description   -n gem-ast-doc
A library for working with Abstract Syntax Trees documentation files.

AST is a small library for working with immutable abstract syntax trees.

%description   -n gem-ast-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ast.


%package       -n gem-ast-devel
Version:       2.4.2
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ast
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ast) = 2.4.2
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(bacon) >= 1.2 gem(bacon) < 2
Requires:      gem(bacon-colored_output) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0.8.23 gem(coveralls) < 0.9
Requires:      gem(yard) >= 0
Requires:      gem(kramdown) >= 0

%description   -n gem-ast-devel
A library for working with Abstract Syntax Trees development package.

AST is a small library for working with immutable abstract syntax trees.

%description   -n gem-ast-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ast.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.YARD.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ast-doc
%doc README.YARD.md
%ruby_gemdocdir

%files         -n gem-ast-devel
%doc README.YARD.md


%changelog
* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt1
- ^ 2.4.1 -> 2.4.2

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt1
- ^ 2.4.0 -> 2.4.1
- ! spec syntax

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
