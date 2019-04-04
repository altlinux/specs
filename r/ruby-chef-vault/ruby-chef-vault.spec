%define        pkgname chef-vault

Name:          ruby-%pkgname
Version:       3.4.5
Release:       alt1
Summary:       Securely manage passwords, certs, and other secrets in Chef
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-vault
# VCS:         https://github.com/chef/chef-vault.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Gem that allows you to encrypt a Chef Data Bag Item using the public keys of
a list of chef nodes. This allows only those chef nodes to decrypt the encrypted
values.

For a more detailed explanation of how chef-vault works, please refer to this
blog post Chef Vault - what is it and what can it do for you? by
Nell Shamrell-Harrington.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
Executable files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/%pkgname

%changelog
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
