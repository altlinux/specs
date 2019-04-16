%define        pkgname hiredis

Name: 	       ruby-%pkgname
Version:       0.6.3
Release:       alt1
Summary:       Ruby wrapper for hiredis
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://github.com/redis/hiredis-rb
# VCS:         https://github.com/redis/hiredis-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libhiredis-devel

%description
Ruby extension that wraps hiredis. Both the synchronous connection API and
a separate protocol reader are supported. It is primarily intended to speed up
parsing multi bulk replies.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


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

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- Move forward with sourcing from github
- Bump to 0.6.3
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.1
- Rebuild with Ruby 2.5.0

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
