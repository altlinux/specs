%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mdl

Name:          gem-mdl
Version:       0.18.1
Release:       alt1
Summary:       Markdown lint tool
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/markdownlint/markdownlint
Vcs:           https://github.com/markdownlint/markdownlint.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bundler) >= 1.12
BuildRequires: gem(kramdown) >= 2.5
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(mixlib-cli) >= 0
BuildRequires: gem(mixlib-config) >= 0
BuildRequires: gem(mixlib-shellout) >= 0
BuildRequires: gem(pry) >= 0.16.0
BuildRequires: gem(rake) >= 13.3.1
BuildRequires: gem(rubocop) >= 1.90
BuildRequires: gem(uri) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 1.12
%ruby_use_gem_dependency kramdown >= 2.3.1
%ruby_use_gem_dependency kramdown-parser-gfm >= 1.1
%ruby_use_gem_dependency minitest >= 5.17.0
%ruby_use_gem_dependency pry >= 0.13.1
%ruby_use_gem_dependency rake >= 13.1.0
%ruby_use_gem_dependency rubocop >= 1.90
Requires:      ruby >= 3.2
Requires:      gem(kramdown) >= 2.5
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(mixlib-cli) >= 0
Requires:      gem(mixlib-config) >= 0
Requires:      gem(mixlib-shellout) >= 0
Requires:      gem(uri) >= 0
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(kramdown-parser-gfm) >= 2
Provides:      gem(mdl) = 0.18.1

%description
Style checker/lint tool for markdown files


%package       -n mdl
Version:       0.18.1
Release:       alt1
Summary:       Markdown lint tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mdl
Group:         Other
BuildArch:     noarch

Requires:      gem(mdl) = 0.18.1

%description   -n mdl
Markdown lint tool executable(s).

Style checker/lint tool for markdown files

%description   -n mdl -l ru_RU.UTF-8
Исполнямка для самоцвета mdl.


%if_enabled    doc
%package       -n gem-mdl-doc
Version:       0.18.1
Release:       alt1
Summary:       Markdown lint tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mdl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mdl) = 0.18.1

%description   -n gem-mdl-doc
Markdown lint tool documentation files.

Style checker/lint tool for markdown files

%description   -n gem-mdl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mdl.
%endif


%if_enabled    devel
%package       -n gem-mdl-devel
Version:       0.18.1
Release:       alt1
Summary:       Markdown lint tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mdl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mdl) = 0.18.1
Requires:      gem(base64) >= 0
Requires:      gem(bundler) >= 1.12
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(mixlib-cli) >= 0
Requires:      gem(mixlib-config) >= 0
Requires:      gem(mixlib-shellout) >= 0
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rubocop) >= 1.15.0

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
* Mon Sep 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.18.1-alt1
- ^ 0.17.0 -> 0.18.1

* Mon Jun 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt1
- ^ 0.13.0 -> 0.17.0

* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- ^ 0.11.0 -> 0.13.0

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- + packaged gem with Ruby Policy 2.0
