%define        gemname chef

Name:          gem-chef
Version:       18.0.167
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
BuildRequires: gem(pry) >= 0.13.0 gem(pry) < 1
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(ed25519) >= 1.2 gem(ed25519) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(fauxhai-ng) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(train-core) >= 3.2.28 gem(train-core) < 4
BuildRequires: gem(train-winrm) >= 0.2.5
BuildRequires: gem(train-rest) >= 0.4.1
BuildRequires: gem(license-acceptance) >= 1.0.5 gem(license-acceptance) < 3
BuildRequires: gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3.0
BuildRequires: gem(mixlib-log) >= 2.0.3 gem(mixlib-log) < 4.0
BuildRequires: gem(mixlib-authentication) >= 2.1 gem(mixlib-authentication) < 4
BuildRequires: gem(mixlib-shellout) >= 3.1.1 gem(mixlib-shellout) < 4.0
BuildRequires: gem(mixlib-archive) >= 0.4 gem(mixlib-archive) < 2.0
BuildRequires: gem(ohai) >= 18.0 gem(ohai) < 19
BuildRequires: gem(inspec-core) >= 5
BuildRequires: gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
BuildRequires: gem(net-sftp) >= 2.1.2 gem(net-sftp) < 4.0
BuildRequires: gem(net-ftp) >= 0
BuildRequires: gem(erubis) >= 2.7 gem(erubis) < 3
BuildRequires: gem(diff-lcs) >= 1.2.4 gem(diff-lcs) > 1.4.0 gem(diff-lcs) < 1.6.0
BuildRequires: gem(ffi-libarchive) >= 1.0.3 gem(ffi-libarchive) < 2
BuildRequires: gem(chef-zero) >= 14.0.11
BuildRequires: gem(plist) >= 3.2 gem(plist) < 4
BuildRequires: gem(iniparse) >= 1.4 gem(iniparse) < 2
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(syslog-logger) >= 1.6 gem(syslog-logger) < 2
BuildRequires: gem(uuidtools) >= 2.1.5 gem(uuidtools) < 3.0
BuildRequires: gem(unf_ext) >= 0.0.8.2
BuildRequires: gem(corefoundation) >= 0.3.4 gem(corefoundation) < 0.4
BuildRequires: gem(proxifier) >= 1.0 gem(proxifier) < 2
BuildRequires: gem(aws-sdk-s3) >= 1.91 gem(aws-sdk-s3) < 2
BuildRequires: gem(aws-sdk-secretsmanager) >= 1.46 gem(aws-sdk-secretsmanager) < 2
BuildRequires: gem(vault) >= 0.16 gem(vault) < 1
BuildRequires: gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
BuildRequires: gem(mixlib-config) >= 2.2.12 gem(mixlib-config) < 4.0
BuildRequires: gem(fuzzyurl) >= 0
BuildRequires: gem(tomlrb) >= 1.2 gem(tomlrb) < 3
BuildRequires: gem(cheffish) >= 14
BuildRequires: gem(pry) >= 0
BuildRequires: gem(ffi) >= 1.15
BuildRequires: gem(net-ssh) >= 5.1 gem(net-ssh) < 7
BuildRequires: gem(net-ssh-multi) >= 1.2.1 gem(net-ssh-multi) < 2
BuildRequires: gem(bcrypt_pbkdf) >= 1.1 gem(bcrypt_pbkdf) < 2
BuildRequires: gem(highline) >= 1.6.9 gem(highline) < 3
BuildRequires: gem(tty-prompt) >= 0.21 gem(tty-prompt) < 1
BuildRequires: gem(tty-screen) >= 0.6 gem(tty-screen) < 1
BuildRequires: gem(tty-table) >= 0.11 gem(tty-table) < 1
BuildRequires: gem(pastel) >= 0
BuildRequires: gem(concurrent-ruby) >= 0
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(cheffish) >= 17
BuildRequires: gem(appbundler) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(inspec-core-bin) >= 5
BuildRequires: gem(chef-vault) >= 0
BuildRequires: gem(pry) >= 0.13.0 gem(pry) < 1
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(ed25519) >= 1.2 gem(ed25519) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(fauxhai-ng) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(train-core) >= 3.2.28 gem(train-core) < 4
BuildRequires: gem(train-winrm) >= 0.2.5
BuildRequires: gem(train-rest) >= 0.4.1
BuildRequires: gem(license-acceptance) >= 1.0.5 gem(license-acceptance) < 3
BuildRequires: gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3.0
BuildRequires: gem(mixlib-log) >= 2.0.3 gem(mixlib-log) < 4.0
BuildRequires: gem(mixlib-authentication) >= 2.1 gem(mixlib-authentication) < 4
BuildRequires: gem(mixlib-shellout) >= 3.1.1 gem(mixlib-shellout) < 4.0
BuildRequires: gem(mixlib-archive) >= 0.4 gem(mixlib-archive) < 2.0
BuildRequires: gem(ohai) >= 18.0 gem(ohai) < 19
BuildRequires: gem(inspec-core) >= 5
BuildRequires: gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
BuildRequires: gem(net-sftp) >= 2.1.2 gem(net-sftp) < 4.0
BuildRequires: gem(net-ftp) >= 0
BuildRequires: gem(erubis) >= 2.7 gem(erubis) < 3
BuildRequires: gem(diff-lcs) >= 1.2.4 gem(diff-lcs) > 1.4.0 gem(diff-lcs) < 1.6.0
BuildRequires: gem(ffi-libarchive) >= 1.0.3 gem(ffi-libarchive) < 2
BuildRequires: gem(chef-zero) >= 14.0.11
BuildRequires: gem(plist) >= 3.2 gem(plist) < 4
BuildRequires: gem(iniparse) >= 1.4 gem(iniparse) < 2
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(syslog-logger) >= 1.6 gem(syslog-logger) < 2
BuildRequires: gem(uuidtools) >= 2.1.5 gem(uuidtools) < 3.0
BuildRequires: gem(unf_ext) >= 0.0.8.2
BuildRequires: gem(corefoundation) >= 0.3.4 gem(corefoundation) < 0.4
BuildRequires: gem(proxifier) >= 1.0 gem(proxifier) < 2
BuildRequires: gem(aws-sdk-s3) >= 1.91 gem(aws-sdk-s3) < 2
BuildRequires: gem(aws-sdk-secretsmanager) >= 1.46 gem(aws-sdk-secretsmanager) < 2
BuildRequires: gem(vault) >= 0.16 gem(vault) < 1
BuildRequires: gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
BuildRequires: gem(mixlib-config) >= 2.2.12 gem(mixlib-config) < 4.0
BuildRequires: gem(fuzzyurl) >= 0
BuildRequires: gem(tomlrb) >= 1.2 gem(tomlrb) < 3
BuildRequires: gem(cheffish) >= 14
BuildRequires: gem(pry) >= 0
BuildRequires: gem(ffi) >= 1.15
BuildRequires: gem(net-ssh) >= 5.1 gem(net-ssh) < 7
BuildRequires: gem(net-ssh-multi) >= 1.2.1 gem(net-ssh-multi) < 2
BuildRequires: gem(bcrypt_pbkdf) >= 1.1 gem(bcrypt_pbkdf) < 2
BuildRequires: gem(highline) >= 1.6.9 gem(highline) < 3
BuildRequires: gem(tty-prompt) >= 0.21 gem(tty-prompt) < 1
BuildRequires: gem(tty-screen) >= 0.6 gem(tty-screen) < 1
BuildRequires: gem(tty-table) >= 0.11 gem(tty-table) < 1
BuildRequires: gem(pastel) >= 0
BuildRequires: gem(concurrent-ruby) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_ignore_names omnibus,kitchen-tests,win32-eventlog
Requires:      gem(appbundler) >= 0
Requires:      gem(rb-readline) >= 0
Requires:      gem(inspec-core-bin) >= 5
Requires:      gem(chef-vault) >= 0
Requires:      gem(pry) >= 0.13.0 gem(pry) < 1
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(ed25519) >= 1.2 gem(ed25519) < 2
Requires:      gem(chef-config) = 18.0.167
Requires:      gem(chef-utils) = 18.0.167
Requires:      gem(train-core) >= 3.2.28 gem(train-core) < 4
Requires:      gem(train-winrm) >= 0.2.5
Requires:      gem(train-rest) >= 0.4.1
Requires:      gem(license-acceptance) >= 1.0.5 gem(license-acceptance) < 3
Requires:      gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3.0
Requires:      gem(mixlib-log) >= 2.0.3 gem(mixlib-log) < 4.0
Requires:      gem(mixlib-authentication) >= 2.1 gem(mixlib-authentication) < 4
Requires:      gem(mixlib-shellout) >= 3.1.1 gem(mixlib-shellout) < 4.0
Requires:      gem(mixlib-archive) >= 0.4 gem(mixlib-archive) < 2.0
Requires:      gem(ohai) >= 18.0 gem(ohai) < 19
Requires:      gem(inspec-core) >= 5
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
Requires:      gem(net-sftp) >= 2.1.2 gem(net-sftp) < 4.0
Requires:      gem(net-ftp) >= 0
Requires:      gem(erubis) >= 2.7 gem(erubis) < 3
Requires:      gem(diff-lcs) >= 1.2.4 gem(diff-lcs) > 1.4.0 gem(diff-lcs) < 1.6.0
Requires:      gem(ffi-libarchive) >= 1.0.3 gem(ffi-libarchive) < 2
Requires:      gem(chef-zero) >= 14.0.11
Requires:      gem(plist) >= 3.2 gem(plist) < 4
Requires:      gem(iniparse) >= 1.4 gem(iniparse) < 2
Requires:      gem(addressable) >= 0
Requires:      gem(syslog-logger) >= 1.6 gem(syslog-logger) < 2
Requires:      gem(uuidtools) >= 2.1.5 gem(uuidtools) < 3.0
Requires:      gem(unf_ext) >= 0.0.8.2
Requires:      gem(corefoundation) >= 0.3.4 gem(corefoundation) < 0.4
Requires:      gem(proxifier) >= 1.0 gem(proxifier) < 2
Requires:      gem(aws-sdk-s3) >= 1.91 gem(aws-sdk-s3) < 2
Requires:      gem(aws-sdk-secretsmanager) >= 1.46 gem(aws-sdk-secretsmanager) < 2
Requires:      gem(vault) >= 0.16 gem(vault) < 1
Obsoletes:     chef-doc < %EVR
Provides:      chef-doc = %EVR
Provides:      gem(chef) = 18.0.167


%description
Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.


%package       -n gem-chef-bin
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 18.0.167
Provides:      gem(chef-bin) = 18.0.167

%description   -n gem-chef-bin
Clients for the chef systems integration framework.


%package       -n gem-chef-bin-doc
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-bin) = 18.0.167

%description   -n gem-chef-bin-doc
Clients for the chef systems integration framework documentation files.

%description   -n gem-chef-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-bin.


%package       -n gem-chef-bin-devel
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-bin) = 18.0.167
Requires:      gem(rake) >= 0

%description   -n gem-chef-bin-devel
Clients for the chef systems integration framework development package.

%description   -n gem-chef-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-bin.


%package       -n gem-chef-config
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-utils) = 18.0.167
Requires:      gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
Requires:      gem(mixlib-config) >= 2.2.12 gem(mixlib-config) < 4.0
Requires:      gem(fuzzyurl) >= 0
Requires:      gem(addressable) >= 0
Requires:      gem(tomlrb) >= 1.2 gem(tomlrb) < 3
Provides:      gem(chef-config) = 18.0.167

%description   -n gem-chef-config
Clients for the chef systems integration framework.


%package       -n gem-chef-config-doc
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-config) = 18.0.167

%description   -n gem-chef-config-doc
Clients for the chef systems integration framework documentation files.

%description   -n gem-chef-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-config.


%package       -n gem-chef-config-devel
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-config) = 18.0.167
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-chef-config-devel
Clients for the chef systems integration framework development package.

%description   -n gem-chef-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-config.


%package       -n gem-knife
Version:       18.0.167
Release:       alt1
Summary:       The knife CLI for Chef Infra
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(chef-config) >= 18
Requires:      gem(chef-utils) >= 18
Requires:      gem(chef) >= 18
Requires:      gem(train-core) >= 3.2.28 gem(train-core) < 4
Requires:      gem(train-winrm) >= 0.2.5
Requires:      gem(license-acceptance) >= 1.0.5 gem(license-acceptance) < 3
Requires:      gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3.0
Requires:      gem(mixlib-archive) >= 0.4 gem(mixlib-archive) < 2.0
Requires:      gem(ohai) >= 18.0 gem(ohai) < 19
Requires:      gem(ffi) >= 1.15
Requires:      gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
Requires:      gem(net-ssh) >= 5.1 gem(net-ssh) < 7
Requires:      gem(net-ssh-multi) >= 1.2.1 gem(net-ssh-multi) < 2
Requires:      gem(bcrypt_pbkdf) >= 1.1 gem(bcrypt_pbkdf) < 2
Requires:      gem(highline) >= 1.6.9 gem(highline) < 3
Requires:      gem(tty-prompt) >= 0.21 gem(tty-prompt) < 1
Requires:      gem(tty-screen) >= 0.6 gem(tty-screen) < 1
Requires:      gem(tty-table) >= 0.11 gem(tty-table) < 1
Requires:      gem(pastel) >= 0
Requires:      gem(erubis) >= 2.7 gem(erubis) < 3
Requires:      gem(chef-vault) >= 0
Provides:      gem(knife) = 18.0.167

%description   -n gem-knife
The knife CLI for Chef Infra.


%package       -n knife
Version:       18.0.167
Release:       alt1
Summary:       The knife CLI for Chef Infra executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета knife
Group:         Other
BuildArch:     noarch

Requires:      gem(knife) = 18.0.167

%description   -n knife
The knife CLI for Chef Infra executable(s).

%description   -n knife -l ru_RU.UTF-8
Исполнямка для самоцвета knife.


%package       -n gem-knife-doc
Version:       18.0.167
Release:       alt1
Summary:       The knife CLI for Chef Infra documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета knife
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(knife) = 18.0.167

%description   -n gem-knife-doc
The knife CLI for Chef Infra documentation files.

%description   -n gem-knife-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета knife.


%package       -n gem-knife-devel
Version:       18.0.167
Release:       alt1
Summary:       The knife CLI for Chef Infra development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета knife
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(knife) = 18.0.167
Requires:      gem(cheffish) >= 14
Requires:      gem(webmock) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(chefstyle) >= 0

%description   -n gem-knife-devel
The knife CLI for Chef Infra development package.

%description   -n gem-knife-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета knife.


%package       -n gem-chef-utils
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby) >= 0
Provides:      ruby-gem-chef-utils
Provides:      gem(chef-utils) = 18.0.167

%description   -n gem-chef-utils
Basic utility functions for Core Chef Infra development


%package       -n gem-chef-utils-doc
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-utils) = 18.0.167

%description   -n gem-chef-utils-doc
Clients for the chef systems integration framework documentation files.

Basic utility functions for Core Chef Infra development

%description   -n gem-chef-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-utils.


%package       -n gem-chef-utils-devel
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-utils) = 18.0.167
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-chef-utils-devel
Clients for the chef systems integration framework development package.

Basic utility functions for Core Chef Infra development

%description   -n gem-chef-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-utils.


%package       -n chef
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 18.0.167

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


%package       -n gem-chef-doc
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef) = 18.0.167

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
Version:       18.0.167
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 18.0.167
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(cheffish) >= 17
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(chefstyle) >= 0

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
# Install init scripts
install -Dm 0755 %SOURCE1 %buildroot%_initdir/chef-client
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/chef-client.service
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/chef-client
install -Dm 0640 %SOURCE4 %buildroot%_sysconfdir/chef/client.rb

mkdir -p %buildroot%_var/log/chef
mkdir -p %buildroot%_var/lib/chef
mkdir -p %buildroot%_var/cache/chef
mkdir -p %buildroot/run/chef

%check
%ruby_test

%pre           -n chef
getent group _chef  >/dev/null || groupadd -r _chef
getent passwd _chef >/dev/null || useradd  -r -g _chef -d %_var/lib/chef -s /sbin/nologin -c "Opscode Chef Daemon" _chef


%files
%doc README.md spec/data/cb_version_cookbooks/tatft/README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-chef-bin
%ruby_gemspecdir/chef-bin-18.0.167.gemspec
%ruby_gemslibdir/chef-bin-18.0.167

%files         -n gem-chef-bin-doc
%ruby_gemsdocdir/chef-bin-18.0.167

%files         -n gem-chef-bin-devel

%files         -n gem-chef-config
%ruby_gemspecdir/chef-config-18.0.167.gemspec
%ruby_gemslibdir/chef-config-18.0.167

%files         -n gem-chef-config-doc
%ruby_gemsdocdir/chef-config-18.0.167

%files         -n gem-chef-config-devel

%files         -n gem-knife
%ruby_gemspecdir/knife-18.0.167.gemspec
%ruby_gemslibdir/knife-18.0.167

%files         -n knife
%_bindir/knife

%files         -n gem-knife-doc
%ruby_gemsdocdir/knife-18.0.167

%files         -n gem-knife-devel

%files         -n gem-chef-utils
%ruby_gemspecdir/chef-utils-18.0.167.gemspec
%ruby_gemslibdir/chef-utils-18.0.167

%files         -n gem-chef-utils-doc
%ruby_gemsdocdir/chef-utils-18.0.167

%files         -n gem-chef-utils-devel

%files         -n chef
%doc README.md spec/data/cb_version_cookbooks/tatft/README.rdoc
%_bindir/chef-apply
%_bindir/chef-client
%_bindir/chef-resource-inspector
%_bindir/chef-service-manager
%_bindir/chef-shell
%_bindir/chef-solo
%_bindir/chef-windows-service
%_initdir/chef-client
%_unitdir/chef-client.service
%_sysconfdir/sysconfig/chef-client
%config(noreplace) %attr(0640, root, _chef) %_sysconfdir/chef/client.rb
%dir %attr(0750, root, _chef) %_sysconfdir/chef
%dir %attr(0750, _chef, _chef) %_var/log/chef
%dir %attr(0750, _chef, _chef) %_var/lib/chef
%dir %attr(0750, _chef, _chef) %_var/cache/chef

%files         -n gem-chef-doc
%doc README.md spec/data/cb_version_cookbooks/tatft/README.rdoc
%ruby_gemdocdir

%files         -n gem-chef-devel
%doc README.md spec/data/cb_version_cookbooks/tatft/README.rdoc


%changelog
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
