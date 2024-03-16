%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gem-wrappers

Name:          gem-gem-wrappers
Version:       1.4.0
Release:       alt1.1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/rvm/gem-wrappers
Vcs:           https://github.com/rvm/gem-wrappers.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(gem-wrappers) = 1.4.0


%description
Create gem wrappers for easy use of gems in cron and other system locations.


%if_enabled    doc
%package       -n gem-gem-wrappers-doc
Version:       1.4.0
Release:       alt1.1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem-wrappers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem-wrappers) = 1.4.0

%description   -n gem-gem-wrappers-doc
Create gem wrappers for easy use of gems in cron and other system locations
documentation files.

%description   -n gem-gem-wrappers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem-wrappers.
%endif


%if_enabled    devel
%package       -n gem-wrappers-devel
Version:       1.4.0
Release:       alt1.1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gem-wrappers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libruby-devel
Requires:      gem(gem-wrappers) = 1.4.0
Requires:      gem(redcarpet) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6

%description   -n gem-wrappers-devel
Create gem wrappers for easy use of gems in cron and other system locations
development package.

%description   -n gem-wrappers-devel -l ru_RU.UTF-8
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
%doc README.md
%ruby_gemspec
%ruby_gemplugin
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-gem-wrappers-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-wrappers-devel
%doc README.md
%endif


%changelog
* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1.1
- + added plugin script for the gem (closes #49696)

* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with Ruby Policy 2.0 without devel
