%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname maxitest

Name:          gem-maxitest
Version:       7.1.1
Release:       alt1
Summary:       Minitest + all the features you always wanted
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/maxitest
Vcs:           https://github.com/grosser/maxitest.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rake) >= 0
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      ruby >= 3.2
Requires:      gem(debug) >= 0
Requires:      gem(minitest) >= 6.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rake) >= 0
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rubocop) >= 2
Provides:      gem(maxitest) = 7.1.1

%description
Minitest + all the features you always wanted.


%if_enabled    doc
%package       -n gem-maxitest-doc
Version:       7.1.1
Release:       alt1
Summary:       Minitest + all the features you always wanted documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета maxitest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(maxitest) = 7.1.1

%description   -n gem-maxitest-doc
Minitest + all the features you always wanted documentation files.

%description   -n gem-maxitest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета maxitest.
%endif


%if_enabled    devel
%package       -n gem-maxitest-devel
Version:       7.1.1
Release:       alt1
Summary:       Minitest + all the features you always wanted development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета maxitest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(maxitest) = 7.1.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-maxitest-devel
Minitest + all the features you always wanted development package.

%description   -n gem-maxitest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета maxitest.
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
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-maxitest-doc
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-maxitest-devel
%doc CHANGELOG.md MIT-LICENSE README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 7.1.1-alt1
- ^ 3.6.0 -> 7.1.1

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- + packaged gem with Ruby Policy 2.0
