%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-around

Name:          gem-minitest-around
Version:       0.6.0
Release:       alt1
Summary:       Around block for minitest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/splattael/minitest-around
Vcs:           https://github.com/splattael/minitest-around.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(cucumber) >= 0
BuildRequires: gem(forking_test_runner) >= 0
BuildRequires: gem(minitest) > 5.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) > 5.0
Conflicts:     gem(minitest) >= 7
Provides:      gem(minitest-around) = 0.6.0

%description
Alternative for setup/teardown dance.


%if_enabled    doc
%package       -n gem-minitest-around-doc
Version:       0.6.0
Release:       alt1
Summary:       Around block for minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-around
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-around) = 0.6.0

%description   -n gem-minitest-around-doc
Around block for minitest documentation files.

Alternative for setup/teardown dance.

%description   -n gem-minitest-around-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-around.
%endif


%if_enabled    devel
%package       -n gem-minitest-around-devel
Version:       0.6.0
Release:       alt1
Summary:       Around block for minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-around
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-around) = 0.6.0
Requires:      gem(bump) >= 0
Requires:      gem(cucumber) >= 0
Requires:      gem(forking_test_runner) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-minitest-around-devel
Around block for minitest development package.

Alternative for setup/teardown dance.

%description   -n gem-minitest-around-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-around.
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

%if_enabled    doc
%files         -n gem-minitest-around-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-around-devel
%doc LICENSE README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- ^ 0.5.0 -> 0.6.0
- * define explicit dependencies

* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
