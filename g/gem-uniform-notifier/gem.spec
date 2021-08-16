%define        gemname uniform_notifier

Name:          gem-uniform-notifier
Version:       1.14.2
Release:       alt1
Summary:       uniform notifier for rails logger, customized logger, javascript alert, javascript console, growl and xmpp
License:       MIT
Group:         Development/Ruby
Url:           http://rubygems.org/gems/uniform_notifier
Vcs:           https://github.com/flyerhzm/uniform_notifier.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) > 0
BuildRequires: gem(ruby_gntp) >= 0.3.4 gem(ruby_gntp) < 1
BuildRequires: gem(ruby-growl) >= 4.0 gem(ruby-growl) < 5
BuildRequires: gem(slack-notifier) >= 1.0 gem(slack-notifier) < 3
BuildRequires: gem(xmpp4r) >= 0.5 gem(xmpp4r) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency ruby_gntp >= 0.3.4,ruby_gntp < 1
%ruby_use_gem_dependency ruby-growl >= 4.1,ruby-growl < 5
%ruby_use_gem_dependency slack-notifier >= 2.4.0,slack-notifier < 3
%ruby_use_gem_dependency xmpp4r >= 0.5.6,xmpp4r < 1
Provides:      gem(uniform_notifier) = 1.14.2


%description
uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp


%package       -n gem-uniform-notifier-doc
Version:       1.14.2
Release:       alt1
Summary:       uniform notifier for rails logger, customized logger, javascript alert, javascript console, growl and xmpp documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uniform_notifier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uniform_notifier) = 1.14.2

%description   -n gem-uniform-notifier-doc
uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp documentation files.

uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp

%description   -n gem-uniform-notifier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uniform_notifier.


%package       -n gem-uniform-notifier-devel
Version:       1.14.2
Release:       alt1
Summary:       uniform notifier for rails logger, customized logger, javascript alert, javascript console, growl and xmpp development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uniform_notifier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(uniform_notifier) = 1.14.2
Requires:      gem(rspec) > 0
Requires:      gem(ruby_gntp) >= 0.3.4 gem(ruby_gntp) < 1
Requires:      gem(ruby-growl) >= 4.0 gem(ruby-growl) < 5
Requires:      gem(slack-notifier) >= 1.0 gem(slack-notifier) < 3
Requires:      gem(xmpp4r) >= 0.5 gem(xmpp4r) < 1

%description   -n gem-uniform-notifier-devel
uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp development package.

uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp

%description   -n gem-uniform-notifier-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uniform_notifier.


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

%files         -n gem-uniform-notifier-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-uniform-notifier-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.14.2-alt1
- + packaged gem with Ruby Policy 2.0
