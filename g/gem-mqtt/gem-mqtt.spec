%define        gemname mqtt

Name:          gem-mqtt
Version:       0.5.0
Release:       alt1
Summary:       Implementation of the MQTT protocol
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/njh/ruby-mqtt
Vcs:           https://github.com/njh/ruby-mqtt.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.11.2
BuildRequires: gem(rake) >= 10.2.2
BuildRequires: gem(yard) >= 0.8.7
BuildRequires: gem(rspec) >= 3.5.0
BuildRequires: gem(simplecov) >= 0.9.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(mqtt) = 0.5.0


%description
Pure Ruby gem that implements the MQTT protocol, a lightweight protocol for
publish/subscribe messaging.


%package       -n gem-mqtt-doc
Version:       0.5.0
Release:       alt1
Summary:       Implementation of the MQTT protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mqtt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mqtt) = 0.5.0

%description   -n gem-mqtt-doc
Implementation of the MQTT protocol documentation files.

Pure Ruby gem that implements the MQTT protocol, a lightweight protocol for
publish/subscribe messaging.

%description   -n gem-mqtt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mqtt.


%package       -n gem-mqtt-devel
Version:       0.5.0
Release:       alt1
Summary:       Implementation of the MQTT protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mqtt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mqtt) = 0.5.0
Requires:      gem(bundler) >= 1.11.2
Requires:      gem(rake) >= 10.2.2
Requires:      gem(yard) >= 0.8.7
Requires:      gem(rspec) >= 3.5.0
Requires:      gem(simplecov) >= 0.9.2

%description   -n gem-mqtt-devel
Implementation of the MQTT protocol development package.

Pure Ruby gem that implements the MQTT protocol, a lightweight protocol for
publish/subscribe messaging.

%description   -n gem-mqtt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mqtt.


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

%files         -n gem-mqtt-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mqtt-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
