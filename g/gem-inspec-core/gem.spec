%define        gemname inspec-core

Name:          gem-inspec-core
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/inspec
Vcs:           https://github.com/inspec/inspec.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(chef-telemetry) >= 1.0.8 gem(chef-telemetry) < 2
# BuildRequires: gem(license-acceptance) >= 0.2.13 gem(license-acceptance) < 3.0
BuildRequires: gem(thor) >= 0.20 gem(thor) < 2.0
BuildRequires: gem(method_source) >= 0.8 gem(method_source) < 2.0
BuildRequires: gem(rubyzip) >= 1.2.2 gem(rubyzip) < 3.0
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(rspec-its) >= 1.2 gem(rspec-its) < 2
BuildRequires: gem(pry) >= 0.13 gem(pry) < 1
BuildRequires: gem(hashie) >= 3.4 gem(hashie) < 5.0
BuildRequires: gem(mixlib-log) >= 3.0 gem(mixlib-log) < 4
BuildRequires: gem(sslshake) >= 1.2 gem(sslshake) < 2
BuildRequires: gem(parallel) >= 1.9 gem(parallel) < 2
BuildRequires: gem(faraday) >= 0.9.0 gem(faraday) < 1.5
BuildRequires: gem(faraday_middleware) >= 1.0 gem(faraday_middleware) < 2
BuildRequires: gem(tty-table) >= 0.10 gem(tty-table) < 1
BuildRequires: gem(tty-prompt) >= 0.17 gem(tty-prompt) < 1
# BuildRequires: gem(tomlrb) >= 1.2 gem(tomlrb) < 3
BuildRequires: gem(addressable) >= 2.4 gem(addressable) < 3
BuildRequires: gem(parslet) >= 1.5 gem(parslet) < 3
BuildRequires: gem(semverse) >= 3.0 gem(semverse) < 4
BuildRequires: gem(multipart-post) >= 2.0 gem(multipart-post) < 3
BuildRequires: gem(train-core) >= 3.0 gem(train-core) < 4
BuildRequires: gem(train) >= 3.0 gem(train) < 4
BuildRequires: gem(faraday_middleware) >= 0.12.2 gem(faraday_middleware) < 1.1
BuildRequires: gem(train-habitat) >= 0.1 gem(train-habitat) < 1
BuildRequires: gem(train-aws) >= 0.1 gem(train-aws) < 1
BuildRequires: gem(train-winrm) >= 0.2 gem(train-winrm) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency parslet >= 1.5,parslet < 3
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_ignore_names rake-tests,omnibus,kitchen-puppet,kitchen-chef,kitchen-ansible,inspec-plugin-template,inspec-resource-lister,ordinal_array,train-test-fixture,inspec-test-fixture
Requires:      gem(chef-telemetry) >= 1.0.8 gem(chef-telemetry) < 2
Requires:      gem(license-acceptance) >= 0.2.13 gem(license-acceptance) < 3.0
Requires:      gem(thor) >= 0.20 gem(thor) < 2.0
Requires:      gem(method_source) >= 0.8 gem(method_source) < 2.0
Requires:      gem(rubyzip) >= 1.2.2 gem(rubyzip) < 3.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(rspec-its) >= 1.2 gem(rspec-its) < 2
Requires:      gem(pry) >= 0.13 gem(pry) < 1
Requires:      gem(hashie) >= 3.4 gem(hashie) < 5.0
Requires:      gem(mixlib-log) >= 3.0 gem(mixlib-log) < 4
Requires:      gem(sslshake) >= 1.2 gem(sslshake) < 2
Requires:      gem(parallel) >= 1.9 gem(parallel) < 2
Requires:      gem(faraday) >= 0.9.0 gem(faraday) < 1.5
Requires:      gem(faraday_middleware) >= 1.0 gem(faraday_middleware) < 2
Requires:      gem(tty-table) >= 0.10 gem(tty-table) < 1
Requires:      gem(tty-prompt) >= 0.17 gem(tty-prompt) < 1
Requires:      gem(tomlrb) >= 1.2 gem(tomlrb) < 3
Requires:      gem(addressable) >= 2.4 gem(addressable) < 3
Requires:      gem(parslet) >= 1.5 gem(parslet) < 3
Requires:      gem(semverse) >= 3.0 gem(semverse) < 4
Requires:      gem(multipart-post) >= 2.0 gem(multipart-post) < 3
Requires:      gem(train-core) >= 3.0 gem(train-core) < 4
Provides:      gem(inspec-core) = 4.38.6


%description
InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification. This has local support only. See the `inspec` gem for
full support.


%package       -n gem-inspec-bin
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec) = 4.38.6
Provides:      gem(inspec-bin) = 4.38.6

%description   -n gem-inspec-bin
InSpec executable for inspec gem. Use of this executable may require accepting a
license agreement.


%package       -n gem-inspec-bin-doc
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-bin) = 4.38.6

%description   -n gem-inspec-bin-doc
Infrastructure and compliance testing documentation files.

InSpec executable for inspec gem. Use of this executable may require accepting a
license agreement.

%description   -n gem-inspec-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec-bin.


%package       -n gem-inspec-bin-devel
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-bin) = 4.38.6
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-inspec-bin-devel
Infrastructure and compliance testing development package.

InSpec executable for inspec gem. Use of this executable may require accepting a
license agreement.

%description   -n gem-inspec-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec-bin.


%package       -n gem-inspec-core-bin
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) = 4.38.6
Provides:      gem(inspec-core-bin) = 4.38.6

%description   -n gem-inspec-core-bin
InSpec executable for inspec-core gem. Use of this executable may require
accepting a license agreement.


%package       -n inspec
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета inspec-core-bin
Group:         Other
BuildArch:     noarch

Requires:      gem(inspec-core-bin) = 4.38.6

%description   -n inspec
Infrastructure and compliance testing executable(s).

InSpec executable for inspec-core gem. Use of this executable may require
accepting a license agreement.

%description   -n inspec -l ru_RU.UTF-8
Исполнямка для самоцвета inspec-core-bin.


%package       -n gem-inspec-core-bin-doc
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-core-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-core-bin) = 4.38.6

%description   -n gem-inspec-core-bin-doc
Infrastructure and compliance testing documentation files.

InSpec executable for inspec-core gem. Use of this executable may require
accepting a license agreement.

%description   -n gem-inspec-core-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec-core-bin.


%package       -n gem-inspec-core-bin-devel
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-core-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core-bin) = 4.38.6
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-inspec-core-bin-devel
Infrastructure and compliance testing development package.

InSpec executable for inspec-core gem. Use of this executable may require
accepting a license agreement.

%description   -n gem-inspec-core-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec-core-bin.


%package       -n gem-inspec
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) = 4.38.6
Requires:      gem(train) >= 3.0 gem(train) < 4
Requires:      gem(faraday_middleware) >= 0.12.2 gem(faraday_middleware) < 1.1
Requires:      gem(train-habitat) >= 0.1 gem(train-habitat) < 1
Requires:      gem(train-aws) >= 0.1 gem(train-aws) < 1
Requires:      gem(train-winrm) >= 0.2 gem(train-winrm) < 1
Provides:      gem(inspec) = 4.38.6

%description   -n gem-inspec
InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification.


%package       -n gem-inspec-doc
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec) = 4.38.6

%description   -n gem-inspec-doc
Infrastructure and compliance testing documentation files.

InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification.

%description   -n gem-inspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec.


%package       -n gem-inspec-devel
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec) = 4.38.6

%description   -n gem-inspec-devel
Infrastructure and compliance testing development package.

InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification.

%description   -n gem-inspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec.


%package       -n gem-inspec-core-doc
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-core) = 4.38.6

%description   -n gem-inspec-core-doc
Infrastructure and compliance testing. Core library documentation files.

InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification. This has local support only. See the `inspec` gem for
full support.

%description   -n gem-inspec-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec-core.


%package       -n gem-inspec-core-devel
Version:       4.38.6
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) = 4.38.6

%description   -n gem-inspec-core-devel
Infrastructure and compliance testing. Core library development package.

InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification. This has local support only. See the `inspec` gem for
full support.

%description   -n gem-inspec-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec-core.


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

%files         -n gem-inspec-bin
%doc README.md
%ruby_gemspecdir/inspec-bin-4.38.6.gemspec
%ruby_gemslibdir/inspec-bin-4.38.6

%files         -n gem-inspec-bin-doc
%doc README.md
%ruby_gemsdocdir/inspec-bin-4.38.6

%files         -n gem-inspec-bin-devel
%doc README.md

%files         -n gem-inspec-core-bin
%doc README.md
%ruby_gemspecdir/inspec-core-bin-4.38.6.gemspec
%ruby_gemslibdir/inspec-core-bin-4.38.6

%files         -n inspec
%doc README.md
%_bindir/inspec

%files         -n gem-inspec-core-bin-doc
%doc README.md
%ruby_gemsdocdir/inspec-core-bin-4.38.6

%files         -n gem-inspec-core-bin-devel
%doc README.md

%files         -n gem-inspec
%doc README.md
%ruby_gemspecdir/inspec-4.38.6.gemspec
%ruby_gemslibdir/inspec-4.38.6

%files         -n gem-inspec-doc
%doc README.md
%ruby_gemsdocdir/inspec-4.38.6

%files         -n gem-inspec-devel
%doc README.md

%files         -n gem-inspec-core-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-inspec-core-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 4.38.6-alt1
- + packaged gem with Ruby Policy 2.0
