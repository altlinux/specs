%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname syntax_tree

Name:          gem-syntax-tree
Version:       6.2.0
Release:       alt1
Summary:       A parser based on ripper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kddnewton/syntax_tree
Vcs:           https://github.com/kddnewton/syntax_tree.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(prettier_print) >= 1.2.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(simplecov) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names syntax_tree,syntax-tree
Requires:      ruby >= 2.7.0
Requires:      gem(prettier_print) >= 1.2.0
Provides:      syntax_tree = %EVR
Provides:      gem(syntax_tree) = 6.2.0

%ruby_use_gem_version syntax_tree:6.2.0

%description
Syntax Tree is a suite of tools built on top of the internal CRuby parser. It
provides the ability to generate a syntax tree from source, as well as the tools
necessary to inspect and manipulate that syntax tree. It can be used to build
formatters, linters, language servers, and more.

It is built with only standard library dependencies. It additionally ships with
a plugin system so that you can build your own syntax trees from other languages
and incorporate these tools.


%package       -n syntax-tree
Version:       6.2.0
Release:       alt1
Summary:       A parser based on ripper executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета syntax_tree
Group:         Other
BuildArch:     noarch

Requires:      gem(syntax_tree) = 6.2.0

%description   -n syntax-tree
A parser based on ripper executable(s).

Syntax Tree is a suite of tools built on top of the internal CRuby parser. It
provides the ability to generate a syntax tree from source, as well as the tools
necessary to inspect and manipulate that syntax tree. It can be used to build
formatters, linters, language servers, and more.

It is built with only standard library dependencies. It additionally ships with
a plugin system so that you can build your own syntax trees from other languages
and incorporate these tools.

%description   -n syntax-tree -l ru_RU.UTF-8
Исполнямка для самоцвета syntax_tree.


%if_enabled    doc
%package       -n gem-syntax-tree-doc
Version:       6.2.0
Release:       alt1
Summary:       A parser based on ripper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета syntax_tree
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(syntax_tree) = 6.2.0

%description   -n gem-syntax-tree-doc
A parser based on ripper documentation files.

Syntax Tree is a suite of tools built on top of the internal CRuby parser. It
provides the ability to generate a syntax tree from source, as well as the tools
necessary to inspect and manipulate that syntax tree. It can be used to build
formatters, linters, language servers, and more.

It is built with only standard library dependencies. It additionally ships with
a plugin system so that you can build your own syntax trees from other languages
and incorporate these tools.

%description   -n gem-syntax-tree-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета syntax_tree.
%endif


%if_enabled    devel
%package       -n gem-syntax-tree-devel
Version:       6.2.0
Release:       alt1
Summary:       A parser based on ripper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета syntax_tree
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(syntax_tree) = 6.2.0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-syntax-tree-devel
A parser based on ripper development package.

Syntax Tree is a suite of tools built on top of the internal CRuby parser. It
provides the ability to generate a syntax tree from source, as well as the tools
necessary to inspect and manipulate that syntax tree. It can be used to build
formatters, linters, language servers, and more.

It is built with only standard library dependencies. It additionally ships with
a plugin system so that you can build your own syntax trees from other languages
and incorporate these tools.

%description   -n gem-syntax-tree-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета syntax_tree.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n syntax-tree
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%_bindir/stree
%_bindir/yarv

%if_enabled    doc
%files         -n gem-syntax-tree-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-syntax-tree-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 6.2.0-alt1
- ^ 4.3.0 -> 6.2.0

* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt1
- + packaged gem with Ruby Policy 2.0
