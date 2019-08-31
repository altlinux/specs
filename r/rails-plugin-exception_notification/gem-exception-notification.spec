# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname exception-notification
%define        gemname exception_notification

Name:          rails-plugin-%gemname
Version:       4.3.0
Release:       alt1
Summary:       Exception Notifier Plugin for Rails
License:       MIT
Group:         Development/Ruby
Url:           https://smartinez87.github.io/exception_notification/
%vcs           https://github.com/smartinez87/exception_notification.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rails)
BuildRequires: gem(resque)

%description
The Exception Notifier plugin provides a mailer object and a default
set of templates for sending email notifications when errors occur
in a Rails application.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=sinatra --use=%gemname --alias=%name --join=lib:bin

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir


%changelog
* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt1
! gemified
^ v4.3.0
^ Ruby Policy 2.0

* Sat Oct 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.git.16.ge8b603e-alt1
- Built for Sisyphus
