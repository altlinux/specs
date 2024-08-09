%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname vault

Name:          gem-vault
Version:       0.18.2
Release:       alt1
Summary:       Vault is a Ruby API client for interacting with a Vault server
License:       MPL-2.0
Group:         Development/Ruby
Url:           https://github.com/hashicorp/vault-ruby
Vcs:           https://github.com/hashicorp/vault-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(yard) >= 0.9.24
BuildRequires: gem(webmock) >= 3.8.3
BuildRequires: gem(webrick) >= 1.5
BuildRequires: gem(aws-sigv4) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(webrick) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(aws-sigv4) >= 0
Provides:      gem(vault) = 0.18.2


%description
Vault is a Ruby API client for interacting with a Vault server.


%if_enabled    doc
%package       -n gem-vault-doc
Version:       0.18.2
Release:       alt1
Summary:       Vault is a Ruby API client for interacting with a Vault server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vault
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vault) = 0.18.2

%description   -n gem-vault-doc
Vault is a Ruby API client for interacting with a Vault server documentation
files.

%description   -n gem-vault-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vault.
%endif


%if_enabled    devel
%package       -n gem-vault-devel
Version:       0.18.2
Release:       alt1
Summary:       Vault is a Ruby API client for interacting with a Vault server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vault
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vault) = 0.18.2
Requires:      gem(bundler) >= 2
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.5
Requires:      gem(yard) >= 0.9.24
Requires:      gem(webmock) >= 3.8.3
Requires:      gem(webrick) >= 1.5
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(webrick) >= 2

%description   -n gem-vault-devel
Vault is a Ruby API client for interacting with a Vault server development
package.

%description   -n gem-vault-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vault.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-vault-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-vault-devel
%doc README.md
%endif


%changelog
* Mon Aug 05 2024 Pavel Skrylev <majioa@altlinux.org> 0.18.2-alt1
- ^ 0.16.0 -> 0.18.2

* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.16.0-alt1
- + packaged gem with Ruby Policy 2.0
