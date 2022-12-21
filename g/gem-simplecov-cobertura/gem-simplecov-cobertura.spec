%define        gemname simplecov-cobertura

Name:          gem-simplecov-cobertura
Version:       2.1.0
Release:       alt1
Summary:       SimpleCov Cobertura Formatter
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/dashingrocket/simplecov-cobertura
Vcs:           https://github.com/dashingrocket/simplecov-cobertura.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(test-unit) >= 3.2 gem(test-unit) < 4
BuildRequires: gem(nokogiri) >= 1.0 gem(nokogiri) < 2
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(rexml) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(rexml) >= 0
Provides:      gem(simplecov-cobertura) = 2.1.0


%description
Produces Cobertura XML formatted output from SimpleCov.


%package       -n gem-simplecov-cobertura-doc
Version:       2.1.0
Release:       alt1
Summary:       SimpleCov Cobertura Formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov-cobertura
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov-cobertura) = 2.1.0

%description   -n gem-simplecov-cobertura-doc
SimpleCov Cobertura Formatter documentation files.

Produces Cobertura XML formatted output from SimpleCov.

%description   -n gem-simplecov-cobertura-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov-cobertura.


%package       -n gem-simplecov-cobertura-devel
Version:       2.1.0
Release:       alt1
Summary:       SimpleCov Cobertura Formatter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simplecov-cobertura
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(simplecov-cobertura) = 2.1.0
Requires:      gem(test-unit) >= 3.2 gem(test-unit) < 4
Requires:      gem(nokogiri) >= 1.0 gem(nokogiri) < 2
Requires:      gem(rake) >= 13.0 gem(rake) < 14

%description   -n gem-simplecov-cobertura-devel
SimpleCov Cobertura Formatter development package.

Produces Cobertura XML formatted output from SimpleCov.

%description   -n gem-simplecov-cobertura-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simplecov-cobertura.


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

%files         -n gem-simplecov-cobertura-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-simplecov-cobertura-devel
%doc README.md


%changelog
* Tue Dec 20 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
