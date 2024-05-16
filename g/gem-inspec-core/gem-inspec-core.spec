%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname inspec-core

Name:          gem-inspec-core
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/inspec
Vcs:           https://github.com/inspec/inspec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ffi) >= 1.9.14
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(appbundler) >= 0
BuildRequires: gem(ed25519) >= 0
BuildRequires: gem(bcrypt_pbkdf) >= 0
BuildRequires: gem(x25519) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(concurrent-ruby) >= 0
BuildRequires: gem(json_schemer) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest-sprint) >= 1.0
BuildRequires: gem(minitest) >= 5.15.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov_json_formatter) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(inquirer) >= 0
BuildRequires: gem(chef-telemetry) >= 1.0.8
BuildRequires: gem(license-acceptance) >= 0.2.13
BuildRequires: gem(thor) >= 0.20
BuildRequires: gem(method_source) >= 0.8
BuildRequires: gem(rubyzip) >= 1.2.2
BuildRequires: gem(rspec-its) >= 1.2
BuildRequires: gem(hashie) >= 3.4
BuildRequires: gem(mixlib-log) >= 3.0
BuildRequires: gem(sslshake) >= 1.2
BuildRequires: gem(parallel) >= 1.9
BuildRequires: gem(faraday) >= 1
BuildRequires: gem(faraday-follow_redirects) >= 0.3
BuildRequires: gem(tty-table) >= 0.10
BuildRequires: gem(tty-prompt) >= 0.17
BuildRequires: gem(tomlrb) >= 1.2
BuildRequires: gem(addressable) >= 2.4
BuildRequires: gem(parslet) >= 1.5
BuildRequires: gem(semverse) >= 3.0
BuildRequires: gem(multipart-post) >= 2.0
BuildRequires: gem(train-core) >= 3.11.0
BuildRequires: gem(chef-licensing) >= 0.7.5
BuildRequires: gem(train) >= 3.10
BuildRequires: gem(cookstyle) >= 0
BuildRequires: gem(progress_bar) >= 1.3.3
BuildRequires: gem(faraday_middleware) >= 0.12.2
BuildRequires: gem(train-habitat) >= 0.1
BuildRequires: gem(train-aws) >= 0.2
BuildRequires: gem(train-winrm) >= 0.2
BuildRequires: gem(train-kubernetes) >= 0.1
BuildRequires: gem(mongo) >= 2.13.2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(minitest-sprint) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(chef-telemetry) >= 2
BuildConflicts: gem(license-acceptance) >= 3.0
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(method_source) >= 2.0
BuildConflicts: gem(rubyzip) >= 3
BuildConflicts: gem(rspec-its) >= 2
BuildConflicts: gem(hashie) >= 6.0
BuildConflicts: gem(mixlib-log) >= 4
BuildConflicts: gem(sslshake) >= 2
BuildConflicts: gem(parallel) >= 2
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday-follow_redirects) >= 1
BuildConflicts: gem(tty-table) >= 1
BuildConflicts: gem(tty-prompt) >= 1
BuildConflicts: gem(tomlrb) >= 3
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(parslet) >= 3
BuildConflicts: gem(semverse) >= 4
BuildConflicts: gem(multipart-post) >= 3
BuildConflicts: gem(train) >= 4
BuildConflicts: gem(progress_bar) >= 1.4
BuildConflicts: gem(faraday_middleware) >= 2
BuildConflicts: gem(train-habitat) >= 1
BuildConflicts: gem(train-aws) >= 1
BuildConflicts: gem(train-winrm) >= 1
BuildConflicts: gem(train-kubernetes) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency thor >= 1.2.1,thor < 2
%ruby_use_gem_dependency ffi >= 1.15.5,ffi < 2
%ruby_use_gem_dependency mongo >= 2.13.2,mongo < 3
%ruby_use_gem_dependency rspec >= 3.12,rspec < 4
%ruby_use_gem_dependency parslet >= 2.0,parslet < 3
%ruby_use_gem_dependency faraday_middleware >= 1.2,faraday_middleware < 2
%ruby_ignore_names omnibus,kitchen,rake-tests
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(pry) >= 0
Requires:      gem(chef-telemetry) >= 1.0.8
Requires:      gem(license-acceptance) >= 0.2.13
Requires:      gem(thor) >= 0.20
Requires:      gem(method_source) >= 0.8
Requires:      gem(rubyzip) >= 1.2.2
Requires:      gem(rspec-its) >= 1.2
Requires:      gem(hashie) >= 3.4
Requires:      gem(mixlib-log) >= 3.0
Requires:      gem(sslshake) >= 1.2
Requires:      gem(parallel) >= 1.9
Requires:      gem(faraday) >= 1
Requires:      gem(faraday-follow_redirects) >= 0.3
Requires:      gem(tty-table) >= 0.10
Requires:      gem(tty-prompt) >= 0.17
Requires:      gem(tomlrb) >= 1.2
Requires:      gem(addressable) >= 2.4
Requires:      gem(parslet) >= 1.5
Requires:      gem(semverse) >= 3.0
Requires:      gem(multipart-post) >= 2.0
Requires:      gem(train-core) >= 3.11.0
Requires:      gem(chef-licensing) >= 0.7.5
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(chef-telemetry) >= 2
Conflicts:     gem(license-acceptance) >= 3.0
Conflicts:     gem(thor) >= 2
Conflicts:     gem(method_source) >= 2.0
Conflicts:     gem(rubyzip) >= 3
Conflicts:     gem(rspec-its) >= 2
Conflicts:     gem(hashie) >= 6.0
Conflicts:     gem(mixlib-log) >= 4
Conflicts:     gem(sslshake) >= 2
Conflicts:     gem(parallel) >= 2
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday-follow_redirects) >= 1
Conflicts:     gem(tty-table) >= 1
Conflicts:     gem(tty-prompt) >= 1
Conflicts:     gem(tomlrb) >= 3
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(parslet) >= 3
Conflicts:     gem(semverse) >= 4
Conflicts:     gem(multipart-post) >= 3
Provides:      gem(inspec-core) = 6.6.16


%description
InSpec provides a framework for creating end-to-end infrastructure tests. You
can use it for integration or even compliance testing. Create fully portable
test profiles and use them in your workflow to ensure stability and security.
Integrate InSpec in your change lifecycle for local testing, CI/CD, and
deployment verification. This has local support only. See the `inspec` gem for
full support.


%package       -n gem-inspec
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rake) >= 0
Requires:      gem(inspec-core) >= 6.2.9
Requires:      gem(train) >= 3.10
Requires:      gem(cookstyle) >= 0
Requires:      gem(progress_bar) >= 1.3.3
Requires:      gem(faraday_middleware) >= 0.12.2
Requires:      gem(train-habitat) >= 0.1
Requires:      gem(train-aws) >= 0.2
Requires:      gem(train-winrm) >= 0.2
Requires:      gem(train-kubernetes) >= 0.1
Requires:      gem(mongo) >= 2.13.2
Conflicts:     gem(inspec-core) >= 7
Conflicts:     gem(train) >= 4
Conflicts:     gem(progress_bar) >= 1.4
Conflicts:     gem(faraday_middleware) >= 2
Conflicts:     gem(train-habitat) >= 1
Conflicts:     gem(train-aws) >= 1
Conflicts:     gem(train-winrm) >= 1
Conflicts:     gem(train-kubernetes) >= 1
Provides:      gem(inspec) = 6.6.16

%description   -n gem-inspec
Infrastructure and compliance testing. Core library.


%if_enabled    doc
%package       -n gem-inspec-doc
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec) = 6.6.16

%description   -n gem-inspec-doc
Infrastructure and compliance testing. Core library documentation files.
%description   -n gem-inspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec.
%endif


%if_enabled    devel
%package       -n gem-inspec-devel
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec) = 6.6.16
Requires:      gem(ffi) >= 1.9.14
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rb-readline) >= 0
Requires:      gem(appbundler) >= 0
Requires:      gem(ed25519) >= 0
Requires:      gem(bcrypt_pbkdf) >= 0
Requires:      gem(x25519) >= 0
Requires:      gem(chefstyle) >= 0
Requires:      gem(concurrent-ruby) >= 0
Requires:      gem(json_schemer) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest-sprint) >= 1.0
Requires:      gem(minitest) >= 5.15.0
Requires:      gem(mocha) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov_json_formatter) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(inquirer) >= 0
Conflicts:     gem(minitest-sprint) >= 2
Conflicts:     gem(minitest) >= 6

%description   -n gem-inspec-devel
Infrastructure and compliance testing. Core library development package.
%description   -n gem-inspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec.
%endif


%package       -n gem-inspec-bin
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec) = 6.6.16
Provides:      gem(inspec-bin) = 6.6.16

%description   -n gem-inspec-bin
Infrastructure and compliance testing. Core library.


%package       -n inspec
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета inspec-bin
Group:         Other
BuildArch:     noarch

Requires:      gem(inspec-bin) = 6.6.16

%description   -n inspec
Infrastructure and compliance testing. Core library executable(s).
%description   -n inspec -l ru_RU.UTF-8
Исполнямка для самоцвета inspec-bin.


%if_enabled    doc
%package       -n gem-inspec-bin-doc
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-bin) = 6.6.16

%description   -n gem-inspec-bin-doc
Infrastructure and compliance testing. Core library documentation files.
%description   -n gem-inspec-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec-bin.
%endif


%if_enabled    devel
%package       -n gem-inspec-bin-devel
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-bin) = 6.6.16
Requires:      gem(rake) >= 0

%description   -n gem-inspec-bin-devel
Infrastructure and compliance testing. Core library development package.
%description   -n gem-inspec-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec-bin.
%endif


%package       -n gem-inspec-core-bin
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) >= 6.2.9
Conflicts:     gem(inspec-core) >= 7
Provides:      gem(inspec-core-bin) = 6.6.16

%description   -n gem-inspec-core-bin
Infrastructure and compliance testing. Core library.


%if_enabled    doc
%package       -n gem-inspec-core-bin-doc
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-core-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-core-bin) = 6.6.16

%description   -n gem-inspec-core-bin-doc
Infrastructure and compliance testing. Core library documentation files.
%description   -n gem-inspec-core-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inspec-core-bin.
%endif


%if_enabled    devel
%package       -n gem-inspec-core-bin-devel
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-core-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core-bin) = 6.6.16
Requires:      gem(rake) >= 0
Requires:      gem(inspec-bin) = 6.6.16

%description   -n gem-inspec-core-bin-devel
Infrastructure and compliance testing. Core library development package.
%description   -n gem-inspec-core-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inspec-core-bin.
%endif


%package       -n inspec-core
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета inspec-core
Group:         Other
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.6.16

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


%if_enabled    doc
%package       -n gem-inspec-core-doc
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inspec-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.6.16

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
%endif


%if_enabled    devel
%package       -n gem-inspec-core-devel
Version:       6.6.16
Release:       alt1
Summary:       Infrastructure and compliance testing. Core library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inspec-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inspec-core) = 6.6.16
Requires:      gem(ffi) >= 1.9.14
Requires:      gem(rb-readline) >= 0
Requires:      gem(appbundler) >= 0
Requires:      gem(ed25519) >= 0
Requires:      gem(bcrypt_pbkdf) >= 0
Requires:      gem(x25519) >= 0
Requires:      gem(chefstyle) >= 0
Requires:      gem(concurrent-ruby) >= 0
Requires:      gem(json_schemer) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest-sprint) >= 1.0
Requires:      gem(minitest) >= 5.15.0
Requires:      gem(mocha) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov_json_formatter) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(inquirer) >= 0
Conflicts:     gem(minitest-sprint) >= 2
Conflicts:     gem(minitest) >= 6

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
%endif


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
%ruby_gemspecdir/inspec-6.6.16.gemspec
%ruby_gemslibdir/inspec-6.6.16

%if_enabled    doc
%files         -n gem-inspec-doc
%doc lib/plugins/inspec-init/templates/profiles/aws/README.md
%ruby_gemsdocdir/inspec-6.6.16
%endif

%if_enabled    devel
%files         -n gem-inspec-devel
%doc lib/plugins/inspec-init/templates/profiles/aws/README.md
%endif

%files         -n gem-inspec-bin
%doc README.md
%ruby_gemspecdir/inspec-bin-6.6.16.gemspec
%ruby_gemslibdir/inspec-bin-6.6.16

%files         -n inspec
%doc README.md
%_bindir/inspec

%if_enabled    doc
%files         -n gem-inspec-bin-doc
%doc README.md
%ruby_gemsdocdir/inspec-bin-6.6.16
%endif

%if_enabled    devel
%files         -n gem-inspec-bin-devel
%doc README.md
%endif

%files         -n gem-inspec-core-bin
%doc README.md
%ruby_gemspecdir/inspec-core-bin-6.6.16.gemspec
%ruby_gemslibdir/inspec-core-bin-6.6.16

%if_enabled    doc
%files         -n gem-inspec-core-bin-doc
%doc README.md
%ruby_gemsdocdir/inspec-core-bin-6.6.16
%endif

%if_enabled    devel
%files         -n gem-inspec-core-bin-devel
%doc README.md
%endif

%files         -n inspec-core
%doc lib/bundles/README.md

%if_enabled    doc
%files         -n gem-inspec-core-doc
%doc lib/bundles/README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-inspec-core-devel
%doc lib/bundles/README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 6.6.16-alt1
- ^ 6.2.9 -> 6.6.16

* Thu Oct 27 2022 Pavel Skrylev <majioa@altlinux.org> 6.2.9-alt1
- ^ 4.38.6 -> 6.2.9

* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 4.38.6-alt1.1
- !fix deps to novel gems

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 4.38.6-alt1
- + packaged gem with Ruby Policy 2.0
