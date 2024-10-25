%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname kafo_wizards

Name:          gem-kafo-wizards
Version:       0.0.2.6
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation
License:       GPL-3.0+
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo_wizards
Vcs:           https://github.com/theforeman/kafo_wizards.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.5
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(minitest) >= 4.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(mocha) >= 1.11.2
BuildRequires: gem(ci_reporter) >= 1.0
BuildRequires: gem(highline) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(ci_reporter) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names kafo_wizards,kafo-wizards
Requires:      gem(highline) >= 0
Provides:      gem(kafo_wizards) = 0.0.2.6


%description
With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on the
chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.


%if_enabled    doc
%package       -n gem-kafo-wizards-doc
Version:       0.0.2.6
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kafo_wizards
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kafo_wizards) = 0.0.2.6

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
Version:       0.0.2.6
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kafo_wizards
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kafo_wizards) = 0.0.2.6
Requires:      gem(bundler) >= 1.5
Requires:      gem(rake) >= 13.0
Requires:      gem(minitest) >= 4.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(mocha) >= 1.11.2
Requires:      gem(ci_reporter) >= 1.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(ci_reporter) >= 3

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-kafo-wizards-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-kafo-wizards-devel
%doc README.md
%endif


%changelog
* Thu Oct 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.0.2.6-alt1
- ^ 0.0.2 -> 0.0.2.6

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- ^ 0.0.1 -> 0.0.2

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
