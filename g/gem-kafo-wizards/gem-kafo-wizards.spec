%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname kafo_wizards

Name:          gem-kafo-wizards
Version:       1.0.0
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation
License:       GPL-3.0-or-later
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo_wizards
Vcs:           https://github.com/theforeman/kafo_wizards.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 4.0
BuildRequires: gem(mocha) >= 2.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(highline) >= 4
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 4.0
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_alias_names kafo_wizards,kafo-wizards
Requires:      ruby >= 2.7
Conflicts:     ruby >= 5
Conflicts:     gem(highline) >= 4
Conflicts:     gem(logger) >= 2
Provides:      gem(kafo_wizards) = 1.0.0

%description
With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on the
chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.


%if_enabled    doc
%package       -n gem-kafo-wizards-doc
Version:       1.0.0
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kafo_wizards
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kafo_wizards) = 1.0.0

%description   -n gem-kafo-wizards-doc
This gem helps to create wizard like interfaces in terminal applications, has
support for nesting and value validation documentation files.

With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on the
chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.

%description   -n gem-kafo-wizards-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kafo_wizards.
%endif


%if_enabled    devel
%package       -n gem-kafo-wizards-devel
Version:       1.0.0
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kafo_wizards
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kafo_wizards) = 1.0.0
Requires:      gem(minitest) >= 4.0
Requires:      gem(mocha) >= 2.1
Requires:      gem(rake) >= 13.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1

%description   -n gem-kafo-wizards-devel
This gem helps to create wizard like interfaces in terminal applications, has
support for nesting and value validation development package.

With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on the
chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.

%description   -n gem-kafo-wizards-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kafo_wizards.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-kafo-wizards-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-kafo-wizards-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.0.2p6 -> 1.0.0

* Thu Oct 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.0.2.6-alt1
- ^ 0.0.2 -> 0.0.2p6

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- ^ 0.0.1 -> 0.0.2

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
