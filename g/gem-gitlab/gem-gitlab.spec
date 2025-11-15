%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gitlab

Name:          gem-gitlab
Version:       6.0.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/NARKOZ/gitlab
Vcs:           https://github.com/narkoz/gitlab.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(httparty) >= 0.20
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(terminal-table) >= 1.5.1
BuildRequires: gem(webmock) >= 0
BuildConflicts: gem(httparty) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      gem(base64) >= 0
Requires:      gem(httparty) >= 0.20
Requires:      gem(terminal-table) >= 1.5.1
Conflicts:     gem(httparty) >= 1
Provides:      gem(gitlab) = 6.0.0

%description
Ruby client and CLI for GitLab API


%package       -n gitlab-cli
Version:       6.0.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gitlab
Group:         Other
BuildArch:     noarch

Requires:      gem(gitlab) = 6.0.0

%description   -n gitlab-cli
A Ruby wrapper and CLI for the GitLab API executable(s).

Ruby client and CLI for GitLab API

%description   -n gitlab-cli -l ru_RU.UTF-8
Исполнямка для самоцвета gitlab.


%if_enabled    doc
%package       -n gem-gitlab-doc
Version:       6.0.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gitlab
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gitlab) = 6.0.0

%description   -n gem-gitlab-doc
A Ruby wrapper and CLI for the GitLab API documentation files.

Ruby client and CLI for GitLab API

%description   -n gem-gitlab-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gitlab.
%endif


%if_enabled    devel
%package       -n gem-gitlab-devel
Version:       6.0.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gitlab
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gitlab) = 6.0.0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(webmock) >= 0

%description   -n gem-gitlab-devel
A Ruby wrapper and CLI for the GitLab API development package.

Ruby client and CLI for GitLab API

%description   -n gem-gitlab-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gitlab.
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
%doc CHANGELOG.md LICENSE.txt README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gitlab-cli
%doc CHANGELOG.md LICENSE.txt README.md CONTRIBUTING.md
%_bindir/gitlab

%if_enabled    doc
%files         -n gem-gitlab-doc
%doc CHANGELOG.md LICENSE.txt README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gitlab-devel
%doc CHANGELOG.md LICENSE.txt README.md CONTRIBUTING.md
%endif


%changelog
* Thu Oct 16 2025 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 4.19.0 -> 6.0.0 (closes ALT#52419)

* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 4.19.0-alt1
- + packaged gem with Ruby Policy 2.0
