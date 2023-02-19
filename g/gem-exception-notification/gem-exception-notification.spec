%define        gemname exception_notification

Name:          gem-exception-notification
Version:       4.5.0.2
Release:       alt0.1
Summary:       Exception Notifier Plugin for Rails
License:       MIT
Group:         Development/Ruby
Url:           https://smartinez87.github.io/exception_notification/
Vcs:           https://github.com/smartinez87/exception_notification.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 2.2.0
BuildRequires: gem(aws-sdk-sns) >= 1
BuildRequires: gem(carrier-pigeon) >= 0.7.0
BuildRequires: gem(coveralls) >= 0.8.2
BuildRequires: gem(dogapi) >= 1.23.0
BuildRequires: gem(hipchat) >= 1.0.0
BuildRequires: gem(httparty) >= 0.10.2
BuildRequires: gem(mocha) >= 0.13.0
BuildRequires: gem(mock_redis) >= 0.19.0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(rails) >= 5.2
BuildRequires: gem(resque) >= 1.8.0
BuildRequires: gem(rubocop) >= 0.78.0
BuildRequires: gem(sidekiq) >= 5.0.4
BuildRequires: gem(slack-notifier) >= 1.0.0
BuildRequires: gem(timecop) >= 0.9.0
BuildRequires: gem(actionmailer) >= 5.2
BuildRequires: gem(activesupport) >= 5.2
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(aws-sdk-sns) >= 2
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(httparty) >= 0.11
BuildConflicts: gem(mock_redis) >= 0.20
BuildConflicts: gem(rails) >= 8
BuildConflicts: gem(resque) >= 1.9
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(timecop) >= 0.10
BuildConflicts: gem(actionmailer) >= 8
BuildConflicts: gem(activesupport) >= 8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names exception_notification,exception-notification
Requires:      gem(actionmailer) >= 5.2
Requires:      gem(activesupport) >= 5.2
Conflicts:     gem(actionmailer) >= 8
Conflicts:     gem(activesupport) >= 8
Obsoletes:     rails-plugin-exception_notification
Provides:      rails-plugin-exception_notification
Provides:      gem(exception_notification) = 4.5.0.2

%ruby_use_gem_version exception_notification:4.5.0.2

%description
The Exception Notifier plugin provides a mailer object and a default set of
templates for sending email notifications when errors occur in a Rails
application.


%package       -n gem-exception-notification-doc
Version:       4.5.0.2
Release:       alt0.1
Summary:       Exception Notifier Plugin for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета exception_notification
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(exception_notification) = 4.5.0.2

%description   -n gem-exception-notification-doc
Exception Notifier Plugin for Rails documentation files.

The Exception Notifier plugin provides a mailer object and a default set of
templates for sending email notifications when errors occur in a Rails
application.

%description   -n gem-exception-notification-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета exception_notification.


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


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 4.5.0.2-alt0.1
- ^ 4.5.0 -> 4.5.0p2 (no devel)

* Wed Jul 13 2022 Pavel Skrylev <majioa@altlinux.org> 4.5.0-alt1.1
- !fix deps to net-smtp

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
