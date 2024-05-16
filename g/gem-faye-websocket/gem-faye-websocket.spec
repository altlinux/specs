%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname faye-websocket

Name:          gem-faye-websocket
Version:       0.11.3
Release:       alt1
Summary:       Standards-compliant WebSocket server and client
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/faye/faye-websocket-ruby
Vcs:           https://github.com/faye/faye-websocket-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(permessage_deflate) >= 0
BuildRequires: gem(progressbar) >= 0
BuildRequires: gem(puma) >= 2.0.0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-eventmachine) >= 0.2.0
BuildRequires: gem(thin) >= 1.2.0
BuildRequires: gem(rainbows) >= 4.4.0
BuildRequires: gem(goliath) > 0
BuildRequires: gem(passenger) >= 4.0.0
BuildRequires: gem(eventmachine) >= 0.12.0
BuildRequires: gem(websocket-driver) >= 0.5.1
BuildConflicts: gem(puma) >= 6
BuildConflicts: gem(rainbows) >= 4.5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(eventmachine) >= 0.12.0
Requires:      gem(websocket-driver) >= 0.5.1
Provides:      gem(faye-websocket) = 0.11.3


%description
Standards-compliant WebSocket server and client


%if_enabled    doc
%package       -n gem-faye-websocket-doc
Version:       0.11.3
Release:       alt1
Summary:       Standards-compliant WebSocket server and client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faye-websocket
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faye-websocket) = 0.11.3

%description   -n gem-faye-websocket-doc
Standards-compliant WebSocket server and client documentation files.

%description   -n gem-faye-websocket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faye-websocket.
%endif


%if_enabled    devel
%package       -n gem-faye-websocket-devel
Version:       0.11.3
Release:       alt1
Summary:       Standards-compliant WebSocket server and client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faye-websocket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faye-websocket) = 0.11.3
Requires:      gem(permessage_deflate) >= 0
Requires:      gem(progressbar) >= 0
Requires:      gem(puma) >= 2.0.0
Requires:      gem(rack) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rspec-eventmachine) >= 0.2.0
Requires:      gem(thin) >= 1.2.0
Requires:      gem(rainbows) >= 4.4.0
Requires:      gem(goliath) > 0
Requires:      gem(passenger) >= 4.0.0
Conflicts:     gem(puma) >= 6
Conflicts:     gem(rainbows) >= 4.5

%description   -n gem-faye-websocket-devel
Standards-compliant WebSocket server and client development package.

%description   -n gem-faye-websocket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faye-websocket.
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

%if_enabled    doc
%files         -n gem-faye-websocket-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faye-websocket-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.11.3-alt1
- + packaged gem with Ruby Policy 2.0
