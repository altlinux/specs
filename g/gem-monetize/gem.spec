%define        gemname monetize

Name:          gem-monetize
Version:       1.12.0
Release:       alt1
Summary:       A library for converting various objects into `Money` objects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/RubyMoney/monetize
Vcs:           https://github.com/rubymoney/monetize/.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(money) >= 6.12 gem(money) < 7
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 10.2 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(money) >= 6.12 gem(money) < 7
Provides:      gem(monetize) = 1.12.0


%description
A library for converting various objects into `Money` objects.


%package       -n gem-monetize-doc
Version:       1.12.0
Release:       alt1
Summary:       A library for converting various objects into `Money` objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета monetize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(monetize) = 1.12.0

%description   -n gem-monetize-doc
A library for converting various objects into `Money` objects documentation
files.

%description   -n gem-monetize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета monetize.


%package       -n gem-monetize-devel
Version:       1.12.0
Release:       alt1
Summary:       A library for converting various objects into `Money` objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета monetize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(monetize) = 1.12.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 10.2 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-monetize-devel
A library for converting various objects into `Money` objects development
package.

%description   -n gem-monetize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета monetize.


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

%files         -n gem-monetize-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-monetize-devel
%doc README.md


%changelog
* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 1.12.0-alt1
- + packaged gem with Ruby Policy 2.0
