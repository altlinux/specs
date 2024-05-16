%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname raabro

Name:          gem-raabro
Version:       1.4.0
Release:       alt1
Summary:       a Ruby version of flon-io/aabro
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/floraison/raabro
Vcs:           https://github.com/floraison/raabro.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.7
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-raabro < %EVR
Provides:      ruby-raabro = %EVR
Provides:      gem(raabro) = 1.4.0


%description
a Ruby version of flon-io/aabro


%if_enabled    doc
%package       -n gem-raabro-doc
Version:       1.4.0
Release:       alt1
Summary:       a Ruby version of flon-io/aabro documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета raabro
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(raabro) = 1.4.0

%description   -n gem-raabro-doc
a Ruby version of flon-io/aabro documentation files.

%description   -n gem-raabro-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета raabro.
%endif


%if_enabled    devel
%package       -n gem-raabro-devel
Version:       1.4.0
Release:       alt1
Summary:       a Ruby version of flon-io/aabro development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета raabro
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(raabro) = 1.4.0
Requires:      gem(rspec) >= 3.7
Conflicts:     gem(rspec) >= 4

%description   -n gem-raabro-devel
a Ruby version of flon-io/aabro development package.

%description   -n gem-raabro-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета raabro.
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
%files         -n gem-raabro-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-raabro-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- > Ruby Policy 2.0
- ^ 1.1.6 -> 1.4.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus
