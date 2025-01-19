%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gem-wrappers

Name:          gem-gem-wrappers
Version:       1.4.0.1
Release:       alt0.1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/rvm/gem-wrappers
Vcs:           https://github.com/rvm/gem-wrappers.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(gem-wrappers) = 1.4.0.1

%ruby_use_gem_version gem-wrappers:1.4.0.1

%description
Create gem wrappers for easy use of gems in cron and other system locations.


%if_enabled    doc
%package       -n gem-gem-wrappers-doc
Version:       1.4.0.1
Release:       alt0.1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem-wrappers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem-wrappers) = 1.4.0.1

%description   -n gem-gem-wrappers-doc
Create gem wrappers for easy use of gems in cron and other system locations
documentation files.

%description   -n gem-gem-wrappers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem-wrappers.
%endif


%if_enabled    devel
%package       -n gem-gem-wrappers-devel
Version:       1.4.0.1
Release:       alt0.1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gem-wrappers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libruby-devel
Requires:      gem(gem-wrappers) = 1.4.0.1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Obsoletes:     gem-wrappers-devel < %EVR
Provides:      gem-wrappers-devel = %EVR

%description   -n gem-gem-wrappers-devel
Create gem wrappers for easy use of gems in cron and other system locations
development package.

%description   -n gem-gem-wrappers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gem-wrappers.
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
%doc Changelog.md LICENSE README.md
%ruby_gemspec
%ruby_gemplugin
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-gem-wrappers-doc
%doc Changelog.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gem-wrappers-devel
%doc Changelog.md LICENSE README.md
%endif


%changelog
* Fri Dec 13 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0.1-alt0.1
- ^ 1.4.0 -> 1.4.0p1
- ! fixed build for spec
- ! closes wrapper installation in rescue clause

* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1.1
- + added plugin script for the gem (closes #49696)

* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with Ruby Policy 2.0 without devel
