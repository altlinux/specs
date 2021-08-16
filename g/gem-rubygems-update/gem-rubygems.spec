%define        gemname rubygems-update

Name:          gem-rubygems-update
Version:       3.2.19
Release:       alt1
Summary:       Library packaging and distribution for Ruby
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://rubygems.org/
Vcs:           https://github.com/rubygems/rubygems.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names warbler,templates,rubyforge,bar,demo,rubygems-update[doc]
Requires:      /usr/bin/gem
Obsoletes:     ruby-rubygems-update < %EVR
Provides:      ruby-rubygems-update = %EVR
Provides:      gem(rubygems-update) = 3.2.19


%description
RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and load
these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers. See
our guide on publishing a Gem at guides.rubygems.org


%package       -n gem-bundler
Version:       2.2.19
Release:       alt1
Summary:       The best way to manage your application's dependencies
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(bundler) = 2.2.19

%description   -n gem-bundler
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably


%package       -n bundle
Version:       2.2.19
Release:       alt1
Summary:       The best way to manage your application's dependencies executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bundler
Group:         Other
BuildArch:     noarch

Requires:      gem(bundler) >= 2.1.4 gem(bundler) < 3

%description   -n bundle
The best way to manage your application's dependencies executable(s).

Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%description   -n bundle -l ru_RU.UTF-8
Исполнямка для самоцвета bundler.


%package       -n gem-bundler-doc
Version:       2.2.19
Release:       alt1
Summary:       The best way to manage your application's dependencies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bundler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bundler) >= 2.1.4 gem(bundler) < 3

%description   -n gem-bundler-doc
The best way to manage your application's dependencies documentation
files.

Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%description   -n gem-bundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bundler.


%package       -n update-rubygems
Version:       3.2.19
Release:       alt1
Summary:       Library packaging and distribution for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubygems-update
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubygems-update) = 3.2.19

%description   -n update-rubygems
Library packaging and distribution for Ruby executable(s).

RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and load
these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers. See
our guide on publishing a Gem at guides.rubygems.org

%description   -n update-rubygems -l ru_RU.UTF-8
Исполнямка для самоцвета rubygems-update.


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

%files         -n gem-bundler
%doc bundler/README.md
%ruby_gemspecdir/bundler-2.2.19.gemspec
%ruby_gemslibdir/bundler-2.2.19

%files         -n bundle
%doc README.md
%_bindir/bundle
%_bindir/bundler

%files         -n gem-bundler-doc
%doc bundler/README.md
%ruby_gemsdocdir/bundler-2.2.19

%files         -n update-rubygems
%doc README.md
%_bindir/update_rubygems


%changelog
* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.19-alt1
- ^ 3.0.4 -> 3.2.19
- ! CVE-2020-36327, CVE-2021-24105

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.4-alt1
- Bump to 3.0.4
- Fix spec to conform setup.rb

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.3-alt1
- Bump to 3.0.3
- Use Ruby Policy 2.0

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus, packaged as a gem
