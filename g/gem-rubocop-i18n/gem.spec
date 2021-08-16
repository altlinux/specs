%define        gemname rubocop-i18n

Name:          gem-rubocop-i18n
Version:       3.0.0
Release:       alt1
Summary:       RuboCop rules for i18n
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/rubocop-i18n
Vcs:           https://github.com/puppetlabs/rubocop-i18n.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.17.3 gem(bundler) < 3
BuildRequires: gem(pry) >= 0.13.1 gem(pry) < 1
BuildRequires: gem(rake) >= 12.3.3 gem(rake) < 14
BuildRequires: gem(rb-readline) >= 0.5.5 gem(rb-readline) < 0.6
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rubocop) >= 1.0 gem(rubocop) < 2
Provides:      gem(rubocop-i18n) = 3.0.0


%description
RuboCop rules for detecting and autocorrecting undecorated strings for i18n
(gettext and rails-i18n)


%package       -n gem-rubocop-i18n-doc
Version:       3.0.0
Release:       alt1
Summary:       RuboCop rules for i18n documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-i18n
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-i18n) = 3.0.0

%description   -n gem-rubocop-i18n-doc
RuboCop rules for i18n documentation files.

RuboCop rules for detecting and autocorrecting undecorated strings for i18n
(gettext and rails-i18n)

%description   -n gem-rubocop-i18n-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-i18n.


%package       -n gem-rubocop-i18n-devel
Version:       3.0.0
Release:       alt1
Summary:       RuboCop rules for i18n development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-i18n
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-i18n) = 3.0.0
Requires:      gem(bundler) >= 1.17.3 gem(bundler) < 3
Requires:      gem(pry) >= 0.13.1 gem(pry) < 1
Requires:      gem(rake) >= 12.3.3 gem(rake) < 14
Requires:      gem(rb-readline) >= 0.5.5 gem(rb-readline) < 0.6
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-rubocop-i18n-devel
RuboCop rules for i18n development package.

RuboCop rules for detecting and autocorrecting undecorated strings for i18n
(gettext and rails-i18n)

%description   -n gem-rubocop-i18n-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-i18n.


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

%files         -n gem-rubocop-i18n-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-i18n-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- + packaged gem with Ruby Policy 2.0
