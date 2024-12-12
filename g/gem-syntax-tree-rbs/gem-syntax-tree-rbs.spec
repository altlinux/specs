%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname syntax_tree-rbs

Name:          gem-syntax-tree-rbs
Version:       1.0.0
Release:       alt1
Summary:       Syntax Tree support for RBS
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-syntax-tree/syntax_tree-rbs
Vcs:           https://github.com/ruby-syntax-tree/syntax_tree-rbs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(prettier_print) >= 0
BuildRequires: gem(rbs) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(syntax_tree) >= 2.0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names syntax_tree-rbs,syntax-tree-rbs
Requires:      gem(prettier_print) >= 0
Requires:      gem(rbs) >= 0
Requires:      gem(syntax_tree) >= 2.0.1
Provides:      gem(syntax_tree-rbs) = 1.0.0

%description
Syntax Tree support for RBS


%if_enabled    doc
%package       -n gem-syntax-tree-rbs-doc
Version:       1.0.0
Release:       alt1
Summary:       Syntax Tree support for RBS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета syntax_tree-rbs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(syntax_tree-rbs) = 1.0.0

%description   -n gem-syntax-tree-rbs-doc
Syntax Tree support for RBS documentation files.

%description   -n gem-syntax-tree-rbs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета syntax_tree-rbs.
%endif


%if_enabled    devel
%package       -n gem-syntax-tree-rbs-devel
Version:       1.0.0
Release:       alt1
Summary:       Syntax Tree support for RBS development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета syntax_tree-rbs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(syntax_tree-rbs) = 1.0.0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-syntax-tree-rbs-devel
Syntax Tree support for RBS development package.

%description   -n gem-syntax-tree-rbs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета syntax_tree-rbs.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-syntax-tree-rbs-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-syntax-tree-rbs-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
