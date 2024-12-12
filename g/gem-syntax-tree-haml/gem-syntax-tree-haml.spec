%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname syntax_tree-haml

Name:          gem-syntax-tree-haml
Version:       4.0.3
Release:       alt1
Summary:       Syntax Tree support for Haml
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-syntax-tree/syntax_tree-haml
Vcs:           https://github.com/ruby-syntax-tree/syntax_tree-haml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(haml) >= 5.2
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(prettier_print) >= 1.2.1
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(syntax_tree) >= 6.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names syntax_tree-haml,syntax-tree-haml
Requires:      gem(haml) >= 5.2
Requires:      gem(prettier_print) >= 1.2.1
Requires:      gem(syntax_tree) >= 6.0.0
Provides:      gem(syntax_tree-haml) = 4.0.3

%description
Syntax Tree support for Haml


%if_enabled    doc
%package       -n gem-syntax-tree-haml-doc
Version:       4.0.3
Release:       alt1
Summary:       Syntax Tree support for Haml documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета syntax_tree-haml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(syntax_tree-haml) = 4.0.3

%description   -n gem-syntax-tree-haml-doc
Syntax Tree support for Haml documentation files.

%description   -n gem-syntax-tree-haml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета syntax_tree-haml.
%endif


%if_enabled    devel
%package       -n gem-syntax-tree-haml-devel
Version:       4.0.3
Release:       alt1
Summary:       Syntax Tree support for Haml development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета syntax_tree-haml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(syntax_tree-haml) = 4.0.3
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-syntax-tree-haml-devel
Syntax Tree support for Haml development package.

%description   -n gem-syntax-tree-haml-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета syntax_tree-haml.
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

%if_enabled    doc
%files         -n gem-syntax-tree-haml-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-syntax-tree-haml-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
