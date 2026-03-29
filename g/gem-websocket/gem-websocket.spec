# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname websocket

Name:          gem-websocket
Version:       1.2.11
Release:       alt1
Summary:       Universal Ruby library to handle WebSocket protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/imanel/websocket-ruby
Vcs:           https://github.com/imanel/websocket-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rubocop) >= 0.52.1
BuildRequires: gem(rubocop-rspec) >= 1.21.0
BuildRequires: gem(webrick) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
Requires:      ruby >= 2.0
Provides:      websocket = %EVR
Provides:      gem(websocket) = 1.2.11

%description
Universal Ruby library to handle WebSocket protocol. It focuses on providing
abstraction layer over WebSocket API instead of providing server or client
functionality.


%if_enabled    doc
%package       -n gem-websocket-doc
Version:       1.2.11
Release:       alt1
Summary:       Universal Ruby library to handle WebSocket protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета websocket
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(websocket) = 1.2.11

%description   -n gem-websocket-doc
Universal Ruby library to handle WebSocket protocol documentation
files.

Universal Ruby library to handle WebSocket protocol. It focuses on providing
abstraction layer over WebSocket API instead of providing server or client
functionality.

%description   -n gem-websocket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета websocket.
%endif


%if_enabled    devel
%package       -n gem-websocket-devel
Version:       1.2.11
Release:       alt1
Summary:       Universal Ruby library to handle WebSocket protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета websocket
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(websocket) = 1.2.11
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.7
Requires:      gem(rubocop) >= 0.52.1
Requires:      gem(rubocop-rspec) >= 1.21.0
Requires:      gem(webrick) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-websocket-devel
Universal Ruby library to handle WebSocket protocol development
package.

Universal Ruby library to handle WebSocket protocol. It focuses on providing
abstraction layer over WebSocket API instead of providing server or client
functionality.

%description   -n gem-websocket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета websocket.
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
%doc CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-websocket-doc
%doc CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-websocket-devel
%doc CHANGELOG.md README.md
%endif


%changelog
* Sun Mar 29 2026 Pavel Skrylev <majioa@altlinux.org> 1.2.11-alt1
- ^ 1.2.10 -> 1.2.11

* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.2.10-alt1
- ^ 1.2.8 -> 1.2.10

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.8-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
