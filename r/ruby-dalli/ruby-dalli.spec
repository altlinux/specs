%define        pkgname dalli

Name:          ruby-%pkgname
Version:       2.7.10
Release:       alt1
Summary:       High performance memcached client for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/petergoldstein/dalli
# VCS:         https://github.com/petergoldstein/dalli.git
BuildArch:     noarch
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: memcached

%description
Dalli is a high performance pure Ruby client for accessing memcached servers.
It works with memcached 1.4+ only as it uses the newer binary protocol. It
should be considered a replacement for the memcache-client gem.

The name is a variant of Salvador Dali for his famous painting The Persistence
of Memory.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem

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

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.10-alt1
- Use Ruby Policy 2.0
- Bump to 2.7.10

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.6-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.6-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.6-alt1
- Initial build in Sisyphus

