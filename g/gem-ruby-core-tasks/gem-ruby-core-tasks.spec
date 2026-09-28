%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-core-tasks

Name:          gem-ruby-core-tasks
Version:       0.0.0.7
Release:       alt0.1
Summary:       Rake extension to build extension libraries
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/nobu/ruby-core-tasks
Vcs:           https://github.com/nobu/ruby-core-tasks.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires: fakegit
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3
Requires:      gem(rake) >= 13.0
Conflicts:     gem(rake) >= 14
Provides:      gem(ruby-core-tasks) = 0.0.0.7

%ruby_use_gem_version ruby-core-tasks:0.0.0.7

%description
Provides Rake extension to build extension libraries.


%if_enabled    doc
%package       -n gem-ruby-core-tasks-doc
Version:       0.0.0.7
Release:       alt0.1
Summary:       Rake extension to build extension libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-core-tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-core-tasks) = 0.0.0.7

%description   -n gem-ruby-core-tasks-doc
Rake extension to build extension libraries documentation files.

Provides Rake extension to build extension libraries.

%description   -n gem-ruby-core-tasks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-core-tasks.
%endif


%if_enabled    devel
%package       -n gem-ruby-core-tasks-devel
Version:       0.0.0.7
Release:       alt0.1
Summary:       Rake extension to build extension libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-core-tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-core-tasks) = 0.0.0.7

%description   -n gem-ruby-core-tasks-devel
Rake extension to build extension libraries development package.

Provides Rake extension to build extension libraries.

%description   -n gem-ruby-core-tasks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-core-tasks.
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

%if_enabled    doc
%files         -n gem-ruby-core-tasks-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-core-tasks-devel
%doc README.md
%endif


%changelog
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.0.0.7-alt0.1
- + packaged gem versioned as 0.0.0p7 with Ruby Policy 2.0
- * define explicit dependencies
