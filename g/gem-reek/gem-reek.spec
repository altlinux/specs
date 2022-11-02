%define        gemname reek

Name:          gem-reek
Version:       6.1.1
Release:       alt1
Summary:       Code smell detector for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/troessner/reek
Vcs:           https://github.com/troessner/reek.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(aruba) >= 2.0 gem(aruba) < 3
BuildRequires: gem(codeclimate-engine-rb) >= 0.4.0 gem(codeclimate-engine-rb) < 0.5
BuildRequires: gem(cucumber) >= 4.0 gem(cucumber) < 8.0
BuildRequires: gem(kramdown) >= 2.1 gem(kramdown) < 3
BuildRequires: gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-benchmark) >= 0.6.0 gem(rspec-benchmark) < 0.7
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-performance) >= 1.11.3 gem(rubocop-performance) < 2
BuildRequires: gem(rubocop-rspec) >= 2.4.0 gem(rubocop-rspec) < 3
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(yard) >= 0.9.5 gem(yard) < 0.10
BuildRequires: gem(redcarpet) >= 3.4 gem(redcarpet) < 4
BuildRequires: gem(pry) >= 0.13.1 gem(pry) < 1
BuildRequires: gem(kwalify) >= 0.7.0 gem(kwalify) < 0.8
BuildRequires: gem(parser) >= 3.1.0 gem(parser) < 3.2
BuildRequires: gem(rainbow) >= 2.0 gem(rainbow) < 4.0
BuildRequires: gem(aruba) >= 2.0 gem(aruba) < 3
BuildRequires: gem(codeclimate-engine-rb) >= 0.4.0 gem(codeclimate-engine-rb) < 0.5
BuildRequires: gem(cucumber) >= 4.0 gem(cucumber) < 8.0
BuildRequires: gem(kramdown) >= 2.1 gem(kramdown) < 3
BuildRequires: gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-benchmark) >= 0.6.0 gem(rspec-benchmark) < 0.7
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-performance) >= 1.11.3 gem(rubocop-performance) < 2
BuildRequires: gem(rubocop-rspec) >= 2.4.0 gem(rubocop-rspec) < 3
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(yard) >= 0.9.5 gem(yard) < 0.10
BuildRequires: gem(redcarpet) >= 3.4 gem(redcarpet) < 4
BuildRequires: gem(pry) >= 0.13.1 gem(pry) < 1
BuildRequires: gem(kwalify) >= 0.7.0 gem(kwalify) < 0.8
BuildRequires: gem(parser) >= 3.1.0 gem(parser) < 3.2
BuildRequires: gem(rainbow) >= 2.0 gem(rainbow) < 4.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      gem(kwalify) >= 0.7.0 gem(kwalify) < 0.8
Requires:      gem(parser) >= 3.1.0 gem(parser) < 3.2
Requires:      gem(rainbow) >= 2.0 gem(rainbow) < 4.0
Provides:      gem(reek) = 6.1.1


%description
Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.


%package       -n reek
Version:       6.1.1
Release:       alt1
Summary:       Code smell detector for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета reek
Group:         Other
BuildArch:     noarch

Requires:      gem(reek) = 6.1.1

%description   -n reek
Code smell detector for Ruby executable(s).

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.

%description   -n reek -l ru_RU.UTF-8
Исполнямка для самоцвета reek.


%package       -n gem-reek-doc
Version:       6.1.1
Release:       alt1
Summary:       Code smell detector for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета reek
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(reek) = 6.1.1

%description   -n gem-reek-doc
Code smell detector for Ruby documentation files.

Reek is a tool that examines Ruby classes, modules and methods and reports any
code smells it finds.

%description   -n gem-reek-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета reek.


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

%files         -n reek
%doc README.md
%_bindir/code_climate_reek
%_bindir/reek

%files         -n gem-reek-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- + packaged gem with Ruby Policy 2.0
