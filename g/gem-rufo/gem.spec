%define        gemname rufo

Name:          gem-rufo
Version:       0.13.0
Release:       alt1
Summary:       Ruby code formatter
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-formatter/rufo
Vcs:           https://github.com/ruby-formatter/rufo.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.15 gem(bundler) < 3
BuildRequires: gem(byebug) >= 11.0.1 gem(byebug) < 12
# BuildRequires: gem(guard-rspec) >= 4.0 gem(guard-rspec) < 5
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rexml) >= 3.2.5 gem(rexml) < 3.3
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
# BuildRequires: gem(rspec_junit_formatter) >= 0.4.1 gem(rspec_junit_formatter) < 0.5
BuildRequires: gem(rubocop) >= 0.79.0 gem(rubocop) < 2
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
# BuildRequires: gem(simplecov-cobertura) >= 1.3.1 gem(simplecov-cobertura) < 1.4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency byebug >= 11.1.3,byebug < 12
%ruby_ignore_names only_gemfiles
Provides:      gem(rufo) = 0.13.0


%description
Fast and unobtrusive Ruby code formatter


%package       -n rufo
Version:       0.13.0
Release:       alt1
Summary:       Ruby code formatter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rufo
Group:         Other
BuildArch:     noarch

Requires:      gem(rufo) = 0.13.0

%description   -n rufo
Ruby code formatter executable(s).

Fast and unobtrusive Ruby code formatter

%description   -n rufo -l ru_RU.UTF-8
Исполнямка для самоцвета rufo.


%package       -n gem-rufo-doc
Version:       0.13.0
Release:       alt1
Summary:       Ruby code formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rufo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rufo) = 0.13.0

%description   -n gem-rufo-doc
Ruby code formatter documentation files.

Fast and unobtrusive Ruby code formatter

%description   -n gem-rufo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rufo.


%package       -n gem-rufo-devel
Version:       0.13.0
Release:       alt1
Summary:       Ruby code formatter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rufo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rufo) = 0.13.0
Requires:      gem(bundler) >= 1.15 gem(bundler) < 3
Requires:      gem(byebug) >= 11.0.1 gem(byebug) < 12
# Requires:      gem(guard-rspec) >= 4.0 gem(guard-rspec) < 5
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rexml) >= 3.2.5 gem(rexml) < 3.3
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
# Requires:      gem(rspec_junit_formatter) >= 0.4.1 gem(rspec_junit_formatter) < 0.5
Requires:      gem(rubocop) >= 0.79.0 gem(rubocop) < 2
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
# Requires:      gem(simplecov-cobertura) >= 1.3.1 gem(simplecov-cobertura) < 1.4

%description   -n gem-rufo-devel
Ruby code formatter development package.

Fast and unobtrusive Ruby code formatter

%description   -n gem-rufo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rufo.


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

%files         -n rufo
%doc README.md
%_bindir/rufo

%files         -n gem-rufo-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rufo-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- + packaged gem with Ruby Policy 2.0
