%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%define        gemname danger-gitlab

Name:          gem-danger-gitlab
Version:       10.0.0
Release:       alt1
Summary:       Stop Saying 'You Forgot To...' in Code Review with GitLab
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/danger/danger
Vcs:           https://github.com/danger/danger.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(danger) >= 0
BuildRequires: gem(gitlab) >= 6.0
BuildConflicts: gem(gitlab) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1.0
Requires:      gem(danger) >= 0
Requires:      gem(gitlab) >= 6.0
Conflicts:     gem(gitlab) >= 7
Provides:      gem(danger-gitlab) = 10.0.0

%description
Stop Saying 'You Forgot To...' in Code Review with GitLab


%if_enabled    devel
%package       -n gem-danger-gitlab-devel
Version:       10.0.0
Release:       alt1
Summary:       Stop Saying 'You Forgot To...' in Code Review with GitLab development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета danger-gitlab
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(danger-gitlab) = 10.0.0

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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    devel
%files         -n gem-danger-gitlab-devel
%doc LICENSE README.md
%endif


%changelog
* Wed Nov 26 2025 Pavel Skrylev <majioa@altlinux.org> 10.0.0-alt1
- ^ 8.0.0 -> 10.0.0

* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 8.0.0-alt1
- + packaged gem with Ruby Policy 2.0
