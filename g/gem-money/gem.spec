%define        gemname money

Name:          gem-money
Version:       6.16.0
Release:       alt1
Summary:       A Ruby Library for dealing with money and currency conversion
License:       MIT
Group:         Development/Ruby
Url:           https://rubymoney.github.io/money
Vcs:           https://github.com/rubymoney/money/.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(i18n) >= 0.6.4 gem(i18n) <= 2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.9.11 gem(yard) < 0.10
BuildRequires: gem(kramdown) >= 2.3 gem(kramdown) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(i18n) >= 0.6.4 gem(i18n) <= 2
Provides:      gem(money) = 6.16.0


%description
A Ruby Library for dealing with money and currency conversion.


%package       -n gem-money-doc
Version:       6.16.0
Release:       alt1
Summary:       A Ruby Library for dealing with money and currency conversion documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета money
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(money) = 6.16.0

%description   -n gem-money-doc
A Ruby Library for dealing with money and currency conversion documentation
files.

%description   -n gem-money-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета money.


%package       -n gem-money-devel
Version:       6.16.0
Release:       alt1
Summary:       A Ruby Library for dealing with money and currency conversion development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета money
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(money) = 6.16.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4
Requires:      gem(yard) >= 0.9.11 gem(yard) < 0.10
Requires:      gem(kramdown) >= 2.3 gem(kramdown) < 3

%description   -n gem-money-devel
A Ruby Library for dealing with money and currency conversion development
package.

%description   -n gem-money-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета money.


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

%files         -n gem-money-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-money-devel
%doc README.md


%changelog
* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 6.16.0-alt1
- + packaged gem with Ruby Policy 2.0
