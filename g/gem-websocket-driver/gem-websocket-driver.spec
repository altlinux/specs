%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname websocket-driver

Name:          gem-websocket-driver
Version:       0.7.6
Release:       alt1
Summary:       WebSocket protocol handler with pluggable I/O
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/faye/websocket-driver-ruby
Vcs:           https://github.com/faye/websocket-driver-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(eventmachine) >= 0
BuildRequires: gem(permessage_deflate) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(websocket-extensions) >= 0.1.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(websocket-extensions) >= 0.1.0
Obsoletes:     websocket-driver-ruby < %EVR
Provides:      websocket-driver-ruby = %EVR
Provides:      gem(websocket-driver) = 0.7.6


%description
This module provides a complete implementation of the WebSocket protocols that
can be hooked up to any TCP library. It aims to simplify things by decoupling
the protocol details from the I/O layer, such that users only need to implement
code to stream data in and out of it without needing to know anything about how
the protocol actually works. Think of it as a complete WebSocket system with
pluggable I/O.


%if_enabled    doc
%package       -n gem-websocket-driver-doc
Version:       0.7.6
Release:       alt1
Summary:       WebSocket protocol handler with pluggable I/O documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета websocket-driver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(websocket-driver) = 0.7.6
Obsoletes:     websocket-driver-ruby-doc
Provides:      websocket-driver-ruby-doc

%description   -n gem-websocket-driver-doc
WebSocket protocol handler with pluggable I/O documentation files.

This module provides a complete implementation of the WebSocket protocols that
can be hooked up to any TCP library. It aims to simplify things by decoupling
the protocol details from the I/O layer, such that users only need to implement
code to stream data in and out of it without needing to know anything about how
the protocol actually works. Think of it as a complete WebSocket system with
pluggable I/O.

%description   -n gem-websocket-driver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета websocket-driver.
%endif


%if_enabled    devel
%package       -n gem-websocket-driver-devel
Version:       0.7.6
Release:       alt1
Summary:       WebSocket protocol handler with pluggable I/O development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета websocket-driver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(websocket-driver) = 0.7.6
Requires:      gem(eventmachine) >= 0
Requires:      gem(permessage_deflate) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-websocket-driver-devel
WebSocket protocol handler with pluggable I/O development package.

This module provides a complete implementation of the WebSocket protocols that
can be hooked up to any TCP library. It aims to simplify things by decoupling
the protocol details from the I/O layer, such that users only need to implement
code to stream data in and out of it without needing to know anything about how
the protocol actually works. Think of it as a complete WebSocket system with
pluggable I/O.

%description   -n gem-websocket-driver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета websocket-driver.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-websocket-driver-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-websocket-driver-devel
%doc README.md
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.6-alt1
- ^ 0.7.5 -> 0.7.6

* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- ^ 0.7.1 -> 0.7.5

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- updated (^) v0.7.1

* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt2
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
