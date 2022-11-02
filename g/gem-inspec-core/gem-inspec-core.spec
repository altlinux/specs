%define        gemname inspec-core

Name:          gem-inspec-core
Version:       6.2.9
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
%if_with check
BuildRequires: gem(ffi) >= 1.9.14 gem(ffi) > 1.14.2
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(appbundler) >= 0
BuildRequires: gem(ed25519) >= 0
BuildRequires: gem(bcrypt_pbkdf) >= 0
BuildRequires: gem(chefstyle) >= 2.0.3 gem(chefstyle) < 3
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
BuildRequires: gem(html-proofer) >= 3.19.4 gem(html-proofer) < 6
BuildRequires: gem(json_schemer) >= 0.2.1 gem(json_schemer) < 1
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest-sprint) >= 1.0 gem(minitest-sprint) < 2
BuildRequires: gem(minitest) >= 5.15.0 gem(minitest) < 6
BuildRequires: gem(mocha) >= 1.1 gem(mocha) < 2
BuildRequires: gem(nokogiri) >= 1.9 gem(nokogiri) < 2
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry) >= 0.10 gem(pry) < 1
BuildRequires: gem(rake) >= 10
BuildRequires: gem(ruby-progressbar) >= 1.8 gem(ruby-progressbar) < 2
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(simplecov_json_formatter) >= 0
BuildRequires: gem(webmock) >= 3.0 gem(webmock) < 4
BuildRequires: gem(inquirer) >= 0
BuildRequires: gem(berkshelf) >= 0
BuildRequires: gem(chef) >= 16.0
BuildRequires: gem(test-kitchen) >= 2.8
BuildRequires: gem(kitchen-inspec) >= 2.0
BuildRequires: gem(kitchen-dokken) >= 2.11
BuildRequires: gem(git) >= 0
BuildRequires: gem(chef-telemetry) >= 1.0.8 gem(chef-telemetry) < 2
BuildRequires: gem(license-acceptance) >= 0.2.13 gem(license-acceptance) < 3.0
BuildRequires: gem(thor) >= 0.20 gem(thor) < 2.0
BuildRequires: gem(method_source) >= 0.8 gem(method_source) < 2.0
BuildRequires: gem(rubyzip) >= 1.2.2 gem(rubyzip) < 3.0
BuildRequires: gem(rspec) >= 3.9 gem(rspec) <= 3.11
BuildRequires: gem(rspec-its) >= 1.2 gem(rspec-its) < 2
BuildRequires: gem(pry) >= 0.13 gem(pry) < 1
BuildRequires: gem(hashie) >= 3.4 gem(hashie) < 5.0
BuildRequires: gem(mixlib-log) >= 3.0 gem(mixlib-log) < 4
BuildRequires: gem(sslshake) >= 1.2 gem(sslshake) < 2
BuildRequires: gem(parallel) >= 1.9 gem(parallel) < 2
BuildRequires: gem(faraday) >= 1 gem(faraday) < 3
BuildRequires: gem(faraday-follow_redirects) >= 0.3 gem(faraday-follow_redirects) < 1
BuildRequires: gem(tty-table) >= 0.10 gem(tty-table) < 1
BuildRequires: gem(tty-prompt) >= 0.17 gem(tty-prompt) < 1
BuildRequires: gem(tomlrb) >= 1.2 gem(tomlrb) < 3
BuildRequires: gem(addressable) >= 2.4 gem(addressable) < 3
BuildRequires: gem(parslet) >= 1.5 gem(parslet) < 3
BuildRequires: gem(semverse) >= 3.0 gem(semverse) < 4
BuildRequires: gem(multipart-post) >= 2.0 gem(multipart-post) < 3
BuildRequires: gem(train-core) >= 3.10 gem(train-core) < 4
BuildRequires: gem(train) >= 3.10 gem(train) < 4
BuildRequires: gem(cookstyle) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(progress_bar) >= 1.3.3 gem(progress_bar) < 1.4
BuildRequires: gem(roo) >= 2.9.0 gem(roo) < 2.10
BuildRequires: gem(roo-xls) >= 0
BuildRequires: gem(faraday_middleware) >= 0.12.2 gem(faraday_middleware) < 2
BuildRequires: gem(train-habitat) >= 0.1 gem(train-habitat) < 1
BuildRequires: gem(train-aws) >= 0.2 gem(train-aws) < 1
BuildRequires: gem(train-winrm) >= 0.2 gem(train-winrm) < 1
BuildRequires: gem(mongo) >= 2.13.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
%ruby_use_gem_dependency faraday_middleware >= 1.2.0,faraday_middleware < 2
%ruby_use_gem_dependency parslet >= 2.0.0,parslet < 3
%ruby_use_gem_dependency html-proofer >= 5.0.0,html-proofer < 6
%ruby_use_gem_dependency json_schemer >= 0.2.22,json_schemer < 1
%ruby_use_gem_dependency mongo >= 2.13.2
%ruby_ignore_names omnibus
Requires:      gem(chef-telemetry) >= 1.0.8 gem(chef-telemetry) < 2
Requires:      gem(license-acceptance) >= 0.2.13 gem(license-acceptance) < 3.0
Requires:      gem(thor) >= 0.20 gem(thor) < 2.0
Requires:      gem(method_source) >= 0.8 gem(method_source) < 2.0
Requires:      gem(rubyzip) >= 1.2.2 gem(rubyzip) < 3.0
Requires:      gem(rspec) >= 3.9 gem(rspec) <= 3.11
Requires:      gem(rspec-its) >= 1.2 gem(rspec-its) < 2
Requires:      gem(pry) >= 0.13 gem(pry) < 1
Requires:      gem(hashie) >= 3.4 gem(hashie) < 5.0
Requires:      gem(mixlib-log) >= 3.0 gem(mixlib-log) < 4
Requires:      gem(sslshake) >= 1.2 gem(sslshake) < 2
Requires:      gem(parallel) >= 1.9 gem(parallel) < 2
Requires:      gem(faraday) >= 1 gem(faraday) < 3
Requires:      gem(faraday-follow_redirects) >= 0.3 gem(faraday-follow_redirects) < 1
Requires:      gem(tty-table) >= 0.10 gem(tty-table) < 1
Requires:      gem(tty-prompt) >= 0.17 gem(tty-prompt) < 1
Requires:      gem(tomlrb) >= 1.2 gem(tomlrb) < 3
Requires:      gem(addressable) >= 2.4 gem(addressable) < 3
Requires:      gem(parslet) >= 1.5 gem(parslet) < 3
Requires:      gem(semverse) >= 3.0 gem(semverse) < 4
Requires:      gem(multipart-post) >= 2.0 gem(multipart-post) < 3
Requires:      gem(train-core) >= 3.10 gem(train-core) < 4
Provides:      gem(inspec-core) = 6.2.9


%description
InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification. This has local support only. See the `inspec` gem for
full support.


%package       -n gem-inspec
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.2.9
Requires:      gem(train) >= 3.10 gem(train) < 4
Requires:      gem(cookstyle) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(progress_bar) >= 1.3.3 gem(progress_bar) < 1.4
Requires:      gem(roo) >= 2.9.0 gem(roo) < 2.10
Requires:      gem(roo-xls) >= 0
Requires:      gem(faraday_middleware) >= 0.12.2 gem(faraday_middleware) < 2
Requires:      gem(train-habitat) >= 0.1 gem(train-habitat) < 1
Requires:      gem(train-aws) >= 0.2 gem(train-aws) < 1
Requires:      gem(train-winrm) >= 0.2 gem(train-winrm) < 1
Requires:      gem(mongo) >= 2.13.2
Provides:      gem(inspec) = 6.2.9

%description   -n gem-inspec
Infrastructure and compliance testing. Core library.


%package       -n gem-inspec-doc
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec) = 6.2.9

%description   -n gem-inspec-doc
Infrastructure and compliance testing. Core library documentation files.

%description   -n gem-inspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec.


%package       -n gem-inspec-devel
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec) = 6.2.9
Requires:      gem(ffi) >= 1.9.14 gem(ffi) > 1.14.2
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(chefstyle) >= 2.0.3 gem(chefstyle) < 3
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(html-proofer) >= 3.19.4 gem(html-proofer) < 6
Requires:      gem(json_schemer) >= 0.2.1 gem(json_schemer) < 1
Requires:      gem(m) >= 0
Requires:      gem(minitest-sprint) >= 1.0 gem(minitest-sprint) < 2
Requires:      gem(minitest) >= 5.15.0 gem(minitest) < 6
Requires:      gem(mocha) >= 1.1 gem(mocha) < 2
Requires:      gem(nokogiri) >= 1.9 gem(nokogiri) < 2
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry) >= 0.10 gem(pry) < 1
Requires:      gem(rake) >= 10
Requires:      gem(ruby-progressbar) >= 1.8 gem(ruby-progressbar) < 2
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(simplecov_json_formatter) >= 0
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4

%description   -n gem-inspec-devel
Infrastructure and compliance testing. Core library development package.

%description   -n gem-inspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec.


%package       -n gem-inspec-bin
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec) = 6.2.9
Provides:      gem(inspec-bin) = 6.2.9

%description   -n gem-inspec-bin
Infrastructure and compliance testing. Core library.


%package       -n inspec
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета inspec-bin
Group:         Other
BuildArch:     noarch

Requires:      gem(inspec-bin) = 6.2.9

%description   -n inspec
Infrastructure and compliance testing. Core library executable(s).

%description   -n inspec -l ru_RU.UTF-8
Исполнямка для самоцвета inspec-bin.


%package       -n gem-inspec-bin-doc
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-bin) = 6.2.9

%description   -n gem-inspec-bin-doc
Infrastructure and compliance testing. Core library documentation files.

%description   -n gem-inspec-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec-bin.


%package       -n gem-inspec-bin-devel
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-bin) = 6.2.9
Requires:      gem(rake) >= 0

%description   -n gem-inspec-bin-devel
Infrastructure and compliance testing. Core library development package.

%description   -n gem-inspec-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec-bin.


%package       -n gem-inspec-core-bin
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.2.9
Provides:      gem(inspec-core-bin) = 6.2.9

%description   -n gem-inspec-core-bin
Infrastructure and compliance testing. Core library.


%package       -n gem-inspec-core-bin-doc
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-core-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-core-bin) = 6.2.9

%description   -n gem-inspec-core-bin-doc
Infrastructure and compliance testing. Core library documentation files.

%description   -n gem-inspec-core-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec-core-bin.


%package       -n gem-inspec-core-bin-devel
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-core-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core-bin) = 6.2.9
Requires:      gem(rake) >= 0
Requires:      gem(inspec-bin) = 6.2.9

%description   -n gem-inspec-core-bin-devel
Infrastructure and compliance testing. Core library development package.

%description   -n gem-inspec-core-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec-core-bin.


%package       -n inspec-core
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета inspec-core
Group:         Other
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.2.9

%description   -n inspec-core
Infrastructure and compliance testing. Core library executable(s).

InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification. This has local support only. See the `inspec` gem for
full support.

%description   -n inspec-core -l ru_RU.UTF-8
Исполнямка для самоцвета inspec-core.


%package       -n gem-inspec-core-doc
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.2.9

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
Version:       6.2.9
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.2.9
Requires:      gem(ffi) >= 1.9.14 gem(ffi) > 1.14.2
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(chefstyle) >= 2.0.3 gem(chefstyle) < 3
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(html-proofer) >= 3.19.4 gem(html-proofer) < 6
Requires:      gem(json_schemer) >= 0.2.1 gem(json_schemer) < 1
Requires:      gem(m) >= 0
Requires:      gem(minitest-sprint) >= 1.0 gem(minitest-sprint) < 2
Requires:      gem(minitest) >= 5.15.0 gem(minitest) < 6
Requires:      gem(mocha) >= 1.1 gem(mocha) < 2
Requires:      gem(nokogiri) >= 1.9 gem(nokogiri) < 2
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry) >= 0.10 gem(pry) < 1
Requires:      gem(rake) >= 10
Requires:      gem(ruby-progressbar) >= 1.8 gem(ruby-progressbar) < 2
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(simplecov_json_formatter) >= 0
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4

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
%doc lib/bundles/README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-inspec
%doc lib/plugins/inspec-init/templates/profiles/aws/README.md
%ruby_gemspecdir/inspec-6.2.9.gemspec
%ruby_gemslibdir/inspec-6.2.9

%files         -n gem-inspec-doc
%doc lib/plugins/inspec-init/templates/profiles/aws/README.md
%ruby_gemsdocdir/inspec-6.2.9

%files         -n gem-inspec-devel
%doc lib/plugins/inspec-init/templates/profiles/aws/README.md

%files         -n gem-inspec-bin
%doc README.md
%ruby_gemspecdir/inspec-bin-6.2.9.gemspec
%ruby_gemslibdir/inspec-bin-6.2.9

%files         -n inspec
%doc README.md
%_bindir/inspec

%files         -n gem-inspec-bin-doc
%doc README.md
%ruby_gemsdocdir/inspec-bin-6.2.9

%files         -n gem-inspec-bin-devel
%doc README.md

%files         -n gem-inspec-core-bin
%doc README.md
%ruby_gemspecdir/inspec-core-bin-6.2.9.gemspec
%ruby_gemslibdir/inspec-core-bin-6.2.9

%files         -n gem-inspec-core-bin-doc
%doc README.md
%ruby_gemsdocdir/inspec-core-bin-6.2.9

%files         -n gem-inspec-core-bin-devel
%doc README.md

%files         -n inspec-core
%doc lib/bundles/README.md

%files         -n gem-inspec-core-doc
%doc lib/bundles/README.md
%ruby_gemdocdir

%files         -n gem-inspec-core-devel
%doc lib/bundles/README.md


%changelog
* Thu Oct 27 2022 Pavel Skrylev <majioa@altlinux.org> 6.2.9-alt1
- ^ 4.38.6 -> 6.2.9

* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 4.38.6-alt1.1
- !fix deps to novel gems

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 4.38.6-alt1
- + packaged gem with Ruby Policy 2.0
