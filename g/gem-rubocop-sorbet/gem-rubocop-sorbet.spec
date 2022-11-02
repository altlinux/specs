%define        gemname rubocop-sorbet

Name:          gem-rubocop-sorbet
Version:       0.6.11
Release:       alt1
Summary:       Automatic Sorbet code style checking tool
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/shopify/rubocop-sorbet
Vcs:           https://github.com/shopify/rubocop-sorbet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.7 gem(rspec) < 4
BuildRequires: gem(unparser) >= 0.6 gem(unparser) < 1
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rubocop-shopify) >= 0
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1
BuildRequires: gem(rubocop) >= 0.90.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 0.90.0
Provides:      gem(rubocop-sorbet) = 0.6.11


%description
Automatic Sorbet code style checking tool.


%package       -n gem-rubocop-sorbet-doc
Version:       0.6.11
Release:       alt1
Summary:       Automatic Sorbet code style checking tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-sorbet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-sorbet) = 0.6.11

%description   -n gem-rubocop-sorbet-doc
Automatic Sorbet code style checking tool documentation files.

%description   -n gem-rubocop-sorbet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-sorbet.


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

%files         -n gem-rubocop-sorbet-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.11-alt1
- + packaged gem with Ruby Policy 2.0
