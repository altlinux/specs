%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-line

Name:          gem-minitest-line
Version:       0.6.5
Release:       alt1
Summary:       Focused tests for Minitest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/judofyr/minitest-line
Vcs:           https://github.com/judofyr/minitest-line.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      ruby >= 2.0.0
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(minitest) >= 7
Provides:      gem(minitest-line) = 0.6.5

%description
Focused tests for Minitest


%if_enabled    doc
%package       -n gem-minitest-line-doc
Version:       0.6.5
Release:       alt1
Summary:       Focused tests for Minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-line
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-line) = 0.6.5

%description   -n gem-minitest-line-doc
Focused tests for Minitest documentation files.

%description   -n gem-minitest-line-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-line.
%endif


%if_enabled    devel
%package       -n gem-minitest-line-devel
Version:       0.6.5
Release:       alt1
Summary:       Focused tests for Minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-line
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-line) = 0.6.5
Requires:      gem(rake) >= 0

%description   -n gem-minitest-line-devel
Focused tests for Minitest development package.

%description   -n gem-minitest-line-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-line.
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
%doc CHANGELOG.md MIT-LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-line-doc
%doc CHANGELOG.md MIT-LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-line-devel
%doc CHANGELOG.md MIT-LICENSE.txt README.md
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 0.6.5-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
