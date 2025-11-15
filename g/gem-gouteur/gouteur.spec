%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gouteur

Name:          gem-gouteur
Version:       1.1.0
Release:       alt1
Summary:       See if your lib is still digestible
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jaynetics/gouteur
Vcs:           https://github.com/jaynetics/gouteur.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(debug) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(relaxed-rubocop) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.7
BuildRequires: gem(simplecov-cobertura) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5.0
Requires:      gem(debug) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(relaxed-rubocop) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.7
Requires:      gem(simplecov-cobertura) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Provides:      gem(gouteur) = 1.1.0

%description
Run tests of dependent gems against your changes.


%package       -n gem-example-repo
Version:       0.1.0
Release:       alt1
Summary:       This is for testing; not intended for publication
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.5.0
Requires:      gem(example_repo) >= 0
Requires:      gem(gouteur) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Provides:      gem(example_repo) = 0.1.0

%description   -n gem-example-repo
Run tests of dependent gems against your changes.


%if_enabled    doc
%package       -n gem-example-repo-doc
Version:       0.1.0
Release:       alt1
Summary:       This is for testing; not intended for publication documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета example_repo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(example_repo) = 0.1.0

%description   -n gem-example-repo-doc
This is for testing; not intended for publication documentation files.

Run tests of dependent gems against your changes.

%description   -n gem-example-repo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета example_repo.
%endif


%if_enabled    devel
%package       -n gem-example-repo-devel
Version:       0.1.0
Release:       alt1
Summary:       This is for testing; not intended for publication development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета example_repo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(example_repo) = 0.1.0

%description   -n gem-example-repo-devel
This is for testing; not intended for publication development package.

Run tests of dependent gems against your changes.

%description   -n gem-example-repo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета example_repo.
%endif


%package       -n gouteur
Version:       1.1.0
Release:       alt1
Summary:       See if your lib is still digestible executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gouteur
Group:         Other
BuildArch:     noarch

Requires:      gem(gouteur) = 1.1.0
Requires:      gem(debug) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(relaxed-rubocop) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.7
Requires:      gem(simplecov-cobertura) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gouteur
See if your lib is still digestible executable(s).

Run tests of dependent gems against your changes.

%description   -n gouteur -l ru_RU.UTF-8
Исполнямка для самоцвета gouteur.


%if_enabled    doc
%package       -n gem-gouteur-doc
Version:       1.1.0
Release:       alt1
Summary:       See if your lib is still digestible documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gouteur
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gouteur) = 1.1.0

%description   -n gem-gouteur-doc
See if your lib is still digestible documentation files.

Run tests of dependent gems against your changes.

%description   -n gem-gouteur-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gouteur.
%endif


%if_enabled    devel
%package       -n gem-gouteur-devel
Version:       1.1.0
Release:       alt1
Summary:       See if your lib is still digestible development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gouteur
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gouteur) = 1.1.0

%description   -n gem-gouteur-devel
See if your lib is still digestible development package.

Run tests of dependent gems against your changes.

%description   -n gem-gouteur-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gouteur.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-example-repo
%ruby_gemspecdir/example_repo-0.1.0.gemspec
%ruby_gemslibdir/example_repo-0.1.0

%if_enabled    doc
%files         -n gem-example-repo-doc
%ruby_gemsdocdir/example_repo-0.1.0
%endif

%if_enabled    devel
%files         -n gem-example-repo-devel
%endif

%files         -n gouteur
%doc CHANGELOG.md LICENSE.txt README.md
%_bindir/gouteur

%if_enabled    doc
%files         -n gem-gouteur-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gouteur-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Thu Oct 30 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
