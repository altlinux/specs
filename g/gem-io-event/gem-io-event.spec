%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname io-event

Name:          gem-io-event
Version:       1.22.0
Release:       alt1
Summary:       An event loop
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/event
Vcs:           https://github.com/socketry/event.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.3
Provides:      io-event = %EVR
Provides:      gem(io-event) = 1.22.0

%description
An event loop.


%if_enabled    doc
%package       -n gem-io-event-doc
Version:       1.22.0
Release:       alt1
Summary:       An event loop documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета io-event
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(io-event) = 1.22.0

%description   -n gem-io-event-doc
An event loop documentation files.

%description   -n gem-io-event-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета io-event.
%endif


%if_enabled    devel
%package       -n gem-io-event-devel
Version:       1.22.0
Release:       alt1
Summary:       An event loop development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета io-event
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(io-event) = 1.22.0

%description   -n gem-io-event-devel
An event loop development package.

%description   -n gem-io-event-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета io-event.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-io-event-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-io-event-devel
%doc license.md readme.md
%ruby_includedir/*
%endif


%changelog
* Sat Sep 12 2026 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt1
- ^ 1.6.5 -> 1.22.0

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.5-alt1
- ^ 1.0.9 -> 1.6.5

* Wed Oct 12 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.9-alt1
- ^ 1.0.5 -> 1.0.9

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- ^ 1.0.2 -> 1.0.5

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
