%define        gemname vault

Name:          gem-vault
Version:       0.16.0
Release:       alt1
Summary:       Vault is a Ruby API client for interacting with a Vault server
License:       MPL-2.0
Group:         Development/Ruby
Url:           https://github.com/hashicorp/vault-ruby
Vcs:           https://github.com/hashicorp/vault-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(aws-sigv4) >= 0
BuildRequires: gem(bundler) >= 2 gem(bundler) < 3
BuildRequires: gem(pry) >= 0.13.1 gem(pry) < 1
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.5 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.9.24 gem(yard) < 0.10
BuildRequires: gem(webmock) >= 3.8.3 gem(webmock) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(aws-sigv4) >= 0
Provides:      gem(vault) = 0.16.0


%description
Vault is a Ruby API client for interacting with a Vault server.


%package       -n gem-vault-doc
Version:       0.16.0
Release:       alt1
Summary:       Vault is a Ruby API client for interacting with a Vault server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vault
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vault) = 0.16.0

%description   -n gem-vault-doc
Vault is a Ruby API client for interacting with a Vault server documentation
files.

%description   -n gem-vault-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vault.


%package       -n gem-vault-devel
Version:       0.16.0
Release:       alt1
Summary:       Vault is a Ruby API client for interacting with a Vault server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vault
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vault) = 0.16.0
Requires:      gem(bundler) >= 2 gem(bundler) < 3
Requires:      gem(pry) >= 0.13.1 gem(pry) < 1
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.5 gem(rspec) < 4
Requires:      gem(yard) >= 0.9.24 gem(yard) < 0.10
Requires:      gem(webmock) >= 3.8.3 gem(webmock) < 4

%description   -n gem-vault-devel
Vault is a Ruby API client for interacting with a Vault server development
package.

%description   -n gem-vault-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vault.


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

%files         -n gem-vault-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-vault-devel
%doc README.md


%changelog
* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.16.0-alt1
- + packaged gem with Ruby Policy 2.0
