%define        gemname chef-vault

Name:          gem-chef-vault
Version:       4.1.3
Release:       alt1
Summary:       Securely manage passwords, certs, and other secrets in Chef
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-vault
Vcs:           https://github.com/chef/chef-vault.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-chef-vault < %EVR
Provides:      ruby-chef-vault = %EVR
Provides:      gem(chef-vault) = 4.1.3


%description
Gem that allows you to encrypt a Chef Data Bag Item using the public keys of a
list of chef nodes. This allows only those chef nodes to decrypt the encrypted
values.

For a more detailed explanation of how chef-vault works, please refer to this
blog post Chef Vault - what is it and what can it do for you? by Nell
Shamrell-Harrington.


%package       -n chef-vault
Version:       4.1.3
Release:       alt1
Summary:       Securely manage passwords, certs, and other secrets in Chef executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef-vault
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-vault) = 4.1.3

%description   -n chef-vault
Securely manage passwords, certs, and other secrets in Chef executable(s).

Gem that allows you to encrypt a Chef Data Bag Item using the public keys of a
list of chef nodes. This allows only those chef nodes to decrypt the encrypted
values.

For a more detailed explanation of how chef-vault works, please refer to this
blog post Chef Vault - what is it and what can it do for you? by Nell
Shamrell-Harrington.

%description   -n chef-vault -l ru_RU.UTF-8
Исполнямка для самоцвета chef-vault.


%package       -n gem-chef-vault-doc
Version:       4.1.3
Release:       alt1
Summary:       Securely manage passwords, certs, and other secrets in Chef documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-vault
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-vault) = 4.1.3

%description   -n gem-chef-vault-doc
Securely manage passwords, certs, and other secrets in Chef documentation
files.

Gem that allows you to encrypt a Chef Data Bag Item using the public keys of a
list of chef nodes. This allows only those chef nodes to decrypt the encrypted
values.

For a more detailed explanation of how chef-vault works, please refer to this
blog post Chef Vault - what is it and what can it do for you? by Nell
Shamrell-Harrington.

%description   -n gem-chef-vault-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-vault.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n chef-vault
%_bindir/chef-vault

%files         -n gem-chef-vault-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 4.1.3-alt1
- ^ 3.4.5 -> 4.1.3

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.4.5-alt1
- Bump to 3.4.5
- Use Ruby Policy 2.0

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.4.3-alt1
- Bump to 3.4.3.

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus
