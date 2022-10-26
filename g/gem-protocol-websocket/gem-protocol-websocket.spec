%define        gemname protocol-websocket

Name:          gem-protocol-websocket
Version:       0.9.1
Release:       alt1
Summary:       A low level implementation of the WebSocket protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-websocket
Vcs:           https://github.com/socketry/protocol-websocket.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency sus >= 0.14.0,sus < 1
Requires:      gem(protocol-http) >= 0.2
Requires:      gem(protocol-http1) >= 0.2
Conflicts:     gem(protocol-http) >= 1
Conflicts:     gem(protocol-http1) >= 1
Provides:      gem(protocol-websocket) = 0.9.1


%description
A low level implementation of the WebSocket protocol.


%package       -n gem-protocol-websocket-doc
Version:       0.9.1
Release:       alt1
Summary:       A low level implementation of the WebSocket protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-websocket
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protocol-websocket) = 0.9.1

%description   -n gem-protocol-websocket-doc
A low level implementation of the WebSocket protocol documentation files.

%description   -n gem-protocol-websocket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-websocket.


%package       -n gem-protocol-websocket-devel
Version:       0.9.1
Release:       alt1
Summary:       A low level implementation of the WebSocket protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-websocket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(protocol-websocket) = 0.9.1
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(sus) >= 0.9.1
Conflicts:     gem(sus) >= 1

%description   -n gem-protocol-websocket-devel
A low level implementation of the WebSocket protocol development package.

%description   -n gem-protocol-websocket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-websocket.


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

%files         -n gem-protocol-websocket-doc
%ruby_gemdocdir

%files         -n gem-protocol-websocket-devel


%changelog
* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- + packaged gem with Ruby Policy 2.0
