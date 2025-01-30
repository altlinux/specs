%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_maintain

Name:          gem-foreman-maintain
Version:       1.7.5
Release:       alt1
Summary:       Foreman maintenance tool belt
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_maintain
Vcs:           https://github.com/theforeman/foreman_maintain.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(minitest-stub-const) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(clamp) >= 0
BuildRequires: gem(highline) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_maintain,foreman-maintain
Requires:      gem(clamp) >= 0
Requires:      gem(highline) >= 0
Provides:      gem(foreman_maintain) = 1.7.5


%description
Provides various features that helps keeping the Foreman/Satellite up and
running.


%package       -n foreman-maintain
Version:       1.7.5
Release:       alt1
Summary:       Foreman maintenance tool belt executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета foreman_maintain
Group:         Other
BuildArch:     noarch

Requires:      gem(foreman_maintain) = 1.7.5

%description   -n foreman-maintain
Foreman maintenance tool belt executable(s).

Provides various features that helps keeping the Foreman/Satellite up and
running.

%description   -n foreman-maintain -l ru_RU.UTF-8
Исполнямка для самоцвета foreman_maintain.


%if_enabled    doc
%package       -n gem-foreman-maintain-doc
Version:       1.7.5
Release:       alt1
Summary:       Foreman maintenance tool belt documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_maintain
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_maintain) = 1.7.5

%description   -n gem-foreman-maintain-doc
Foreman maintenance tool belt documentation files.

Provides various features that helps keeping the Foreman/Satellite up and
running.

%description   -n gem-foreman-maintain-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_maintain.
%endif


%if_enabled    devel
%package       -n gem-foreman-maintain-devel
Version:       1.7.5
Release:       alt1
Summary:       Foreman maintenance tool belt development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_maintain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_maintain) = 1.7.5
Requires:      gem(bundler) >= 1.17
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(minitest-stub-const) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(theforeman-rubocop) >= 0
Requires:      gem(rexml) >= 0

%description   -n gem-foreman-maintain-devel
Foreman maintenance tool belt development package.

Provides various features that helps keeping the Foreman/Satellite up and
running.

%description   -n gem-foreman-maintain-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_maintain.
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

%files         -n foreman-maintain
%doc README.md
%_bindir/foreman-maintain
%_bindir/foreman-maintain-complete
%_bindir/foreman-maintain-rotate-tar

%if_enabled    doc
%files         -n gem-foreman-maintain-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-maintain-devel
%doc README.md
%endif


%changelog
* Fri Oct 04 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.5-alt1
- ^ 1.1.6 -> 1.7.5

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.6-alt1
- + packaged gem with Ruby Policy 2.0
