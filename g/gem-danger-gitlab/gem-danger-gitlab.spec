%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%define        gemname danger-gitlab

Name:          gem-danger-gitlab
Version:       8.0.0
Release:       alt1
Summary:       Stop Saying 'You Forgot To...' in Code Review with GitLab
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/danger/danger
Vcs:           https://github.com/danger/danger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(danger) >= 0
BuildRequires: gem(gitlab) >= 4.2
BuildConflicts: gem(gitlab) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(danger) >= 0
Requires:      gem(gitlab) >= 4.2
Conflicts:     gem(gitlab) >= 5
Provides:      gem(danger-gitlab) = 8.0.0


%description
Stop Saying 'You Forgot To...' in Code Review with GitLab


%if_enabled    devel
%package       -n gem-danger-gitlab-devel
Version:       8.0.0
Release:       alt1
Summary:       Stop Saying 'You Forgot To...' in Code Review with GitLab development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета danger-gitlab
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(danger-gitlab) = 8.0.0

%description   -n gem-danger-gitlab-devel
Stop Saying 'You Forgot To...' in Code Review with GitLab development package.

%description   -n gem-danger-gitlab-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета danger-gitlab.
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

%if_enabled    devel
%files         -n gem-danger-gitlab-devel
%doc README.md
%endif


%changelog
* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 8.0.0-alt1
- + packaged gem with Ruby Policy 2.0
