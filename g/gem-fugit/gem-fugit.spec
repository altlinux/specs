%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fugit

Name:          gem-fugit
Version:       1.10.1
Release:       alt1
Summary:       time tools (cron, parsing, durations, ...) for Ruby and flor
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/floraison/fugit
Vcs:           https://github.com/floraison/fugit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(chronic) >= 0.10
BuildRequires: gem(raabro) >= 1.4
BuildRequires: gem(et-orbi) >= 1.2.7
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(chronic) >= 1
BuildConflicts: gem(raabro) >= 2
BuildConflicts: gem(et-orbi) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(raabro) >= 1.4
Requires:      gem(et-orbi) >= 1.2.7
Conflicts:     gem(raabro) >= 2
Conflicts:     gem(et-orbi) >= 2
Obsoletes:     ruby-fugit < %EVR
Provides:      ruby-fugit = %EVR
Provides:      gem(fugit) = 1.10.1


%description
time tools (cron, parsing, durations, ...) for Ruby and flor


%if_enabled    doc
%package       -n gem-fugit-doc
Version:       1.10.1
Release:       alt1
Summary:       time tools (cron, parsing, durations, ...) for Ruby and flor documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fugit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fugit) = 1.10.1

%description   -n gem-fugit-doc
time tools (cron, parsing, durations, ...) for Ruby and flor documentation
files.

%description   -n gem-fugit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fugit.
%endif


%if_enabled    devel
%package       -n gem-fugit-devel
Version:       1.10.1
Release:       alt1
Summary:       time tools (cron, parsing, durations, ...) for Ruby and flor development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fugit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fugit) = 1.10.1
Requires:      gem(rspec) >= 3.8
Requires:      gem(chronic) >= 0.10
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(chronic) >= 1

%description   -n gem-fugit-devel
time tools (cron, parsing, durations, ...) for Ruby and flor development
package.

%description   -n gem-fugit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fugit.
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
%files         -n gem-fugit-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fugit-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt1
- > Ruby Policy 2.0
- ^ 1.1.6 -> 1.10.1

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
