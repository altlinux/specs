%define        gemname factory_bot

Name:          gem-factory-bot
Version:       6.2.0
Release:       alt1
Summary:       factory_bot provides a framework and DSL for defining and using model instance factories
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thoughtbot/factory_bot
Vcs:           https://github.com/thoughtbot/factory_bot.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 5.0.0
BuildRequires: gem(activerecord) >= 0
BuildRequires: gem(appraisal) >= 0
# BuildRequires: gem(aruba) >= 0
# BuildRequires: gem(cucumber) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rspec) >= 0
# BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(simplecov) >= 0 gem(simplecov) < 1
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(activesupport) >= 5.0.0
Provides:      gem(factory_bot) = 6.2.0


%description
factory_bot provides a framework and DSL for defining and using factories - less
error-prone, more explicit, and all-around easier to work with than fixtures.


%package       -n gem-factory-bot-doc
Version:       6.2.0
Release:       alt1
Summary:       factory_bot provides a framework and DSL for defining and using model instance factories documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета factory_bot
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(factory_bot) = 6.2.0

%description   -n gem-factory-bot-doc
factory_bot provides a framework and DSL for defining and using model instance
factories documentation files.

factory_bot provides a framework and DSL for defining and using factories - less
error-prone, more explicit, and all-around easier to work with than fixtures.

%description   -n gem-factory-bot-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета factory_bot.


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

%files         -n gem-factory-bot-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 6.2.0-alt1
- + packaged gem with Ruby Policy 2.0
