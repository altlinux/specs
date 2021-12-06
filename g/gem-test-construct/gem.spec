%define        gemname test_construct

Name:          gem-test-construct
Version:       2.0.2
Release:       alt1
Summary:       Creates temporary files and directories for testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bhb/test_construct
Vcs:           https://github.com/bhb/test_construct.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 5.0.8 gem(minitest) < 6
BuildRequires: gem(mocha) >= 0.14.0 gem(mocha) < 2
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(test_construct) = 2.0.2


%description
TestConstruct is a DSL for creating temporary files and directories during
testing.


%package       -n gem-test-construct-doc
Version:       2.0.2
Release:       alt1
Summary:       Creates temporary files and directories for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test_construct
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test_construct) = 2.0.2

%description   -n gem-test-construct-doc
Creates temporary files and directories for testing documentation files.

TestConstruct is a DSL for creating temporary files and directories during
testing.

%description   -n gem-test-construct-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test_construct.


%package       -n gem-test-construct-devel
Version:       2.0.2
Release:       alt1
Summary:       Creates temporary files and directories for testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test_construct
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test_construct) = 2.0.2
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 5.0.8 gem(minitest) < 6
Requires:      gem(mocha) >= 0.14.0 gem(mocha) < 2
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-test-construct-devel
Creates temporary files and directories for testing development package.

TestConstruct is a DSL for creating temporary files and directories during
testing.

%description   -n gem-test-construct-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test_construct.


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

%files         -n gem-test-construct-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-test-construct-devel
%doc README.md


%changelog
* Fri Oct 29 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt1
- + packaged gem with Ruby Policy 2.0
