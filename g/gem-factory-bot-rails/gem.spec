%define        gemname factory_bot_rails

Name:          gem-factory-bot-rails
Version:       6.2.0
Release:       alt1
Summary:       factory_bot_rails provides integration between factory_bot and rails 5.0 or newer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thoughtbot/factory_bot_rails
Vcs:           https://github.com/thoughtbot/factory_bot_rails.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(factory_bot) >= 6.2.0 gem(factory_bot) < 6.3
BuildRequires: gem(railties) >= 5.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(factory_bot) >= 6.2.0 gem(factory_bot) < 6.3
Requires:      gem(railties) >= 5.0.0
Provides:      gem(factory_bot_rails) = 6.2.0


%description
factory_bot_rails provides integration between factory_bot and rails 5.0 or
newer.


%package       -n gem-factory-bot-rails-doc
Version:       6.2.0
Release:       alt1
Summary:       factory_bot_rails provides integration between factory_bot and rails 5.0 or newer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета factory_bot_rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(factory_bot_rails) = 6.2.0

%description   -n gem-factory-bot-rails-doc
factory_bot_rails provides integration between factory_bot and rails 5.0 or
newer documentation files.

%description   -n gem-factory-bot-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета factory_bot_rails.


%package       -n gem-factory-bot-rails-devel
Version:       6.2.0
Release:       alt1
Summary:       factory_bot_rails provides integration between factory_bot and rails 5.0 or newer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета factory_bot_rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(factory_bot_rails) = 6.2.0

%description   -n gem-factory-bot-rails-devel
factory_bot_rails provides integration between factory_bot and rails 5.0 or
newer development package.

%description   -n gem-factory-bot-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета factory_bot_rails.


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

%files         -n gem-factory-bot-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-factory-bot-rails-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 6.2.0-alt1
- + packaged gem with Ruby Policy 2.0
