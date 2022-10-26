%define        gemname foreman_maintain

Name:          gem-foreman-maintain
Version:       1.1.6
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
BuildRequires: gem(clamp) >= 0
BuildRequires: gem(highline) >= 0
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0.50.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(clamp) >= 0
Requires:      gem(highline) >= 0
Provides:      gem(foreman_maintain) = 1.1.6

%ruby_alias_names foreman_maintain,foreman-maintain

%description
Provides various features that helps keeping the Foreman/Satellite up and
running.


%package       -n foreman-maintain
Version:       1.1.6
Release:       alt1
Summary:       Foreman maintenance tool belt executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета foreman_maintain
Group:         Other
BuildArch:     noarch

Requires:      gem(foreman_maintain) = 1.1.6

%description   -n foreman-maintain
Foreman maintenance tool belt executable(s).

Provides various features that helps keeping the Foreman/Satellite up and
running.

%description   -n foreman-maintain -l ru_RU.UTF-8
Исполнямка для самоцвета foreman_maintain.


%package       -n gem-foreman-maintain-doc
Version:       1.1.6
Release:       alt1
Summary:       Foreman maintenance tool belt documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_maintain
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_maintain) = 1.1.6

%description   -n gem-foreman-maintain-doc
Foreman maintenance tool belt documentation files.

Provides various features that helps keeping the Foreman/Satellite up and
running.

%description   -n gem-foreman-maintain-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_maintain.


%package       -n gem-foreman-maintain-devel
Version:       1.1.6
Release:       alt1
Summary:       Foreman maintenance tool belt development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_maintain
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_maintain) = 1.1.6
Requires:      gem(bundler) >= 1.17
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0.50.0 gem(rubocop) < 2

%description   -n gem-foreman-maintain-devel
Foreman maintenance tool belt development package.

Provides various features that helps keeping the Foreman/Satellite up and
running.

%description   -n gem-foreman-maintain-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_maintain.


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

%files         -n gem-foreman-maintain-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-maintain-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.6-alt1
- + packaged gem with Ruby Policy 2.0
