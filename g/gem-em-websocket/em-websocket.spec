%define        gemname em-websocket

Name:          gem-em-websocket
Version:       0.5.2
Release:       alt1.1
Summary:       EventMachine based WebSocket server
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/igrigorik/em-websocket/
Vcs:           https://github.com/igrigorik/em-websocket.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(eventmachine) >= 0.12.9
BuildRequires: gem(http_parser.rb) >= 0.6.0 gem(http_parser.rb) < 0.7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(eventmachine) >= 0.12.9
Requires:      gem(http_parser.rb) >= 0.6.0 gem(http_parser.rb) < 0.7
Provides:      gem(em-websocket) = 0.5.2


%description
EventMachine based WebSocket server


%package       -n gem-em-websocket-doc
Version:       0.5.2
Release:       alt1.1
Summary:       EventMachine based WebSocket server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета em-websocket
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(em-websocket) = 0.5.2

%description   -n gem-em-websocket-doc
EventMachine based WebSocket server documentation files.

%description   -n gem-em-websocket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета em-websocket.


%package       -n gem-em-websocket-devel
Version:       0.5.2
Release:       alt1.1
Summary:       EventMachine based WebSocket server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета em-websocket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(em-websocket) = 0.5.2

%description   -n gem-em-websocket-devel
EventMachine based WebSocket server development package.

%description   -n gem-em-websocket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета em-websocket.


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

%files         -n gem-em-websocket-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-em-websocket-devel
%doc README.md


%changelog
* Mon Sep 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1.1
- ! spec

* Tue Mar 21 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.5.2-alt1
- initial build
