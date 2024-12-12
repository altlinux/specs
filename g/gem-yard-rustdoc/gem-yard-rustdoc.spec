%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname yard-rustdoc

Name:          gem-yard-rustdoc
Version:       0.4.0
Release:       alt1
Summary:       Generate YARD documentation for Magnus-based Rust gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/oxidize-rb/yard-rustdoc
Vcs:           https://github.com/oxidize-rb/yard-rustdoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rb_sys) >= 0.9.18
BuildRequires: gem(standard) >= 1.9
BuildRequires: gem(syntax_tree) >= 5.0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rb_sys) >= 0.10
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(syntax_tree) >= 7
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency syntax_tree >= 6.0.0,syntax_tree < 7
Requires:      ruby >= 2.7.0
Requires:      gem(syntax_tree) >= 5.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(syntax_tree) >= 7
Conflicts:     gem(yard) >= 1
Provides:      gem(yard-rustdoc) = 0.4.0

%description
Generate YARD documentation for Magnus-based Rust gems.


%if_enabled    doc
%package       -n gem-yard-rustdoc-doc
Version:       0.4.0
Release:       alt1
Summary:       Generate YARD documentation for Magnus-based Rust gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard-rustdoc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard-rustdoc) = 0.4.0

%description   -n gem-yard-rustdoc-doc
Generate YARD documentation for Magnus-based Rust gems documentation files.

%description   -n gem-yard-rustdoc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard-rustdoc.
%endif


%if_enabled    devel
%package       -n gem-yard-rustdoc-devel
Version:       0.4.0
Release:       alt1
Summary:       Generate YARD documentation for Magnus-based Rust gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yard-rustdoc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yard-rustdoc) = 0.4.0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 13.0
Requires:      gem(standard) >= 1.9
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(standard) >= 2

%description   -n gem-yard-rustdoc-devel
Generate YARD documentation for Magnus-based Rust gems development package.

%description   -n gem-yard-rustdoc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yard-rustdoc.
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
%doc README.md CHANGELOG.md LICENSE.txt
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-yard-rustdoc-doc
%doc README.md CHANGELOG.md LICENSE.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-yard-rustdoc-devel
%doc README.md CHANGELOG.md LICENSE.txt
%endif


%changelog
* Thu Dec 12 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
