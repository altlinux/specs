%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname chef

Name:          gem-chef
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework
License:       Apache-2.0
Group:         Networking/Other
Url:           https://www.chef.io/
Vcs:           https://github.com/opscode/chef.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       chef-client.init
Source2:       chef-client.service
Source3:       chef-client.sysconfig
Source4:       chef-client.rb
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(abbrev) >= 0
BuildRequires: gem(activesupport) >= 7.1
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(aws-sdk-s3) >= 1.91
BuildRequires: gem(aws-sdk-secretsmanager) >= 1.46
BuildRequires: gem(bcrypt_pbkdf) >= 1.1
BuildRequires: gem(chef-licensing) >= 0.7.5
BuildRequires: gem(chef-vault) >= 0
BuildRequires: gem(chef-zero) >= 15.0.21
BuildRequires: gem(cheffish) >= 0
BuildRequires: gem(concurrent-ruby) >= 0
BuildRequires: gem(cookstyle) >= 7.32.8
BuildRequires: gem(corefoundation) >= 0.3.4
BuildRequires: gem(csv) >= 3.3.5
BuildRequires: gem(diff-lcs) >= 1.4.0
BuildRequires: gem(erubis) >= 2.7
BuildRequires: gem(fauxhai-ng) >= 0
BuildRequires: gem(ffi) >= 1.15
BuildRequires: gem(ffi-libarchive) >= 1.0
BuildRequires: gem(ffi-yajl) >= 2.2
BuildRequires: gem(fuzzyurl) >= 0
BuildRequires: gem(highline) >= 1.6.9
BuildRequires: gem(iniparse) >= 1.4
BuildRequires: gem(inspec-core) >= 6.2.9
BuildRequires: gem(license-acceptance) >= 1.0.5
BuildRequires: gem(mixlib-archive) >= 0.4
BuildRequires: gem(mixlib-authentication) >= 2.1
BuildRequires: gem(mixlib-cli) >= 2.1.1
BuildRequires: gem(mixlib-config) >= 2.2.12
BuildRequires: gem(mixlib-log) >= 2.0.3
BuildRequires: gem(net-ftp) >= 0
BuildRequires: gem(net-sftp) >= 2.1.2
BuildRequires: gem(net-ssh) >= 5.1
BuildRequires: gem(net-ssh-multi) >= 1.2.1
BuildRequires: gem(ohai) >= 18.1.16
BuildRequires: gem(openssl) >= 3.0.0
BuildRequires: gem(pastel) >= 0
BuildRequires: gem(plist) >= 3.2
BuildRequires: gem(proxifier2) >= 1.1
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(syslog) >= 0
BuildRequires: gem(syslog-logger) >= 1.6
BuildRequires: gem(tomlrb) >= 1.2
BuildRequires: gem(train-core) >= 3.11.1
BuildRequires: gem(train-rest) >= 0.4.1
BuildRequires: gem(train-winrm) >= 0.2.13
BuildRequires: gem(tty-prompt) >= 0.21
BuildRequires: gem(tty-screen) >= 0.6
BuildRequires: gem(tty-table) >= 0.11
BuildRequires: gem(unf_ext) >= 0.0.8.2
BuildRequires: gem(uri) >= 1.0.3
BuildRequires: gem(vault) >= 0.18.2
BuildRequires: gem(webmock) >= 0
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(aws-sdk-s3) >= 2
BuildConflicts: gem(aws-sdk-secretsmanager) >= 2
BuildConflicts: gem(bcrypt_pbkdf) >= 2
BuildConflicts: gem(chef-zero) >= 16
BuildConflicts: gem(corefoundation) >= 1
BuildConflicts: gem(crack) >= 0.4.6
BuildConflicts: gem(csv) >= 3.4
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(erubis) >= 3
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(ffi-yajl) >= 3
BuildConflicts: gem(highline) >= 4
BuildConflicts: gem(iniparse) >= 2
BuildConflicts: gem(inspec-core) >= 7.1
BuildConflicts: gem(license-acceptance) >= 3
BuildConflicts: gem(mixlib-archive) >= 2.0
BuildConflicts: gem(mixlib-authentication) >= 4
BuildConflicts: gem(mixlib-cli) >= 3.0
BuildConflicts: gem(mixlib-config) >= 4.0
BuildConflicts: gem(mixlib-log) >= 4.0
BuildConflicts: gem(mixlib-shellout) >= 4
BuildConflicts: gem(net-sftp) >= 5.0
BuildConflicts: gem(net-ssh) >= 8
BuildConflicts: gem(net-ssh-multi) >= 2
BuildConflicts: gem(ohai) >= 20
BuildConflicts: gem(openssl) >= 4
BuildConflicts: gem(plist) >= 4
BuildConflicts: gem(proxifier2) >= 2
BuildConflicts: gem(syslog-logger) >= 2
BuildConflicts: gem(tomlrb) >= 3
BuildConflicts: gem(train-core) >= 4
BuildConflicts: gem(tty-prompt) >= 1
BuildConflicts: gem(tty-screen) >= 1
BuildConflicts: gem(tty-table) >= 1
BuildConflicts: gem(unf_ext) >= 1
BuildConflicts: gem(uri) >= 2
BuildConflicts: gem(vault) >= 0.19
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency diff-lcs >= 2.0.0,diff-lcs < 3
%ruby_use_gem_dependency chef-zero >= 15.1.6,chef-zero < 16
%ruby_use_gem_dependency unf_ext >= 0.0.9.1,unf_ext < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
%ruby_use_gem_dependency openssl >= 3.0.0,openssl < 4
%ruby_use_gem_dependency train-winrm >= 0.2.13,train-winrm < 1
%ruby_use_gem_dependency train-core >= 3.11.1,train-core < 4
%ruby_use_gem_dependency ohai >= 18.1.16,ohai < 19
%ruby_use_gem_dependency inspec-core >= 6.2.9,inspec-core < 7
%ruby_use_gem_dependency corefoundation >= 0.3.14,corefoundation < 1
%ruby_use_gem_dependency ffi-libarchive >= 1.1.13,ffi-libarchive < 2
%ruby_use_gem_dependency ffi >= 1.15.5,ffi < 2
%ruby_use_gem_dependency uri >= 1.1,uri < 2
%ruby_use_gem_dependency highline >= 3.1.2,highline < 4
%ruby_use_gem_dependency mixlib-shellout >= 3.4.9,mixlib-shellout < 4
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
Requires:      ruby >= 3.1.0
Requires:      gem(activesupport) >= 7.1
Requires:      gem(addressable) >= 0
Requires:      gem(aws-sdk-s3) >= 1.91
Requires:      gem(aws-sdk-secretsmanager) >= 1.46
Requires:      gem(chef-licensing) >= 0.7.5
Requires:      gem(chef-vault) >= 0
Requires:      gem(chef-zero) >= 15.0.21
Requires:      gem(cheffish) >= 0
Requires:      gem(corefoundation) >= 0.3.4
Requires:      gem(csv) >= 3.3.5
Requires:      gem(diff-lcs) >= 1.4.0
Requires:      gem(erubis) >= 2.7
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(ffi-libarchive) >= 1.0
Requires:      gem(ffi-yajl) >= 2.2
Requires:      gem(iniparse) >= 1.4
Requires:      gem(inspec-core) >= 6.2.9
Requires:      gem(license-acceptance) >= 1.0.5
Requires:      gem(mixlib-archive) >= 0.4
Requires:      gem(mixlib-authentication) >= 2.1
Requires:      gem(mixlib-cli) >= 2.1.1
Requires:      gem(mixlib-log) >= 2.0.3
Requires:      gem(mixlib-shellout) >= 3.3.8
Requires:      gem(net-ftp) >= 0
Requires:      gem(net-sftp) >= 2.1.2
Requires:      gem(ohai) >= 18.1.16
Requires:      gem(plist) >= 3.2
Requires:      gem(proxifier2) >= 1.1
Requires:      gem(syslog) >= 0
Requires:      gem(syslog-logger) >= 1.6
Requires:      gem(train-core) >= 3.11.1
Requires:      gem(train-rest) >= 0.4.1
Requires:      gem(train-winrm) >= 0.2.13
Requires:      gem(unf_ext) >= 0.0.8.2
Requires:      gem(uri) >= 1.0.3
Requires:      gem(vault) >= 0.18.2
Conflicts:     gem(activesupport) >= 8
Conflicts:     gem(aws-sdk-s3) >= 2
Conflicts:     gem(aws-sdk-secretsmanager) >= 2
Conflicts:     gem(chef-zero) >= 16
Conflicts:     gem(corefoundation) >= 1
Conflicts:     gem(csv) >= 3.4
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(erubis) >= 3
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(ffi-yajl) >= 3
Conflicts:     gem(iniparse) >= 2
Conflicts:     gem(inspec-core) >= 7.1
Conflicts:     gem(license-acceptance) >= 3
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(mixlib-authentication) >= 4
Conflicts:     gem(mixlib-cli) >= 3.0
Conflicts:     gem(mixlib-log) >= 4.0
Conflicts:     gem(mixlib-shellout) >= 4
Conflicts:     gem(net-sftp) >= 5.0
Conflicts:     gem(ohai) >= 20
Conflicts:     gem(plist) >= 4
Conflicts:     gem(proxifier2) >= 2
Conflicts:     gem(syslog-logger) >= 2
Conflicts:     gem(unf_ext) >= 1
Conflicts:     gem(uri) >= 2
Conflicts:     gem(vault) >= 0.19
Obsoletes:     chef-doc < %EVR
Provides:      chef-doc = %EVR
Provides:      gem(chef) = 19.1.176

%ruby_ignore_names kitchen-tests

%description
Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.


%package       -n gem-knife
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby >= 3.1.0
Requires:      gem(abbrev) >= 0
Requires:      gem(bcrypt_pbkdf) >= 1.1
Requires:      gem(chef) >= 19
Requires:      gem(chef-config) >= 19
Requires:      gem(chef-utils) >= 19
Requires:      gem(chef-vault) >= 0
Requires:      gem(cheffish) >= 0
Requires:      gem(erubis) >= 2.7
Requires:      gem(ffi) >= 1.15
Requires:      gem(ffi-yajl) >= 2.2
Requires:      gem(highline) >= 1.6.9
Requires:      gem(knife) >= 0
Requires:      gem(license-acceptance) >= 1.0.5
Requires:      gem(mixlib-archive) >= 0.4
Requires:      gem(mixlib-cli) >= 2.1.1
Requires:      gem(net-ssh) >= 5.1
Requires:      gem(net-ssh-multi) >= 1.2.1
Requires:      gem(ohai) >= 19.0
Requires:      gem(pastel) >= 0
Requires:      gem(proxifier2) >= 1.1
Requires:      gem(train-core) >= 3.11.5
Requires:      gem(train-winrm) >= 0.2.17
Requires:      gem(tty-prompt) >= 0.21
Requires:      gem(tty-screen) >= 0.6
Requires:      gem(tty-table) >= 0.11
Conflicts:     gem(bcrypt_pbkdf) >= 2
Conflicts:     gem(erubis) >= 3
Conflicts:     gem(ffi) >= 1.18.0
Conflicts:     gem(ffi-yajl) >= 3
Conflicts:     gem(highline) >= 4
Conflicts:     gem(license-acceptance) >= 3
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(mixlib-cli) >= 3.0
Conflicts:     gem(net-ssh) >= 8
Conflicts:     gem(net-ssh-multi) >= 2
Conflicts:     gem(ohai) >= 20
Conflicts:     gem(proxifier2) >= 2
Conflicts:     gem(train-core) >= 4
Conflicts:     gem(tty-prompt) >= 1
Conflicts:     gem(tty-screen) >= 1
Conflicts:     gem(tty-table) >= 1
Provides:      gem(knife) = 19.1.176

%description   -n gem-knife
The knife CLI for Chef Infra.


%package       -n knife
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета knife
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(knife) = 19.1.176
Requires:      gem(cheffish) >= 0
Requires:      gem(ohai) >= 18.1.16
Conflicts:     gem(ohai) >= 20

%description   -n knife
Clients for the chef systems integration framework executable(s).

The knife CLI for Chef Infra.

%description   -n knife -l ru_RU.UTF-8
Исполнямка для самоцвета knife.


%if_enabled    doc
%package       -n gem-knife-doc
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета knife
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(knife) = 19.1.176

%description   -n gem-knife-doc
Clients for the chef systems integration framework documentation files.

The knife CLI for Chef Infra.

%description   -n gem-knife-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета knife.
%endif


%if_enabled    devel
%package       -n gem-knife-devel
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета knife
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(knife) = 19.1.176
Requires:      gem(cookstyle) >= 7.32.8
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Conflicts:     gem(crack) >= 0.4.6

%description   -n gem-knife-devel
Clients for the chef systems integration framework development package.

The knife CLI for Chef Infra.

%description   -n gem-knife-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета knife.
%endif


%package       -n gem-chef-bin
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef) = 19.1.176
Requires:      gem(chef-bin) >= 0
Provides:      chef-bin = %EVR
Provides:      gem(chef-bin) = 19.1.176

%description   -n gem-chef-bin
Chef-branded binstubs for chef-client.


%package       -n chef
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef-bin
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-bin) = 19.1.176

%description   -n chef
Clients for the chef systems integration framework executable(s).

Chef-branded binstubs for chef-client.

%description   -n chef -l ru_RU.UTF-8
Исполнямка для самоцвета chef-bin.


%if_enabled    doc
%package       -n gem-chef-bin-doc
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-bin
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-bin) = 19.1.176

%description   -n gem-chef-bin-doc
Clients for the chef systems integration framework documentation
files.

Chef-branded binstubs for chef-client.

%description   -n gem-chef-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-bin.
%endif


%if_enabled    devel
%package       -n gem-chef-bin-devel
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-bin
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-bin) = 19.1.176
Requires:      gem(rake) >= 12.3.3

%description   -n gem-chef-bin-devel
Clients for the chef systems integration framework development
package.

Chef-branded binstubs for chef-client.

%description   -n gem-chef-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-bin.
%endif


%package       -n gem-chef-utils
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby >= 2.6
Requires:      gem(chef-utils) >= 0
Requires:      gem(concurrent-ruby) >= 0
Provides:      chef-utils = %EVR
Provides:      gem(chef-utils) = 19.1.176

%description   -n gem-chef-utils
Basic utility functions for Core Chef Infra development


%if_enabled    doc
%package       -n gem-chef-utils-doc
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-utils
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-utils) = 19.1.176

%description   -n gem-chef-utils-doc
Clients for the chef systems integration framework documentation files.

Basic utility functions for Core Chef Infra development

%description   -n gem-chef-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-utils.
%endif


%if_enabled    devel
%package       -n gem-chef-utils-devel
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-utils
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-utils) = 19.1.176
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0

%description   -n gem-chef-utils-devel
Clients for the chef systems integration framework development package.

Basic utility functions for Core Chef Infra development

%description   -n gem-chef-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-utils.
%endif


%package       -n gem-chef-config
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby >= 2.6
Requires:      gem(addressable) >= 0
Requires:      gem(chef-config) >= 0
Requires:      gem(chef-utils) = 19.1.176
Requires:      gem(fuzzyurl) >= 0
Requires:      gem(mixlib-config) >= 2.2.12
Requires:      gem(mixlib-shellout) >= 2.0
Requires:      gem(racc) >= 0
Requires:      gem(tomlrb) >= 1.2
Conflicts:     gem(mixlib-config) >= 4.0
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(tomlrb) >= 3
Provides:      gem(chef-config) = 19.1.176

%description   -n gem-chef-config
Chef's default configuration and config loading.


%if_enabled    doc
%package       -n gem-chef-config-doc
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-config
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-config) = 19.1.176

%description   -n gem-chef-config-doc
Clients for the chef systems integration framework documentation files.

Chef's default configuration and config loading.

%description   -n gem-chef-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-config.
%endif


%if_enabled    devel
%package       -n gem-chef-config-devel
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-config
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-config) = 19.1.176
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0

%description   -n gem-chef-config-devel
Clients for the chef systems integration framework development package.

Chef's default configuration and config loading.

%description   -n gem-chef-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-config.
%endif


%if_enabled    doc
%package       -n gem-chef-doc
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef) = 19.1.176

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
%endif


%if_enabled    devel
%package       -n gem-chef-devel
Version:       19.1.176
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef) = 19.1.176
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Conflicts:     gem(crack) >= 0.4.6

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
%endif


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
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-knife
%doc LICENSE
%ruby_gemspecdir/knife-19.1.176.gemspec
%ruby_gemslibdir/knife-19.1.176

%files         -n knife
%doc LICENSE
%_bindir/knife

%if_enabled    doc
%files         -n gem-knife-doc
%doc LICENSE
%ruby_gemsdocdir/knife-19.1.176
%endif

%if_enabled    devel
%files         -n gem-knife-devel
%doc LICENSE
%endif

%files         -n gem-chef-bin
%doc LICENSE
%ruby_gemspecdir/chef-bin-19.1.176.gemspec
%ruby_gemslibdir/chef-bin-19.1.176

%files         -n chef
%doc LICENSE
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

%if_enabled    doc
%files         -n gem-chef-bin-doc
%doc LICENSE
%ruby_gemsdocdir/chef-bin-19.1.176
%endif

%if_enabled    devel
%files         -n gem-chef-bin-devel
%doc LICENSE
%endif

%files         -n gem-chef-utils
%doc LICENSE README.md
%ruby_gemspecdir/chef-utils-19.1.176.gemspec
%ruby_gemslibdir/chef-utils-19.1.176

%if_enabled    doc
%files         -n gem-chef-utils-doc
%doc LICENSE README.md
%ruby_gemsdocdir/chef-utils-19.1.176
%endif

%if_enabled    devel
%files         -n gem-chef-utils-devel
%doc LICENSE README.md
%endif

%files         -n gem-chef-config
%doc LICENSE
%ruby_gemspecdir/chef-config-19.1.176.gemspec
%ruby_gemslibdir/chef-config-19.1.176

%if_enabled    doc
%files         -n gem-chef-config-doc
%doc LICENSE
%ruby_gemsdocdir/chef-config-19.1.176
%endif

%if_enabled    devel
%files         -n gem-chef-config-devel
%doc LICENSE
%endif

%if_enabled    doc
%files         -n gem-chef-doc
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-devel
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Sat May 30 2026 Pavel Skrylev <majioa@altlinux.org> 19.1.176-alt1
- ^ 19.1.116 -> 19.1.176

* Mon Mar 30 2026 Pavel Skrylev <majioa@altlinux.org> 19.1.116-alt1.2
- ! fixed spec and deps to chef-zero

* Sun Mar 22 2026 Pavel Skrylev <majioa@altlinux.org> 19.1.116-alt1.1
- ! fixed spec to filter out kitchen-tests source

* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 19.1.116-alt1
- ^ 19.0.85 -> 19.1.116
- * fixed cheatingly dep to train-core decreasing it to 3.11.5

* Wed Nov 05 2025 Pavel Skrylev <majioa@altlinux.org> 19.0.85-alt1
- ^ 19.0.43 -> 19.0.85

* Mon Oct 28 2024 Pavel Skrylev <majioa@altlinux.org> 19.0.43-alt1
- ^ 18.4.59 -> 19.0.43

* Mon Aug 05 2024 Pavel Skrylev <majioa@altlinux.org> 18.4.59-alt1
- ^ 18.3.58 -> 18.4.59

* Mon Dec 04 2023 Pavel Skrylev <majioa@altlinux.org> 18.3.58-alt1
- ^ 18.1.32 -> 18.3.58

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
