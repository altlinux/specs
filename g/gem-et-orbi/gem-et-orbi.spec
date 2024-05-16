%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname et-orbi

Name:          gem-et-orbi
Version:       1.2.11
Release:       alt1
Summary:       Time zones for fugit and rufus-scheduler. Urbi et Orbi
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/floraison/et-orbi
Vcs:           https://github.com/floraison/et-orbi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(chronic) >= 0.10
BuildRequires: gem(tzinfo) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(chronic) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(tzinfo) >= 0
Obsoletes:     ruby-et-orbi < %EVR
Provides:      ruby-et-orbi = %EVR
Provides:      gem(et-orbi) = 1.2.11


%description
Time zones for fugit and rufus-scheduler. Urbi et Orbi.


%if_enabled    doc
%package       -n gem-et-orbi-doc
Version:       1.2.11
Release:       alt1
Summary:       Time zones for fugit and rufus-scheduler. Urbi et Orbi documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета et-orbi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(et-orbi) = 1.2.11

%description   -n gem-et-orbi-doc
Time zones for fugit and rufus-scheduler. Urbi et Orbi documentation files.

%description   -n gem-et-orbi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета et-orbi.
%endif


%if_enabled    devel
%package       -n gem-et-orbi-devel
Version:       1.2.11
Release:       alt1
Summary:       Time zones for fugit and rufus-scheduler. Urbi et Orbi development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета et-orbi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(et-orbi) = 1.2.11
Requires:      gem(rspec) >= 3.8
Requires:      gem(chronic) >= 0.10
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(chronic) >= 1

%description   -n gem-et-orbi-devel
Time zones for fugit and rufus-scheduler. Urbi et Orbi development package.

%description   -n gem-et-orbi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета et-orbi.
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
%files         -n gem-et-orbi-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-et-orbi-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.11-alt1
- > Ruby Policy 2.0
- ^ 1.1.6 -> 1.2.11

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
