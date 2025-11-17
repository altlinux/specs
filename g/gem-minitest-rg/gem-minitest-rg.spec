%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-rg

Name:          gem-minitest-rg
Version:       5.3.0
Release:       alt1
Summary:       Red/Green for MiniTest
License:       MIT
Group:         Development/Ruby
Url:           http://blowmage.com/minitest-rg
Vcs:           https://github.com/minitest/minitest-rg.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 4.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(minitest) >= 6
Provides:      gem(minitest-rg) = 5.3.0

%description
Colored red/green output for Minitest


%if_enabled    doc
%package       -n gem-minitest-rg-doc
Version:       5.3.0
Release:       alt1
Summary:       Red/Green for MiniTest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-rg
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-rg) = 5.3.0

%description   -n gem-minitest-rg-doc
Red/Green for MiniTest documentation files.

Colored red/green output for Minitest

%description   -n gem-minitest-rg-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-rg.
%endif


%if_enabled    devel
%package       -n gem-minitest-rg-devel
Version:       5.3.0
Release:       alt1
Summary:       Red/Green for MiniTest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-rg
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-rg) = 5.3.0
Requires:      gem(hoe) >= 4.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rubocop) >= 2

%description   -n gem-minitest-rg-devel
Red/Green for MiniTest development package.

Colored red/green output for Minitest

%description   -n gem-minitest-rg-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-rg.
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
%doc CHANGELOG.rdoc LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-rg-doc
%doc CHANGELOG.rdoc LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-rg-devel
%doc CHANGELOG.rdoc LICENSE README.rdoc
%endif


%changelog
* Mon Nov 03 2025 Pavel Skrylev <majioa@altlinux.org> 5.3.0-alt1
- ^ 5.2.0 -> 5.3.0

* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt1.1
- ! spec

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt1
- + packaged gem with Ruby Policy 2.0
