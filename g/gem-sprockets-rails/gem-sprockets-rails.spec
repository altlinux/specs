%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sprockets-rails

Name:          gem-sprockets-rails
Version:       3.5.2.4
Release:       alt1
Summary:       Sprockets Rails integration
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/sprockets-rails
Vcs:           https://github.com/rails/sprockets-rails.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb
%if_enabled check
BuildRequires: gem(actionpack) >= 6.1
BuildRequires: gem(activesupport) >= 6.1
BuildRequires: gem(rack) >= 2.2
BuildRequires: gem(railties) >= 6.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sass) >= 0
BuildRequires: gem(sprockets) >= 3.0.0
BuildRequires: gem(uglifier) >= 0
BuildConflicts: gem(rack) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.1.7,rack < 4
Requires:      ruby >= 2.5
Requires:      gem(actionpack) >= 6.1
Requires:      gem(activesupport) >= 6.1
Requires:      gem(rack) >= 2.2
Requires:      gem(railties) >= 6.1
Requires:      gem(sprockets) >= 3.0.0
Conflicts:     gem(rack) >= 4
Provides:      gem(sprockets-rails) = 3.5.2.4

%ruby_use_gem_version sprockets-rails:3.5.2.4

%description
Sprockets Rails integration


%if_enabled    doc
%package       -n gem-sprockets-rails-doc
Version:       3.5.2.4
Release:       alt1
Summary:       Sprockets Rails integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sprockets-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sprockets-rails) = 3.5.2.4

%description   -n gem-sprockets-rails-doc
Sprockets Rails integration documentation files.

%description   -n gem-sprockets-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sprockets-rails.
%endif


%if_enabled    devel
%package       -n gem-sprockets-rails-devel
Version:       3.5.2.4
Release:       alt1
Summary:       Sprockets Rails integration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sprockets-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sprockets-rails) = 3.5.2.4
Requires:      gem(rake) >= 0
Requires:      gem(sass) >= 0
Requires:      gem(uglifier) >= 0

%description   -n gem-sprockets-rails-devel
Sprockets Rails integration development package.

%description   -n gem-sprockets-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sprockets-rails.
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
%doc MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-sprockets-rails-doc
%doc MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sprockets-rails-devel
%doc MIT-LICENSE README.md CONTRIBUTING.md
%endif


%changelog
* Sun Mar 29 2026 Pavel Skrylev <majioa@altlinux.org> 3.5.2.4-alt1
- ^ 3.5.2 -> 3.5.2p4
- * define explicit dependencies

* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 3.5.2-alt1
- ^ 3.4.2.25 -> 3.5.2

* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 3.4.2.25-alt0.1
- ^ 3.4.2 -> 3.4.2p25

* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 3.4.2-alt1
- + packaged gem with Ruby Policy 2.0
