%define        gemname syntax_tree

Name:          gem-syntax-tree
Version:       4.3.0
Release:       alt1
Summary:       A parser based on ripper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kddnewton/syntax_tree
Vcs:           https://github.com/kddnewton/syntax_tree.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(prettier_print) >= 1.0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(prettier_print) >= 1.0.2
Provides:      gem(syntax_tree) = 4.3.0


%description
A parser based on ripper


%package       -n stree
Version:       4.3.0
Release:       alt1
Summary:       A parser based on ripper executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета syntax_tree
Group:         Other
BuildArch:     noarch

Requires:      gem(syntax_tree) = 4.3.0

%description   -n stree
A parser based on ripper executable(s).

%description   -n stree -l ru_RU.UTF-8
Исполнямка для самоцвета syntax_tree.


%package       -n gem-syntax-tree-doc
Version:       4.3.0
Release:       alt1
Summary:       A parser based on ripper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета syntax_tree
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(syntax_tree) = 4.3.0

%description   -n gem-syntax-tree-doc
A parser based on ripper documentation files.

%description   -n gem-syntax-tree-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета syntax_tree.


%package       -n gem-syntax-tree-devel
Version:       4.3.0
Release:       alt1
Summary:       A parser based on ripper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета syntax_tree
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(syntax_tree) = 4.3.0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-syntax-tree-devel
A parser based on ripper development package.

%description   -n gem-syntax-tree-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета syntax_tree.


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

%files         -n stree
%doc README.md
%_bindir/stree

%files         -n gem-syntax-tree-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-syntax-tree-devel
%doc README.md


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt1
- + packaged gem with Ruby Policy 2.0
