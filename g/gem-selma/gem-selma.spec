%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname selma

Name:          gem-selma
Version:       0.5.3
Release:       alt1
Summary:       Selma selects and matches HTML nodes using CSS rules. Backed by Rust's lol_html parser
License:       MIT
Group:         Development/Ruby
Vcs:           https://github.com/gjtorikian/selma.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
%if_enabled check
BuildRequires: gem(amazing_print) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(gemojione) >= 4.3
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(minitest-focus) >= 1.2
BuildRequires: gem(minitest-spec-context) >= 0.0.4
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rb_sys) >= 0.9
BuildRequires: gem(ruby-lsp) >= 0.11
BuildRequires: gem(ruby_memcheck) >= 0
BuildConflicts: gem(gemojione) >= 5
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-spec-context) >= 0.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rb_sys) >= 1
BuildConflicts: gem(ruby-lsp) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Requires:      ruby >= 3.2
Requires:      rubygems >= 3.4
Requires:      gem(rb_sys) >= 0.9
Conflicts:     ruby >= 5
Conflicts:     gem(rb_sys) >= 1
Provides:      gem(selma) = 0.5.3

%description
Selma selects and matches HTML nodes using CSS rules. Backed by Rust's lol_html
parser.


%if_enabled    doc
%package       -n gem-selma-doc
Version:       0.5.3
Release:       alt1
Summary:       Selma selects and matches HTML nodes using CSS rules. Backed by Rust's lol_html parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета selma
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(selma) = 0.5.3

%description   -n gem-selma-doc
Selma selects and matches HTML nodes using CSS rules. Backed by Rust's lol_html
parser documentation files.

%description   -n gem-selma-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета selma.
%endif


%if_enabled    devel
%package       -n gem-selma-devel
Version:       0.5.3
Release:       alt1
Summary:       Selma selects and matches HTML nodes using CSS rules. Backed by Rust's lol_html parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета selma
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(selma) = 0.5.3
Requires:      gem(amazing_print) >= 0
Requires:      gem(debug) >= 0
Requires:      gem(gemojione) >= 4.3
Requires:      gem(minitest) >= 6.0
Requires:      gem(minitest-focus) >= 1.2
Requires:      gem(minitest-spec-context) >= 0.0.4
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(ruby-lsp) >= 0.11
Requires:      gem(ruby_memcheck) >= 0
Conflicts:     gem(gemojione) >= 5
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-spec-context) >= 0.1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(ruby-lsp) >= 1

%description   -n gem-selma-devel
Selma selects and matches HTML nodes using CSS rules. Backed by Rust's lol_html
parser development package.

%description   -n gem-selma-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета selma.
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
%doc LICENSE.txt README.md CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-selma-doc
%doc LICENSE.txt README.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-selma-devel
%doc LICENSE.txt README.md CHANGELOG.md
%endif


%changelog
* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.5.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
