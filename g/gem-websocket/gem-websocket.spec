# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%define        gemname websocket

Name:          gem-websocket
Version:       1.2.10
Release:       alt1
Summary:       Universal Ruby library to handle WebSocket protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/imanel/websocket-ruby
Vcs:           https://github.com/imanel/websocket-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(rubocop) >= 0.52.1
BuildRequires: gem(rubocop-rspec) >= 1.21.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
Provides:      gem(websocket) = 1.2.10


%description
Universal Ruby library to handle WebSocket protocol. It focuses on providing
abstraction layer over WebSocket API instead of providing server or client
functionality.


%package       -n gem-websocket-doc
Version:       1.2.10
Release:       alt1
Summary:       Universal Ruby library to handle WebSocket protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета websocket
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(websocket) = 1.2.10

%description   -n gem-websocket-doc
Universal Ruby library to handle WebSocket protocol documentation
files.

Universal Ruby library to handle WebSocket protocol. It focuses on providing
abstraction layer over WebSocket API instead of providing server or client
functionality.

%description   -n gem-websocket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета websocket.


%package       -n gem-websocket-devel
Version:       1.2.10
Release:       alt1
Summary:       Universal Ruby library to handle WebSocket protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета websocket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(websocket) = 1.2.10
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.7
Requires:      gem(webrick) >= 0
Requires:      gem(rubocop) >= 0.52.1
Requires:      gem(rubocop-rspec) >= 1.21.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rspec) >= 3

%description   -n gem-websocket-devel
Universal Ruby library to handle WebSocket protocol development
package.

Universal Ruby library to handle WebSocket protocol. It focuses on providing
abstraction layer over WebSocket API instead of providing server or client
functionality.

%description   -n gem-websocket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета websocket.


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

%files         -n gem-websocket-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-websocket-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.2.10-alt1
- ^ 1.2.8 -> 1.2.10

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.8-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
