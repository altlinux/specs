%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname slop

Name:          gem-slop
Version:       4.10.1
Release:       alt1
Summary:       Simple Lightweight Option Parsing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/leejarvis/slop
Vcs:           https://github.com/leejarvis/slop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.0.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      ruby >= 2.0.0
Conflicts:     ruby-slop
Obsoletes:     ruby-slop3 < %EVR
Provides:      ruby-slop3 = %EVR
Provides:      gem(slop) = 4.10.1

%description
Slop is a simple option parser with an easy to remember syntax and friendly API.


%if_enabled    doc
%package       -n gem-slop-doc
Version:       4.10.1
Release:       alt1
Summary:       Simple Lightweight Option Parsing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета slop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(slop) = 4.10.1

%description   -n gem-slop-doc
Simple Lightweight Option Parsing documentation files.

Slop is a simple option parser with an easy to remember syntax and friendly API.

%description   -n gem-slop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета slop.
%endif


%if_enabled    devel
%package       -n gem-slop-devel
Version:       4.10.1
Release:       alt1
Summary:       Simple Lightweight Option Parsing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета slop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(slop) = 4.10.1
Requires:      gem(minitest) >= 5.0.0
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 7

%description   -n gem-slop-devel
Simple Lightweight Option Parsing development package.

Slop is a simple option parser with an easy to remember syntax and friendly API.

%description   -n gem-slop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета slop.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-slop-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-slop-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Aug 24 2026 Pavel Skrylev <majioa@altlinux.org> 4.10.1-alt1
- ^ 4.9.1 -> 4.10.1

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 4.9.1-alt1
- ^ 3.6.0 -> 4.9.1
- * policify name

* Sun May 21 2017 Gordeev Mikhail <obirvalger@altlinux.org> 3.6.0-alt1
- Initial build in Sisyphus
