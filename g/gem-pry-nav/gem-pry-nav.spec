%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pry-nav

Name:          gem-pry-nav
Version:       1.0.0
Release:       alt1
Summary:       Simple execution navigation for Pry
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nixme/pry-nav
Vcs:           https://github.com/nixme/pry-nav.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(pry) >= 0.9.10
BuildRequires: gem(pry-remote) >= 0
BuildConflicts: gem(pry) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(pry) >= 0.9.10
Conflicts:     gem(pry) >= 1
Provides:      gem(pry-nav) = 1.0.0


%description
Turn Pry into a primitive debugger. Adds 'step' and 'next' commands to control
execution.


%if_enabled    doc
%package       -n gem-pry-nav-doc
Version:       1.0.0
Release:       alt1
Summary:       Simple execution navigation for Pry documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-nav
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-nav) = 1.0.0

%description   -n gem-pry-nav-doc
Simple execution navigation for Pry documentation files.

%description   -n gem-pry-nav-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-nav.
%endif


%if_enabled    devel
%package       -n gem-pry-nav-devel
Version:       1.0.0
Release:       alt1
Summary:       Simple execution navigation for Pry development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-nav
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-nav) = 1.0.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(pry-remote) >= 0

%description   -n gem-pry-nav-devel
Simple execution navigation for Pry development package.

%description   -n gem-pry-nav-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-nav.
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
%files         -n gem-pry-nav-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pry-nav-devel
%doc README.md
%endif


%changelog
* Thu Oct 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
