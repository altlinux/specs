%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-gradual

Name:          gem-rubocop-gradual
Version:       0.3.4
Release:       alt1
Summary:       Gradual RuboCop plugin
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/skryukov/rubocop-gradual
Vcs:           https://github.com/skryukov/rubocop-gradual.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(diff-lcs) >= 1.2.0
BuildRequires: gem(diffy) >= 3.0
BuildRequires: gem(parallel) >= 1.10
BuildRequires: gem(rainbow) >= 2.2.2
BuildRequires: gem(rubocop) >= 1.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(diff-lcs) >= 2.0
BuildConflicts: gem(diffy) >= 4
BuildConflicts: gem(parallel) >= 2
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(diff-lcs) >= 1.2.0
Requires:      gem(diffy) >= 3.0
Requires:      gem(parallel) >= 1.10
Requires:      gem(rainbow) >= 2.2.2
Requires:      gem(rubocop) >= 1.0
Conflicts:     gem(diff-lcs) >= 2.0
Conflicts:     gem(diffy) >= 4
Conflicts:     gem(parallel) >= 2
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(rubocop) >= 2
Provides:      gem(rubocop-gradual) = 0.3.4


%description
Gradually improve your code with RuboCop.


%package       -n rubocop-gradual
Version:       0.3.4
Release:       alt1
Summary:       Gradual RuboCop plugin executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubocop-gradual
Group:         Other
BuildArch:     noarch

Requires:      gem(rubocop-gradual) = 0.3.4

%description   -n rubocop-gradual
Gradual RuboCop plugin executable(s).

Gradually improve your code with RuboCop.

%description   -n rubocop-gradual -l ru_RU.UTF-8
Исполнямка для самоцвета rubocop-gradual.


%if_enabled    doc
%package       -n gem-rubocop-gradual-doc
Version:       0.3.4
Release:       alt1
Summary:       Gradual RuboCop plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-gradual
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-gradual) = 0.3.4

%description   -n gem-rubocop-gradual-doc
Gradual RuboCop plugin documentation files.

Gradually improve your code with RuboCop.

%description   -n gem-rubocop-gradual-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-gradual.
%endif


%if_enabled    devel
%package       -n gem-rubocop-gradual-devel
Version:       0.3.4
Release:       alt1
Summary:       Gradual RuboCop plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-gradual
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-gradual) = 0.3.4
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-rspec) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-rubocop-gradual-devel
Gradual RuboCop plugin development package.

Gradually improve your code with RuboCop.
%description   -n gem-rubocop-gradual-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-gradual.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rubocop-gradual
%doc README.md
%_bindir/rubocop-gradual

%if_enabled    doc
%files         -n gem-rubocop-gradual-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-gradual-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.3.4-alt1
- + packaged gem with Ruby Policy 2.0
