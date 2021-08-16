%define        gemname train-habitat

Name:          gem-train-habitat
Version:       0.2.32
Release:       alt1
Summary:       Habitat API Transport for Train
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train-habitat
Vcs:           https://github.com/inspec/train-habitat.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(train-habitat) = 0.2.32


%description
Allows applications using Train to speak to Habitat.

train-habitat is a Train plugin and is used as a Train Transport to connect to
Habitat installations.


%package       -n gem-train-habitat-doc
Version:       0.2.32
Release:       alt1
Summary:       Habitat API Transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-habitat
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-habitat) = 0.2.32

%description   -n gem-train-habitat-doc
Habitat API Transport for Train documentation files.

Allows applications using Train to speak to Habitat.

train-habitat is a Train plugin and is used as a Train Transport to connect to
Habitat installations.

%description   -n gem-train-habitat-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-habitat.


%package       -n gem-train-habitat-devel
Version:       0.2.32
Release:       alt1
Summary:       Habitat API Transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-habitat
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-habitat) = 0.2.32
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(rake) >= 13.0 gem(rake) < 14

%description   -n gem-train-habitat-devel
Habitat API Transport for Train development package.

Allows applications using Train to speak to Habitat.

train-habitat is a Train plugin and is used as a Train Transport to connect to
Habitat installations.

%description   -n gem-train-habitat-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-habitat.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-train-habitat-doc
%ruby_gemdocdir

%files         -n gem-train-habitat-devel


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.32-alt1
- + packaged gem with Ruby Policy 2.0
