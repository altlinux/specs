%define        gemname io-event

Name:          gem-io-event
Version:       1.0.5
Release:       alt1
Summary:       An event loop
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/event
Vcs:           https://github.com/socketry/event.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(sus) >= 0.6 gem(sus) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names bench
Provides:      gem(io-event) = 1.0.5


%description
An event loop.


%package       -n gem-io-event-doc
Version:       1.0.5
Release:       alt1
Summary:       An event loop documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета io-event
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(io-event) = 1.0.5

%description   -n gem-io-event-doc
An event loop documentation files.

%description   -n gem-io-event-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета io-event.


%package       -n gem-io-event-devel
Version:       1.0.5
Release:       alt1
Summary:       An event loop development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета io-event
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(io-event) = 1.0.5
Requires:      gem(bake) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(sus) >= 0.6 gem(sus) < 1

%description   -n gem-io-event-devel
An event loop development package.

%description   -n gem-io-event-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета io-event.


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
%ruby_gemextdir

%files         -n gem-io-event-doc
%ruby_gemdocdir

%files         -n gem-io-event-devel
%ruby_includedir/*


%changelog
* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- ^ 1.0.2 -> 1.0.5

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
