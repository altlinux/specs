%define        pkgname redis

Name:          ruby-%pkgname
Version:       4.1.0
Release:       alt1
Summary:       A Ruby client library for Redis
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/redis/redis-rb
# VCS:         https://github.com/redis/redis-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary.

A Ruby client that tries to match Redis' API one-to-one, while still providing
an idiomatic interface.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
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

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Fri Apr 12 2019 Pavel Skrylev <majioa@altlinux.org> 4.1.0-alt1
- Bump to 4.1.0
- Use Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus
