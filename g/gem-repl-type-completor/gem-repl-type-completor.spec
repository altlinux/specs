%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname repl_type_completor

Name:          gem-repl-type-completor
Version:       0.1.11
Release:       alt1
Summary:       Type based completion for REPL
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/repl_type_completor
Vcs:           https://github.com/ruby/repl_type_completor.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(irb) >= 1.10.0
BuildRequires: gem(prism) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rbs) >= 2.7.0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildConflicts: gem(prism) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rbs) >= 4.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names repl_type_completor,repl-type-completor
Requires:      ruby >= 3.0.0
Requires:      gem(prism) >= 1.0
Requires:      gem(rbs) >= 2.7.0
Conflicts:     gem(prism) >= 2
Conflicts:     gem(rbs) >= 4.0.0
Provides:      gem(repl_type_completor) = 0.1.11

%description
Type based completion for REPL.


%if_enabled    doc
%package       -n gem-repl-type-completor-doc
Version:       0.1.11
Release:       alt1
Summary:       Type based completion for REPL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета repl_type_completor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(repl_type_completor) = 0.1.11

%description   -n gem-repl-type-completor-doc
Type based completion for REPL documentation files.

%description   -n gem-repl-type-completor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета repl_type_completor.
%endif


%if_enabled    devel
%package       -n gem-repl-type-completor-devel
Version:       0.1.11
Release:       alt1
Summary:       Type based completion for REPL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета repl_type_completor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(repl_type_completor) = 0.1.11
Requires:      gem(irb) >= 1.10.0
Requires:      gem(rake) >= 13.0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-repl-type-completor-devel
Type based completion for REPL development package.

%description   -n gem-repl-type-completor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета repl_type_completor.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-repl-type-completor-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-repl-type-completor-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Thu Aug 14 2025 Pavel Skrylev <majioa@altlinux.org> 0.1.11-alt1
- ^ 0.1.4 -> 0.1.11

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
- + packaged gem with Ruby Policy 2.0
