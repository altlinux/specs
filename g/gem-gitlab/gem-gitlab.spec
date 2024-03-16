%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gitlab

Name:          gem-gitlab
Version:       4.19.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/NARKOZ/gitlab
Vcs:           https://github.com/narkoz/gitlab.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(httparty) >= 0.20
BuildRequires: gem(terminal-table) >= 1.5.1
BuildConflicts: gem(httparty) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(httparty) >= 0.20
Requires:      gem(terminal-table) >= 1.5.1
Conflicts:     gem(httparty) >= 1
Provides:      gem(gitlab) = 4.19.0


%description
Ruby client and CLI for GitLab API


%package       -n gitlab
Version:       4.19.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gitlab
Group:         Other
BuildArch:     noarch

Requires:      gem(gitlab) = 4.19.0

%description   -n gitlab
A Ruby wrapper and CLI for the GitLab API executable(s).

Ruby client and CLI for GitLab API
%description   -n gitlab -l ru_RU.UTF-8
Исполнямка для самоцвета gitlab.


%if_enabled    doc
%package       -n gem-gitlab-doc
Version:       4.19.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gitlab
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gitlab) = 4.19.0

%description   -n gem-gitlab-doc
A Ruby wrapper and CLI for the GitLab API documentation files.

Ruby client and CLI for GitLab API
%description   -n gem-gitlab-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gitlab.
%endif


%if_enabled    devel
%package       -n gem-gitlab-devel
Version:       4.19.0
Release:       alt1
Summary:       A Ruby wrapper and CLI for the GitLab API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gitlab
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gitlab) = 4.19.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 0

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gitlab
%doc README.md
%_bindir/gitlab

%if_enabled    doc
%files         -n gem-gitlab-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gitlab-devel
%doc README.md
%endif


%changelog
* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 4.19.0-alt1
- + packaged gem with Ruby Policy 2.0
