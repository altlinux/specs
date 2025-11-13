%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mdl

Name:          gem-mdl
Version:       0.13.0
Release:       alt1
Summary:       Markdown lint tool
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/markdownlint/markdownlint
Vcs:           https://github.com/markdownlint/markdownlint.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.12
BuildRequires: gem(kramdown) >= 2.3
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(minitest) >= 5.9
BuildRequires: gem(mixlib-cli) >= 2.1.1
BuildRequires: gem(mixlib-config) >= 2.2.1
BuildRequires: gem(mixlib-shellout) >= 0
BuildRequires: gem(pry) >= 0.10
BuildRequires: gem(rake) >= 11.2
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mixlib-cli) >= 3
BuildConflicts: gem(mixlib-config) >= 4
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.7
Requires:      gem(kramdown) >= 2.3
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(mixlib-cli) >= 2.1.1
Requires:      gem(mixlib-config) >= 2.2.1
Requires:      gem(mixlib-shellout) >= 0
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(mixlib-cli) >= 3
Conflicts:     gem(mixlib-config) >= 4
Provides:      gem(mdl) = 0.13.0

%description
Style checker/lint tool for markdown files


%package       -n mdl
Version:       0.13.0
Release:       alt1
Summary:       Markdown lint tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mdl
Group:         Other
BuildArch:     noarch

Requires:      gem(mdl) = 0.13.0

%description   -n mdl
Markdown lint tool executable(s).

Style checker/lint tool for markdown files

%description   -n mdl -l ru_RU.UTF-8
Исполнямка для самоцвета mdl.


%if_enabled    doc
%package       -n gem-mdl-doc
Version:       0.13.0
Release:       alt1
Summary:       Markdown lint tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mdl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mdl) = 0.13.0

%description   -n gem-mdl-doc
Markdown lint tool documentation files.

Style checker/lint tool for markdown files

%description   -n gem-mdl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mdl.
%endif


%if_enabled    devel
%package       -n gem-mdl-devel
Version:       0.13.0
Release:       alt1
Summary:       Markdown lint tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mdl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mdl) = 0.13.0
Requires:      gem(bundler) >= 1.12
Requires:      gem(minitest) >= 5.9
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 11.2
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2

%description   -n gem-mdl-devel
Markdown lint tool development package.

Style checker/lint tool for markdown files

%description   -n gem-mdl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mdl.
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
%doc LICENSE.txt CHANGELOG.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n mdl
%doc LICENSE.txt CHANGELOG.md CONTRIBUTING.md README.md
%_bindir/mdl

%if_enabled    doc
%files         -n gem-mdl-doc
%doc LICENSE.txt CHANGELOG.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mdl-devel
%doc LICENSE.txt CHANGELOG.md CONTRIBUTING.md README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- ^ 0.11.0 -> 0.13.0

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- + packaged gem with Ruby Policy 2.0
