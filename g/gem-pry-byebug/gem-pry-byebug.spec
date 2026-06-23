%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pry-byebug

Name:          gem-pry-byebug
Version:       3.12.0
Release:       alt1
Summary:       Fast debugging with Pry
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/deivid-rodriguez/pry-byebug
Vcs:           https://github.com/deivid-rodriguez/pry-byebug.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(byebug) >= 11.1.3
BuildRequires: gem(chandler) >= 0.9.0
BuildRequires: gem(faraday-retry) >= 0
BuildRequires: gem(mdl) >= 0.15.0
BuildRequires: gem(minitest) >= 5.14
BuildRequires: gem(minitest-bisect) >= 1.5
BuildRequires: gem(pry) >= 0.13
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop) >= 1.0
BuildConflicts: gem(byebug) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-bisect) >= 2
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency byebug >= 11.1.3,byebug < 12
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency chandler >= 0.9.0.5,chandler < 1
%ruby_use_gem_dependency mdl >= 0.17.0,mdl < 1
Requires:      ruby >= 3.2.0
Requires:      gem(byebug) >= 11.1.3
Requires:      gem(pry) >= 0.13
Conflicts:     gem(byebug) >= 14
Conflicts:     gem(pry) >= 1
Provides:      gem(pry-byebug) = 3.12.0

%description
Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish', 'continue' and
'break' commands to control execution.


%if_enabled    doc
%package       -n gem-pry-byebug-doc
Version:       3.12.0
Release:       alt1
Summary:       Fast debugging with Pry documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-byebug
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-byebug) = 3.12.0

%description   -n gem-pry-byebug-doc
Fast debugging with Pry documentation files.

Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish', 'continue' and
'break' commands to control execution.

%description   -n gem-pry-byebug-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-byebug.
%endif


%if_enabled    devel
%package       -n gem-pry-byebug-devel
Version:       3.12.0
Release:       alt1
Summary:       Fast debugging with Pry development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-byebug
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-byebug) = 3.12.0
Requires:      gem(byebug) >= 11.1.3
Requires:      gem(chandler) >= 0.9.0
Requires:      gem(faraday-retry) >= 0
Requires:      gem(mdl) >= 0.15.0
Requires:      gem(minitest) >= 5.14
Requires:      gem(minitest-bisect) >= 1.5
Requires:      gem(pry) >= 0.13
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 1.0
Conflicts:     gem(byebug) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-bisect) >= 2
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2

%description   -n gem-pry-byebug-devel
Fast debugging with Pry development package.

Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish', 'continue' and
'break' commands to control execution.

%description   -n gem-pry-byebug-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-byebug.
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
%doc CHANGELOG.md LICENSE README.md CONTRIBUTING.md code_of_conduct.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pry-byebug-doc
%doc CHANGELOG.md LICENSE README.md CONTRIBUTING.md code_of_conduct.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pry-byebug-devel
%doc CHANGELOG.md LICENSE README.md CONTRIBUTING.md code_of_conduct.md
%endif


%changelog
* Mon Jun 22 2026 Pavel Skrylev <majioa@altlinux.org> 3.12.0-alt1
- ^ 3.11.0 -> 3.12.0

* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 3.11.0-alt1
- ^ 3.9.0 -> 3.11.0

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 3.9.0-alt1
- + packaged gem with Ruby Policy 2.0
