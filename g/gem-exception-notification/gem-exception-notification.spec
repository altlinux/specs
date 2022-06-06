%define        gemname exception_notification

Name:          gem-exception-notification
Version:       4.5.0
Release:       alt1
Summary:       Exception Notifier Plugin for Rails
License:       MIT
Group:         Development/Ruby
Url:           https://smartinez87.github.io/exception_notification/
Vcs:           https://github.com/smartinez87/exception_notification.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(actionmailer) >= 5.2 gem(actionmailer) < 8
BuildRequires: gem(activesupport) >= 5.2 gem(activesupport) < 8
BuildRequires: gem(appraisal) >= 2.2.0 gem(appraisal) < 3
BuildRequires: gem(aws-sdk-sns) >= 1 gem(aws-sdk-sns) < 2
# BuildRequires: gem(carrier-pigeon) >= 0.7.0
BuildRequires: gem(coveralls) >= 0.8.2 gem(coveralls) < 0.9
# BuildRequires: gem(dogapi) >= 1.23.0
# BuildRequires: gem(hipchat) >= 1.0.0
# BuildRequires: gem(httparty) >= 0.10.2 gem(httparty) < 0.11
BuildRequires: gem(mocha) >= 0.13.0
# BuildRequires: gem(mock_redis) >= 0.19.0 gem(mock_redis) < 0.20
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(rails) >= 5.2 gem(rails) < 8
BuildRequires: gem(resque) >= 1.8.0 gem(resque) < 3
BuildRequires: gem(rubocop) >= 0.78.0 gem(rubocop) < 2
BuildRequires: gem(sidekiq) >= 5.0.4
BuildRequires: gem(slack-notifier) >= 1.0.0
BuildRequires: gem(timecop) >= 0.9.0 gem(timecop) < 0.10

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency resque >= 2.1.0,resque < 3
%ruby_alias_names exception_notification,exception-notification
Requires:      gem(actionmailer) >= 5.2 gem(actionmailer) < 8
Requires:      gem(activesupport) >= 5.2 gem(activesupport) < 8
Obsoletes:     rails-plugin-exception_notification
Provides:      rails-plugin-exception_notification
Provides:      gem(exception_notification) = 4.5.0


%description
The Exception Notifier plugin provides a mailer object and a default set of
templates for sending email notifications when errors occur in a Rails
application.


%package       -n gem-exception-notification-doc
Version:       4.5.0
Release:       alt1
Summary:       Exception Notifier Plugin for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета exception_notification
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(exception_notification) = 4.5.0

%description   -n gem-exception-notification-doc
Exception Notifier Plugin for Rails documentation files.

The Exception Notifier plugin provides a mailer object and a default set of
templates for sending email notifications when errors occur in a Rails
application.

%description   -n gem-exception-notification-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета exception_notification.


%package       -n gem-exception-notification-devel
Version:       4.5.0
Release:       alt1
Summary:       Exception Notifier Plugin for Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета exception_notification
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(exception_notification) = 4.5.0
Requires:      gem(appraisal) >= 2.2.0 gem(appraisal) < 3
Requires:      gem(aws-sdk-sns) >= 1 gem(aws-sdk-sns) < 2
# Requires:      gem(carrier-pigeon) >= 0.7.0
Requires:      gem(coveralls) >= 0.8.2 gem(coveralls) < 0.9
# Requires:      gem(dogapi) >= 1.23.0
# Requires:      gem(hipchat) >= 1.0.0
# Requires:      gem(httparty) >= 0.10.2 gem(httparty) < 0.11
Requires:      gem(mocha) >= 0.13.0
# Requires:      gem(mock_redis) >= 0.19.0 gem(mock_redis) < 0.20
Requires:      gem(net-smtp) >= 0
Requires:      gem(rails) >= 5.2 gem(rails) < 8
Requires:      gem(resque) >= 1.8.0 gem(resque) < 3
Requires:      gem(rubocop) >= 0.78.0 gem(rubocop) < 2
Requires:      gem(sidekiq) >= 5.0.4
Requires:      gem(slack-notifier) >= 1.0.0
Requires:      gem(timecop) >= 0.9.0 gem(timecop) < 0.10

%description   -n gem-exception-notification-devel
Exception Notifier Plugin for Rails development package.

The Exception Notifier plugin provides a mailer object and a default set of
templates for sending email notifications when errors occur in a Rails
application.

%description   -n gem-exception-notification-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета exception_notification.


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

%files         -n gem-exception-notification-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-exception-notification-devel
%doc README.md


%changelog
* Wed Apr 20 2022 Pavel Skrylev <majioa@altlinux.org> 4.5.0-alt1
- ^ 4.4.0 -> 4.5.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 4.4.0-alt1.1
- fixed (!) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 4.4.0-alt1
- updated (^) 4.3.0 -> 4.4.0
- fixed (!) spec according to changelog rules, plus some others

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 0.git.16.ge8b603e -> 4.3.0

* Sat Oct 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.git.16.ge8b603e-alt1
- Built for Sisyphus
