%define        gemname websocket-extensions

Name:          gem-websocket-extensions
Version:       0.1.5
Release:       alt1
Summary:       Generic extension management for WebSocket connections
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/faye/websocket-extensions-ruby
Vcs:           https://github.com/faye/websocket-extensions-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     websocket-extensions-ruby < %EVR
Provides:      websocket-extensions-ruby = %EVR
Provides:      gem(websocket-extensions) = 0.1.5


%description
A minimal framework that supports the implementation of WebSocket extensions in
a way that's decoupled from the main protocol. This library aims to allow a
WebSocket extension to be written and used with any protocol library, by
defining abstract representations of frames and messages that allow modules to
co-operate.


%package       -n gem-websocket-extensions-doc
Version:       0.1.5
Release:       alt1
Summary:       Generic extension management for WebSocket connections documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета websocket-extensions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(websocket-extensions) = 0.1.5

%description   -n gem-websocket-extensions-doc
Generic extension management for WebSocket connections documentation files.

A minimal framework that supports the implementation of WebSocket extensions in
a way that's decoupled from the main protocol. This library aims to allow a
WebSocket extension to be written and used with any protocol library, by
defining abstract representations of frames and messages that allow modules to
co-operate.

%description   -n gem-websocket-extensions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета websocket-extensions.


%package       -n gem-websocket-extensions-devel
Version:       0.1.5
Release:       alt1
Summary:       Generic extension management for WebSocket connections development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета websocket-extensions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(websocket-extensions) = 0.1.5
Requires:      gem(rspec) >= 0 gem(rspec) < 4

%description   -n gem-websocket-extensions-devel
Generic extension management for WebSocket connections development package.

A minimal framework that supports the implementation of WebSocket extensions in
a way that's decoupled from the main protocol. This library aims to allow a
WebSocket extension to be written and used with any protocol library, by
defining abstract representations of frames and messages that allow modules to
co-operate.

%description   -n gem-websocket-extensions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета websocket-extensions.


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

%files         -n gem-websocket-extensions-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-websocket-extensions-devel
%doc README.md


%changelog
* Sat Jun 26 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- ^ 0.1.4 -> 0.1.5

* Mon Aug 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
^ v0.1.4
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus
