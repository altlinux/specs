%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef

Name:          gem-chef
Version:       19.4.12
Release:       alt1.1
Summary:       Clients for the chef systems integration framework
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://www.chef.io
Vcs:           https://github.com/chef/chef.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       chef-client.init
Source2:       chef-client.service
Source3:       chef-client.sysconfig
Source4:       chef-client.rb
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(aws-sdk-s3) >= 1.91
BuildRequires: gem(aws-sdk-secretsmanager) >= 1.46
BuildRequires: gem(bcrypt_pbkdf) >= 1.0
BuildRequires: gem(chef-licensing) >= 1.3
BuildRequires: gem(chef-vault) >= 0
BuildRequires: gem(chef-zero) >= 15.1.0
BuildRequires: gem(cheffish) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.3.7
BuildRequires: gem(corefoundation) >= 0.3.14
BuildRequires: gem(crack) >= 1.0.1
BuildRequires: gem(csv) >= 3.3.5
BuildRequires: gem(diff-lcs) >= 1.6.0
BuildRequires: gem(ed25519) >= 1.2
BuildRequires: gem(erubis) >= 2.7
BuildRequires: gem(fauxhai-ng) >= 0
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(ffi-libarchive) >= 1.0
BuildRequires: gem(ffi-yajl) >= 2.2
BuildRequires: gem(fuzzyurl) >= 0
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
BuildRequires: gem(ohai) >= 18.1.16
BuildRequires: gem(openssl) >= 3.0.0
BuildRequires: gem(plist) >= 3.2
BuildRequires: gem(proxifier2) >= 1.1
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(repl_type_completor) >= 0.1.15
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(syslog) >= 0
BuildRequires: gem(syslog-logger) >= 1.6
BuildRequires: gem(tomlrb) >= 1.2
BuildRequires: gem(train-core) >= 3.11.1
BuildRequires: gem(train-rest) >= 0.4.1
BuildRequires: gem(train-winrm) >= 0.2.13
BuildRequires: gem(unf_ext) >= 0.0.9.1
BuildRequires: gem(uri) >= 1.0.4
BuildRequires: gem(vault) >= 0.18.2
BuildRequires: gem(webmock) >= 0
BuildConflicts: gem(aws-sdk-s3) >= 2
BuildConflicts: gem(aws-sdk-secretsmanager) >= 2
BuildConflicts: gem(bcrypt_pbkdf) >= 2
BuildConflicts: gem(chef-licensing) >= 2
BuildConflicts: gem(chef-zero) >= 15.2
BuildConflicts: gem(corefoundation) >= 1
BuildConflicts: gem(crack) >= 1.1
BuildConflicts: gem(csv) >= 3.4
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(ed25519) >= 2
BuildConflicts: gem(erubis) >= 3
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(ffi-yajl) >= 4.0
BuildConflicts: gem(iniparse) >= 2
BuildConflicts: gem(inspec-core) >= 7.2
BuildConflicts: gem(license-acceptance) >= 3
BuildConflicts: gem(mixlib-archive) >= 2.0
BuildConflicts: gem(mixlib-authentication) >= 4
BuildConflicts: gem(mixlib-cli) >= 3.0
BuildConflicts: gem(mixlib-config) >= 4.0
BuildConflicts: gem(mixlib-log) >= 4.0
BuildConflicts: gem(mixlib-shellout) >= 3.5.0
BuildConflicts: gem(net-sftp) >= 5.0
BuildConflicts: gem(ohai) >= 20
BuildConflicts: gem(openssl) >= 4
BuildConflicts: gem(plist) >= 4
BuildConflicts: gem(proxifier2) >= 2
BuildConflicts: gem(repl_type_completor) >= 0.2
BuildConflicts: gem(syslog-logger) >= 2
BuildConflicts: gem(tomlrb) >= 3
BuildConflicts: gem(unf_ext) >= 1
BuildConflicts: gem(uri) >= 1.2.0
BuildConflicts: gem(vault) >= 0.21.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency unf_ext >= 0.0.9.1,unf_ext < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency openssl >= 3.0.0,openssl < 4
%ruby_use_gem_dependency addressable >= 2.8.0,addressable < 3
%ruby_use_gem_dependency train-winrm >= 0.2.13,train-winrm < 1
%ruby_use_gem_dependency train-core >= 3.11.1,train-core < 4
%ruby_use_gem_dependency ohai >= 18.1.16,ohai < 20
%ruby_use_gem_dependency inspec-core >= 6.2.9,inspec-core < 7
%ruby_use_gem_dependency corefoundation >= 0.3.14,corefoundation < 1
%ruby_use_gem_dependency ffi-libarchive >= 1.1.13,ffi-libarchive < 2
%ruby_use_gem_dependency ffi >= 1.17.0,ffi < 2
%ruby_use_gem_dependency diff-lcs >= 2.0,diff-lcs < 3
Requires:      ruby >= 3.1.0
Requires:      gem(addressable) >= 2.8.0
Requires:      gem(aws-sdk-s3) >= 1.91
Requires:      gem(aws-sdk-secretsmanager) >= 1.46
Requires:      gem(bcrypt_pbkdf) >= 1.0
Requires:      gem(chef-licensing) >= 1.3
Requires:      gem(chef-vault) >= 0
Requires:      gem(chef-zero) >= 15.1.0
Requires:      gem(cheffish) >= 0
Requires:      gem(corefoundation) >= 0.3.14
Requires:      gem(csv) >= 3.3.5
Requires:      gem(diff-lcs) >= 1.6.0
Requires:      gem(ed25519) >= 1.2
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
Requires:      gem(openssl) >= 3.0.0
Requires:      gem(plist) >= 3.2
Requires:      gem(proxifier2) >= 1.1
Requires:      gem(repl_type_completor) >= 0.1.15
Requires:      gem(rest-client) >= 0
Requires:      gem(syslog) >= 0
Requires:      gem(syslog-logger) >= 1.6
Requires:      gem(train-core) >= 3.11.1
Requires:      gem(train-rest) >= 0.4.1
Requires:      gem(train-winrm) >= 0.2.13
Requires:      gem(unf_ext) >= 0.0.9.1
Requires:      gem(uri) >= 1.0.4
Requires:      gem(vault) >= 0.18.2
Conflicts:     gem(aws-sdk-s3) >= 2
Conflicts:     gem(aws-sdk-secretsmanager) >= 2
Conflicts:     gem(bcrypt_pbkdf) >= 2
Conflicts:     gem(chef-licensing) >= 2
Conflicts:     gem(chef-zero) >= 15.2
Conflicts:     gem(corefoundation) >= 1
Conflicts:     gem(csv) >= 3.4
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(ed25519) >= 2
Conflicts:     gem(erubis) >= 3
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(ffi-yajl) >= 4.0
Conflicts:     gem(iniparse) >= 2
Conflicts:     gem(inspec-core) >= 7.2
Conflicts:     gem(license-acceptance) >= 3
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(mixlib-authentication) >= 4
Conflicts:     gem(mixlib-cli) >= 3.0
Conflicts:     gem(mixlib-log) >= 4.0
Conflicts:     gem(mixlib-shellout) >= 3.5.0
Conflicts:     gem(net-sftp) >= 5.0
Conflicts:     gem(ohai) >= 20
Conflicts:     gem(openssl) >= 4
Conflicts:     gem(plist) >= 4
Conflicts:     gem(proxifier2) >= 2
Conflicts:     gem(repl_type_completor) >= 0.2
Conflicts:     gem(syslog-logger) >= 2
Conflicts:     gem(unf_ext) >= 1
Conflicts:     gem(uri) >= 2
Conflicts:     gem(vault) >= 0.19
Obsoletes:     chef-doc < %EVR
Provides:      chef-doc = %EVR
Provides:      gem(chef) = 19.4.12

%ruby_ignore_names kitchen-tests

%description
Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.


%package       -n gem-chef-bin
Version:       19.4.12
Release:       alt1.1
Summary:       Chef-branded binstubs for chef-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 19.4.12
Requires:      gem(chef-bin) >= 0
Provides:      gem(chef-bin) = 19.4.12

%description   -n gem-chef-bin
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


%package       -n chef
Version:       19.4.12
Release:       alt1.1
Summary:       Chef-branded binstubs for chef-client executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef-bin
Group:         Other
BuildArch:     noarch

Requires:      gem(chef-bin) = 19.4.12

%description   -n chef
Chef-branded binstubs for chef-client executable(s).

A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%description   -n chef -l ru_RU.UTF-8
Исполнямка для самоцвета chef-bin.


%if_enabled    doc
%package       -n gem-chef-bin-doc
Version:       19.4.12
Release:       alt1.1
Summary:       Chef-branded binstubs for chef-client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-bin) = 19.4.12

%description   -n gem-chef-bin-doc
Chef-branded binstubs for chef-client documentation files.

A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%description   -n gem-chef-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-bin.
%endif


%if_enabled    devel
%package       -n gem-chef-bin-devel
Version:       19.4.12
Release:       alt1.1
Summary:       Chef-branded binstubs for chef-client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-bin) = 19.4.12
Requires:      gem(rake) >= 12.3.3

%description   -n gem-chef-bin-devel
Chef-branded binstubs for chef-client development package.

A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%description   -n gem-chef-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-bin.
%endif


%package       -n gem-chef-utils
Version:       19.4.12
Release:       alt1.1
Summary:       Basic utility functions for Core Chef Infra development
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.6
Requires:      gem(chef-utils) >= 0
Requires:      gem(concurrent-ruby) >= 1.3.7
Provides:      gem(chef-utils) = 19.4.12

%description   -n gem-chef-utils
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


%if_enabled    doc
%package       -n gem-chef-utils-doc
Version:       19.4.12
Release:       alt1.1
Summary:       Basic utility functions for Core Chef Infra development documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-utils) = 19.4.12

%description   -n gem-chef-utils-doc
Basic utility functions for Core Chef Infra development documentation files.

A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%description   -n gem-chef-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-utils.
%endif


%if_enabled    devel
%package       -n gem-chef-utils-devel
Version:       19.4.12
Release:       alt1.1
Summary:       Basic utility functions for Core Chef Infra development development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-utils) = 19.4.12
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0

%description   -n gem-chef-utils-devel
Basic utility functions for Core Chef Infra development development package.

A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%description   -n gem-chef-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-utils.
%endif


%package       -n gem-chef-config
Version:       19.4.12
Release:       alt1.1
Summary:       Chef Infra's default configuration and config loading library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.6
Requires:      gem(addressable) >= 2.9.0
Requires:      gem(chef-config) >= 0
Requires:      gem(chef-utils) = 19.4.12
Requires:      gem(fuzzyurl) >= 0
Requires:      gem(mixlib-config) >= 2.2.12
Requires:      gem(mixlib-shellout) >= 2.0
Requires:      gem(racc) >= 0
Requires:      gem(tomlrb) >= 1.2
Conflicts:     gem(mixlib-config) >= 4.0
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(tomlrb) >= 3.0
Provides:      gem(chef-config) = 19.4.12

%description   -n gem-chef-config
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


%if_enabled    doc
%package       -n gem-chef-config-doc
Version:       19.4.12
Release:       alt1.1
Summary:       Chef Infra's default configuration and config loading library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-config) = 19.4.12

%description   -n gem-chef-config-doc
Chef Infra's default configuration and config loading library documentation
files.

A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%description   -n gem-chef-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-config.
%endif


%if_enabled    devel
%package       -n gem-chef-config-devel
Version:       19.4.12
Release:       alt1.1
Summary:       Chef Infra's default configuration and config loading library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-config) = 19.4.12
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0

%description   -n gem-chef-config-devel
Chef Infra's default configuration and config loading library development
package.

A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

%description   -n gem-chef-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-config.
%endif


%if_enabled    doc
%package       -n gem-chef-doc
Version:       19.4.12
Release:       alt1.1
Summary:       A systems integration framework, built to bring the benefits of configuration management to your entire infrastructure documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef) = 19.4.12

%description   -n gem-chef-doc
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure documentation files.

%description   -n gem-chef-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef.
%endif


%if_enabled    devel
%package       -n gem-chef-devel
Version:       19.4.12
Release:       alt1.1
Summary:       A systems integration framework, built to bring the benefits of configuration management to your entire infrastructure development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 19.4.12
Requires:      gem(crack) >= 1.0.1
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Conflicts:     gem(crack) >= 1.1

%description   -n gem-chef-devel
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure development package.

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

%files         -n gem-chef-bin
%doc LICENSE
%ruby_gemspecdir/chef-bin-19.4.12.gemspec
%ruby_gemslibdir/chef-bin-19.4.12

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
%ruby_gemsdocdir/chef-bin-19.4.12
%endif

%if_enabled    devel
%files         -n gem-chef-bin-devel
%doc LICENSE
%endif

%files         -n gem-chef-utils
%doc LICENSE README.md
%ruby_gemspecdir/chef-utils-19.4.12.gemspec
%ruby_gemslibdir/chef-utils-19.4.12

%if_enabled    doc
%files         -n gem-chef-utils-doc
%doc LICENSE README.md
%ruby_gemsdocdir/chef-utils-19.4.12
%endif

%if_enabled    devel
%files         -n gem-chef-utils-devel
%doc LICENSE README.md
%endif

%files         -n gem-chef-config
%doc LICENSE
%ruby_gemspecdir/chef-config-19.4.12.gemspec
%ruby_gemslibdir/chef-config-19.4.12

%if_enabled    doc
%files         -n gem-chef-config-doc
%doc LICENSE
%ruby_gemsdocdir/chef-config-19.4.12
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
* Fri Aug 14 2026 Pavel Skrylev <majioa@altlinux.org> 19.4.12-alt1.1
- ! fixed dep to ohai gem

* Wed Aug 12 2026 Pavel Skrylev <majioa@altlinux.org> 19.4.12-alt1
- ^ 19.1.176 -> 19.4.12

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
