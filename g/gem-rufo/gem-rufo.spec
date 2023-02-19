%define        gemname rufo

Name:          gem-rufo
Version:       0.14.0
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
%if_with check
BuildRequires: gem(bundler) >= 1.15
BuildRequires: gem(byebug) >= 11.0.1
BuildRequires: gem(guard-rspec) >= 4.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rexml) >= 3.2.5
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec_junit_formatter) >= 0.4.1
BuildRequires: gem(rubocop) >= 0.79.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 1.3.1
BuildConflicts: gem(byebug) >= 12
BuildConflicts: gem(guard-rspec) >= 5
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rexml) >= 3.3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec_junit_formatter) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-cobertura) >= 1.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency byebug >= 11.1.3,byebug < 12
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec_junit_formatter >= 0.5.1,rspec_junit_formatter < 1
Provides:      gem(rufo) = 0.14.0


%description
Fast and unobtrusive Ruby code formatter


%package       -n rufo
Version:       0.14.0
Release:       alt1
Summary:       Ruby code formatter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rufo
Group:         Other
BuildArch:     noarch

Requires:      gem(rufo) = 0.14.0

%description   -n rufo
Ruby code formatter executable(s).

Fast and unobtrusive Ruby code formatter

%description   -n rufo -l ru_RU.UTF-8
Исполнямка для самоцвета rufo.


%package       -n gem-rufo-doc
Version:       0.14.0
Release:       alt1
Summary:       Ruby code formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rufo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rufo) = 0.14.0

%description   -n gem-rufo-doc
Ruby code formatter documentation files.

Fast and unobtrusive Ruby code formatter

%description   -n gem-rufo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rufo.


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


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- ^ 0.13.0 -> 0.14.0 (no devel)

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- + packaged gem with Ruby Policy 2.0
