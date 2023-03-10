%define        _unpackaged_files_terminate_build 1
%define        gemname chef

Name:          gem-chef
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework
License:       Apache-2.0
Group:         Networking/Other
Url:           https://www.chef.io/
Vcs:           https://github.com/opscode/chef.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       chef-client.init
Source2:       chef-client.service
Source3:       chef-client.default
Source4:       chef-client.rb
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(cheffish) >= 17
BuildRequires: gem(appbundler) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(inspec-core-bin) >= 5
BuildRequires: gem(chef-vault) >= 0
BuildRequires: gem(pry) >= 0.13.0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(ed25519) >= 1.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(fauxhai-ng) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(train-core) >= 3.10
BuildRequires: gem(train-winrm) >= 0.2.5
BuildRequires: gem(train-rest) >= 0.4.1
BuildRequires: gem(license-acceptance) >= 1.0.5
BuildRequires: gem(mixlib-cli) >= 2.1.1
BuildRequires: gem(mixlib-log) >= 2.0.3
BuildRequires: gem(mixlib-authentication) >= 2.1
BuildRequires: gem(mixlib-shellout) >= 3.1.1
BuildRequires: gem(mixlib-archive) >= 0.4
BuildRequires: gem(ohai) >= 18.0
BuildRequires: gem(inspec-core) >= 5
BuildRequires: gem(ffi-yajl) >= 2.2
BuildRequires: gem(net-sftp) >= 2.1.2
BuildRequires: gem(net-ftp) >= 0
BuildRequires: gem(erubis) >= 2.7
BuildRequires: gem(diff-lcs) > 1.4.0
BuildRequires: gem(ffi-libarchive) >= 1.0.3
BuildRequires: gem(chef-zero) >= 14.0.11
BuildRequires: gem(plist) >= 3.2
BuildRequires: gem(iniparse) >= 1.4
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(syslog-logger) >= 1.6
BuildRequires: gem(uuidtools) >= 2.1.5
BuildRequires: gem(unf_ext) >= 0.0.8.2
BuildRequires: gem(corefoundation) >= 0.3.4
BuildRequires: gem(proxifier2) >= 1.1
BuildRequires: gem(aws-sdk-s3) >= 1.91
BuildRequires: gem(aws-sdk-secretsmanager) >= 1.46
BuildRequires: gem(vault) >= 0.16
BuildRequires: gem(cheffish) >= 14
BuildRequires: gem(pry) >= 0
BuildRequires: gem(ffi) >= 1.15
BuildRequires: gem(net-ssh) >= 5.1
BuildRequires: gem(net-ssh-multi) >= 1.2.1
BuildRequires: gem(bcrypt_pbkdf) >= 1.1
BuildRequires: gem(highline) >= 1.6.9
BuildRequires: gem(tty-prompt) >= 0.21
BuildRequires: gem(tty-screen) >= 0.6
BuildRequires: gem(tty-table) >= 0.11
BuildRequires: gem(pastel) >= 0
BuildRequires: gem(concurrent-ruby) >= 0
BuildRequires: gem(mixlib-shellout) >= 2.0
BuildRequires: gem(mixlib-config) >= 2.2.12
BuildRequires: gem(fuzzyurl) >= 0
BuildRequires: gem(tomlrb) >= 1.2
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(ed25519) >= 2
BuildConflicts: gem(train-core) >= 4
BuildConflicts: gem(license-acceptance) >= 3
BuildConflicts: gem(mixlib-cli) >= 3.0
BuildConflicts: gem(mixlib-log) >= 4.0
BuildConflicts: gem(mixlib-authentication) >= 4
BuildConflicts: gem(mixlib-shellout) >= 4.0
BuildConflicts: gem(mixlib-archive) >= 2.0
BuildConflicts: gem(ohai) >= 19
BuildConflicts: gem(ffi-yajl) >= 3
BuildConflicts: gem(net-sftp) >= 5.0
BuildConflicts: gem(erubis) >= 3
BuildConflicts: gem(diff-lcs) >= 1.6.0
BuildConflicts: gem(ffi-libarchive) >= 2
BuildConflicts: gem(plist) >= 4
BuildConflicts: gem(iniparse) >= 2
BuildConflicts: gem(syslog-logger) >= 2
BuildConflicts: gem(uuidtools) >= 3.0
BuildConflicts: gem(corefoundation) >= 0.4
BuildConflicts: gem(proxifier2) >= 2
BuildConflicts: gem(aws-sdk-s3) >= 2
BuildConflicts: gem(aws-sdk-secretsmanager) >= 2
BuildConflicts: gem(vault) >= 1
BuildConflicts: gem(net-ssh) >= 8
BuildConflicts: gem(net-ssh-multi) >= 2
BuildConflicts: gem(bcrypt_pbkdf) >= 2
BuildConflicts: gem(highline) >= 3
BuildConflicts: gem(tty-prompt) >= 1
BuildConflicts: gem(tty-screen) >= 1
BuildConflicts: gem(tty-table) >= 1
BuildConflicts: gem(mixlib-config) >= 4.0
BuildConflicts: gem(tomlrb) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_ignore_names omnibus,kitchen-tests
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(chef-vault) >= 0
Requires:      gem(chef-config) = 18.1.32
Requires:      gem(chef-utils) = 18.1.32
Requires:      gem(train-core) >= 3.10
Requires:      gem(train-winrm) >= 0.2.5
Requires:      gem(train-rest) >= 0.4.1
Requires:      gem(license-acceptance) >= 1.0.5
Requires:      gem(mixlib-cli) >= 2.1.1
Requires:      gem(mixlib-log) >= 2.0.3
Requires:      gem(mixlib-authentication) >= 2.1
Requires:      gem(mixlib-shellout) >= 3.1.1
Requires:      gem(mixlib-archive) >= 0.4
Requires:      gem(ohai) >= 18.0
Requires:      gem(inspec-core) >= 5
Requires:      gem(ffi-yajl) >= 2.2
Requires:      gem(net-sftp) >= 2.1.2
Requires:      gem(net-ftp) >= 0
Requires:      gem(erubis) >= 2.7
Requires:      gem(diff-lcs) > 1.4.0
Requires:      gem(ffi-libarchive) >= 1.0.3
Requires:      gem(chef-zero) >= 14.0.11
Requires:      gem(plist) >= 3.2
Requires:      gem(iniparse) >= 1.4
Requires:      gem(addressable) >= 0
Requires:      gem(syslog-logger) >= 1.6
Requires:      gem(uuidtools) >= 2.1.5
Requires:      gem(unf_ext) >= 0.0.8.2
Requires:      gem(corefoundation) >= 0.3.4
Requires:      gem(proxifier2) >= 1.1
Requires:      gem(aws-sdk-s3) >= 1.91
Requires:      gem(aws-sdk-secretsmanager) >= 1.46
Requires:      gem(vault) >= 0.16
Conflicts:     gem(train-core) >= 4
Conflicts:     gem(license-acceptance) >= 3
Conflicts:     gem(mixlib-cli) >= 3.0
Conflicts:     gem(mixlib-log) >= 4.0
Conflicts:     gem(mixlib-authentication) >= 4
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(ohai) >= 19
Conflicts:     gem(ffi-yajl) >= 3
Conflicts:     gem(net-sftp) >= 5.0
Conflicts:     gem(erubis) >= 3
Conflicts:     gem(diff-lcs) >= 1.6.0
Conflicts:     gem(ffi-libarchive) >= 2
Conflicts:     gem(plist) >= 4
Conflicts:     gem(iniparse) >= 2
Conflicts:     gem(syslog-logger) >= 2
Conflicts:     gem(uuidtools) >= 3.0
Conflicts:     gem(corefoundation) >= 0.4
Conflicts:     gem(proxifier2) >= 2
Conflicts:     gem(aws-sdk-s3) >= 2
Conflicts:     gem(aws-sdk-secretsmanager) >= 2
Conflicts:     gem(vault) >= 1
Obsoletes:     chef-doc < %EVR
Provides:      chef-doc = %EVR
Provides:      gem(chef) = 18.1.32


%description
Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.


%package       -n gem-knife
Version:       18.1.32
Release:       alt1
Summary:       The knife CLI for Chef Infra
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-config) >= 18
Requires:      gem(chef-utils) >= 18
Requires:      gem(chef) >= 18
Requires:      gem(train-core) >= 3.10
Requires:      gem(train-winrm) >= 0.2.5
Requires:      gem(license-acceptance) >= 1.0.5
Requires:      gem(mixlib-cli) >= 2.1.1
Requires:      gem(mixlib-archive) >= 0.4
Requires:      gem(ohai) >= 18.0
Requires:      gem(ffi) >= 1.15
Requires:      gem(ffi-yajl) >= 2.2
Requires:      gem(net-ssh) >= 5.1
Requires:      gem(net-ssh-multi) >= 1.2.1
Requires:      gem(bcrypt_pbkdf) >= 1.1
Requires:      gem(highline) >= 1.6.9
Requires:      gem(tty-prompt) >= 0.21
Requires:      gem(tty-screen) >= 0.6
Requires:      gem(tty-table) >= 0.11
Requires:      gem(pastel) >= 0
Requires:      gem(erubis) >= 2.7
Requires:      gem(chef-vault) >= 0
Requires:      gem(proxifier2) >= 1.1
Conflicts:     gem(train-core) >= 4
Conflicts:     gem(license-acceptance) >= 3
Conflicts:     gem(mixlib-cli) >= 3.0
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(ohai) >= 19
Conflicts:     gem(ffi-yajl) >= 3
Conflicts:     gem(net-ssh) >= 8
Conflicts:     gem(net-ssh-multi) >= 2
Conflicts:     gem(bcrypt_pbkdf) >= 2
Conflicts:     gem(highline) >= 3
Conflicts:     gem(tty-prompt) >= 1
Conflicts:     gem(tty-screen) >= 1
Conflicts:     gem(tty-table) >= 1
Conflicts:     gem(erubis) >= 3
Conflicts:     gem(proxifier2) >= 2
Provides:      gem(knife) = 18.1.32

%description   -n gem-knife
The knife CLI for Chef Infra.


%package       -n knife
Version:       18.1.32
Release:       alt1
Summary:       The knife CLI for Chef Infra executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета knife
Group:         Other
BuildArch:     noarch

Requires:      gem(knife) = 18.1.32

%description   -n knife
The knife CLI for Chef Infra executable(s).

%description   -n knife -l ru_RU.UTF-8
Исполнямка для самоцвета knife.


%package       -n gem-knife-doc
Version:       18.1.32
Release:       alt1
Summary:       The knife CLI for Chef Infra documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета knife
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(knife) = 18.1.32

%description   -n gem-knife-doc
The knife CLI for Chef Infra documentation files.

%description   -n gem-knife-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета knife.


%package       -n gem-knife-devel
Version:       18.1.32
Release:       alt1
Summary:       The knife CLI for Chef Infra development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета knife
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(knife) = 18.1.32
Requires:      gem(cheffish) >= 14
Requires:      gem(webmock) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(chefstyle) >= 0

%description   -n gem-knife-devel
The knife CLI for Chef Infra development package.

%description   -n gem-knife-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета knife.


%package       -n gem-chef-bin
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 18.1.32
Provides:      gem(chef-bin) = 18.1.32

%description   -n gem-chef-bin
Chef-branded binstubs for chef-client.


%package       -n chef
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 18.1.32

%description   -n chef
Clients for the chef systems integration framework executable(s).

Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.

%description   -n chef -l ru_RU.UTF-8
Исполнямка для самоцвета chef.


%package       -n gem-chef-bin-doc
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-bin) = 18.1.32

%description   -n gem-chef-bin-doc
Clients for the chef systems integration framework documentation
files.

Chef-branded binstubs for chef-client.

%description   -n gem-chef-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-bin.


%package       -n gem-chef-bin-devel
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-bin) = 18.1.32
Requires:      gem(rake) >= 0

%description   -n gem-chef-bin-devel
Clients for the chef systems integration framework development
package.

Chef-branded binstubs for chef-client.

%description   -n gem-chef-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-bin.


%package       -n gem-chef-utils
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby) >= 0
Provides:      ruby-gem-chef-utils
Provides:      gem(chef-utils) = 18.1.32

%description   -n gem-chef-utils
Basic utility functions for Core Chef Infra development


%package       -n gem-chef-utils-doc
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-utils) = 18.1.32

%description   -n gem-chef-utils-doc
Clients for the chef systems integration framework documentation files.

Basic utility functions for Core Chef Infra development

%description   -n gem-chef-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-utils.


%package       -n gem-chef-utils-devel
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-utils) = 18.1.32
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-chef-utils-devel
Clients for the chef systems integration framework development package.

Basic utility functions for Core Chef Infra development

%description   -n gem-chef-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-utils.


%package       -n gem-chef-config
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-utils) = 18.1.32
Requires:      gem(mixlib-shellout) >= 2.0
Requires:      gem(mixlib-config) >= 2.2.12
Requires:      gem(fuzzyurl) >= 0
Requires:      gem(addressable) >= 0
Requires:      gem(tomlrb) >= 1.2
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(mixlib-config) >= 4.0
Conflicts:     gem(tomlrb) >= 3
Provides:      gem(chef-config) = 18.1.32

%description   -n gem-chef-config
Chef's default configuration and config loading.


%package       -n gem-chef-config-doc
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-config) = 18.1.32

%description   -n gem-chef-config-doc
Clients for the chef systems integration framework documentation files.

Chef's default configuration and config loading.

%description   -n gem-chef-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-config.


%package       -n gem-chef-config-devel
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-config) = 18.1.32
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-chef-config-devel
Clients for the chef systems integration framework development package.

Chef's default configuration and config loading.

%description   -n gem-chef-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-config.


%package       -n gem-chef-doc
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef) = 18.1.32

%description   -n gem-chef-doc
Clients for the chef systems integration framework documentation files.

Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.

%description   -n gem-chef-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef.


%package       -n gem-chef-devel
Version:       18.1.32
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 18.1.32
Requires:      gem(cheffish) >= 17
Requires:      gem(appbundler) >= 0
Requires:      gem(rb-readline) >= 0
Requires:      gem(inspec-core-bin) >= 5
Requires:      gem(pry) >= 0.13.0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(ed25519) >= 1.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(chefstyle) >= 0
Conflicts:     gem(pry) >= 1
Conflicts:     gem(ed25519) >= 2

%description   -n gem-chef-devel
Clients for the chef systems integration framework development package.

Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.

%description   -n gem-chef-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef.


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

%files         -n gem-knife
%doc README.md
%ruby_gemspecdir/knife-18.1.32.gemspec
%ruby_gemslibdir/knife-18.1.32

%files         -n knife
%doc README.md
%_bindir/knife

%files         -n gem-knife-doc
%doc README.md
%ruby_gemsdocdir/knife-18.1.32

%files         -n gem-knife-devel
%doc README.md

%files         -n gem-chef-bin
%doc README.md
%ruby_gemspecdir/chef-bin-18.1.32.gemspec
%ruby_gemslibdir/chef-bin-18.1.32

%files         -n chef
%doc README.md
%_bindir/chef-apply
%_bindir/chef-client
%_bindir/chef-resource-inspector
%_bindir/chef-service-manager
%_bindir/chef-shell
%_bindir/chef-solo
%_bindir/chef-windows-service

%files         -n gem-chef-bin-doc
%doc README.md
%ruby_gemsdocdir/chef-bin-18.1.32

%files         -n gem-chef-bin-devel
%doc README.md

%files         -n gem-chef-utils
%doc README.md
%ruby_gemspecdir/chef-utils-18.1.32.gemspec
%ruby_gemslibdir/chef-utils-18.1.32

%files         -n gem-chef-utils-doc
%doc README.md
%ruby_gemsdocdir/chef-utils-18.1.32

%files         -n gem-chef-utils-devel
%doc README.md

%files         -n gem-chef-config
%doc README.md
%ruby_gemspecdir/chef-config-18.1.32.gemspec
%ruby_gemslibdir/chef-config-18.1.32

%files         -n gem-chef-config-doc
%doc README.md
%ruby_gemsdocdir/chef-config-18.1.32

%files         -n gem-chef-config-devel
%doc README.md

%files         -n gem-chef-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-chef-devel
%doc README.md


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 18.1.32-alt1
- ^ 18.0.167 -> 18.1.32

* Thu Oct 27 2022 Pavel Skrylev <majioa@altlinux.org> 18.0.167-alt1
- ^ 18.0.91 -> 18.0.167

* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 18.0.91-alt1
- ^ 16.13.16 -> 18.0.91

* Sun Jul 11 2021 Pavel Skrylev <majioa@altlinux.org> 16.13.16-alt1
- ^ 16.5.32 -> 16.13.16

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 16.5.32-alt1
- ^ 16.2.89 -> 16.5.32
- ! build

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 16.2.89-alt1
- ^ 15.2.19 -> 16.2.89
- + chef-utils gem package

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 15.2.19-alt1
- ^ 15.0.201 -> 15.2.19

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.201-alt1
- ^ 15.0.167 -> 15.0.201

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.167-alt2
- > setup gem's dependency detection

* Wed Feb 20 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.167-alt1
- > Ruby Policy 2.0
- ^ 15.0.120 -> 15.0.167

* Fri Jan 04 2019 Andrey Cherepanov <cas@altlinux.org> 15.0.120-alt1
- New version.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.102-alt1
- New version.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.98-alt1
- New version.

* Tue Oct 30 2018 Pavel Skrylev <majioa@altlinux.org> 14.6.47-alt1
- Bump to 14.6.47.

* Thu Oct 04 2018 Pavel Skrylev <majioa@altlinux.org> 14.6.11-alt2
- Fix to files storing procedure.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 14.6.11-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.28-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.21-alt1
- New version.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 14.4.63-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.20-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.20-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.18-alt1
- New version.

* Tue Jun 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.17-alt1
- New version.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.16-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.10-alt1
- New version.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.5-alt1
- New version.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.2-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.21-alt1
- New version.

* Tue Mar 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.142-alt1
- New version.

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 13.4.15-alt1
- New version

* Mon Sep 04 2017 Andrey Cherepanov <cas@altlinux.org> 13.4.11-alt1
- New version

* Sun Aug 27 2017 Andrey Cherepanov <cas@altlinux.org> 13.3.52-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 12.19.2-alt1
- new version 12.19.2

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 12.15.11-alt1
- new version 12.15.11

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 12.11.18-alt1
- New version

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 12.6.0-alt1
- New version

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 12.5.1-alt1
- New version
- Package chef-config as separate package (need ro build ohai)

* Fri Oct 02 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.4-alt1
- New version

* Sun Sep 20 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.2-alt1
- New version
- Check for component versions according chef.gemspec

* Mon Aug 03 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 12.3.0-alt1
- New version

* Sat Jan 24 2015 Andrey Cherepanov <cas@altlinux.org> 12.0.6-alt1
- Initial build in Sisyphus
