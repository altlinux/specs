%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ast

Name:          gem-ast
Version:       2.4.3
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees
License:       MIT
Group:         Development/Ruby
Url:           https://whitequark.github.io/ast/
Vcs:           https://github.com/whitequark/ast.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(coveralls) >= 0.8.23
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(ast) = 2.4.3

%description
AST is a small library for working with immutable abstract syntax trees.


%if_enabled    doc
%package       -n gem-ast-doc
Version:       2.4.3
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ast
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ast) = 2.4.3

%description   -n gem-ast-doc
A library for working with Abstract Syntax Trees documentation files.

AST is a small library for working with immutable abstract syntax trees.

%description   -n gem-ast-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ast.
%endif


%if_enabled    devel
%package       -n gem-ast-devel
Version:       2.4.3
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ast
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ast) = 2.4.3
Requires:      gem(coveralls) >= 0.8.23
Requires:      gem(kramdown) >= 0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(simplecov) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-ast-devel
A library for working with Abstract Syntax Trees development package.

AST is a small library for working with immutable abstract syntax trees.

%description   -n gem-ast-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ast.
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
%doc LICENSE.MIT README.YARD.md CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-ast-doc
%doc LICENSE.MIT README.YARD.md CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ast-devel
%doc LICENSE.MIT README.YARD.md CHANGELOG.md README.md
%endif


%changelog
* Mon Jun 22 2026 Pavel Skrylev <majioa@altlinux.org> 2.4.3-alt1
- ^ 2.4.2p7 -> 2.4.3

* Mon Mar 03 2025 Pavel Skrylev <majioa@altlinux.org> 2.4.2.7-alt0.1
- ^ 2.4.2 -> 2.4.2p7
- * define explicit dependencies

* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt1
- ^ 2.4.1 -> 2.4.2

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt1
- ^ 2.4.0 -> 2.4.1
- ! spec syntax

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
