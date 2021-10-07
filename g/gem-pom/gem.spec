%define        gemname pom

Name:          gem-pom
Version:       0.0.1
Release:       alt1
Summary:       A simple command-line Pomodoro timer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/midwire/pom
Vcs:           https://github.com/midwire/pom.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
# BuildRequires: gem(guard) >= 0
# BuildRequires: gem(guard-bundler) >= 0
# BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(midwire_common) >= 0.1.4
BuildRequires: gem(timers) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(thor) >= 0
Requires:      gem(midwire_common) >= 0.1.4
Requires:      gem(timers) >= 0
Provides:      gem(pom) = 0.0.1


%description
A simple command-line Pomodoro timer.


%package       -n pom
Version:       0.0.1
Release:       alt1
Summary:       A simple command-line Pomodoro timer executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pom
Group:         Other
BuildArch:     noarch

Requires:      gem(pom) = 0.0.1

%description   -n pom
A simple command-line Pomodoro timer executable(s).

%description   -n pom -l ru_RU.UTF-8
Исполнямка для самоцвета pom.


%package       -n gem-pom-doc
Version:       0.0.1
Release:       alt1
Summary:       A simple command-line Pomodoro timer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pom
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pom) = 0.0.1

%description   -n gem-pom-doc
A simple command-line Pomodoro timer documentation files.

%description   -n gem-pom-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pom.


%package       -n gem-pom-devel
Version:       0.0.1
Release:       alt1
Summary:       A simple command-line Pomodoro timer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pom
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pom) = 0.0.1
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
# Requires:      gem(guard) >= 0
# Requires:      gem(guard-bundler) >= 0
# Requires:      gem(guard-rspec) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-pom-devel
A simple command-line Pomodoro timer development package.

%description   -n gem-pom-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pom.


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

%files         -n pom
%doc README.md
%_bindir/pom

%files         -n gem-pom-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pom-devel
%doc README.md


%changelog
* Wed Oct 06 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + packaged gem with Ruby Policy 2.0
