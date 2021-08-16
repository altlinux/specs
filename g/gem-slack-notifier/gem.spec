%define        gemname slack-notifier

Name:          gem-slack-notifier
Version:       2.4.0
Release:       alt1
Summary:       A slim ruby wrapper for posting to slack webhooks
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/stevenosloan/slack-notifier
Vcs:           https://github.com/stevenosloan/slack-notifier.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(slack-notifier) = 2.4.0


%description
A slim ruby wrapper for posting to slack webhooks


%package       -n gem-slack-notifier-doc
Version:       2.4.0
Release:       alt1
Summary:       A slim ruby wrapper for posting to slack webhooks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета slack-notifier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(slack-notifier) = 2.4.0

%description   -n gem-slack-notifier-doc
A slim ruby wrapper for posting to slack webhooks documentation files.

A slim ruby wrapper for posting to slack webhooks

%description   -n gem-slack-notifier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета slack-notifier.


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

%files         -n gem-slack-notifier-doc
%ruby_gemdocdir


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
