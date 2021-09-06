%define        gemname event

Name:          gem-event
Version:       1.0.2
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
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(event) = 1.0.2

%description
An event loop.


%package       -n gem-event-doc
Version:       1.0.2
Release:       alt1
Summary:       An event loop documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета event
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(event) = 1.0.2

%description   -n gem-event-doc
An event loop documentation files.

%description   -n gem-event-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета event.


%package       -n gem-event-devel
Version:       1.0.2
Release:       alt1
Summary:       An event loop development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета event
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(event) = 1.0.2
Requires:      gem(bake) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-event-devel
An event loop development package.

%description   -n gem-event-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета event.


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

%files         -n gem-event-doc
%ruby_gemdocdir

%files         -n gem-event-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
