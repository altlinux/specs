%define        gemname timers

Name:          gem-timers
Version:       4.3.3
Release:       alt1
Summary:       Pure Ruby one-shot and periodic timers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/timers
Vcs:           https://github.com/socketry/timers.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(timers) = 4.3.3

%description
Collections of one-shot and periodic timers, intended for use with event loops
such as async.


%package       -n gem-timers-doc
Version:       4.3.3
Release:       alt1
Summary:       Pure Ruby one-shot and periodic timers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета timers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(timers) = 4.3.3

%description   -n gem-timers-doc
Pure Ruby one-shot and periodic timers documentation files.

%description   -n gem-timers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета timers.


%package       -n gem-timers-devel
Version:       4.3.3
Release:       alt1
Summary:       Pure Ruby one-shot and periodic timers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета timers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(timers) = 4.3.3
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-timers-devel
Pure Ruby one-shot and periodic timers development package.

%description   -n gem-timers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета timers.


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

%files         -n gem-timers-doc
%ruby_gemdocdir

%files         -n gem-timers-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 4.3.3-alt1
- + packaged gem with Ruby Policy 2.0
