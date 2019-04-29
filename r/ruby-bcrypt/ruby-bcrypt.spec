%define        pkgname bcrypt

Name:          ruby-%pkgname
Version:       3.1.12
Release:       alt2
Summary:       bcrypt-ruby is a Ruby binding for the OpenBSD bcrypt() password hashing algorithm, allowing you to easily store a secure hash of your users' passwords
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/codahale/bcrypt-ruby
# VCS:         https://github.com/codahale/bcrypt-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
Provides:      %pkgname-ruby
Obsoletes:     %pkgname-ruby

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project for hashing passwords. The bcrypt Ruby gem provides a
simple wrapper for safely handling passwords.

%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

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
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Apr 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.12-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.12-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.12-alt1
- Initial build for Sisyphus
