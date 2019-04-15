%define pkgname memcache-client

Name: ruby-%pkgname
Version: 1.7.8
Release: alt1
Summary: Ruby client for Danga Interactive's memcached
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/seattlerb/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar

Patch1: remove_require_to_continuum_native.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jul 08 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-flexmock ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-test-unit

%description
memcache-client is a client for Danga Interactive's memcached.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -n %pkgname-%version
%patch1 -p2
# Useless crap.
rm -f lib/continuum_native.rb

%build
%gem_build

%install
%gem_install

%files
%doc History.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Mon Apr 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.8-alt1
- Update to 1.7.8
- Move to the new scheme

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1.2
- Rebuild with Ruby 2.4.1

* Sat Dec 08 2012 Led <led@altlinux.ru> 1.7.4-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.7.4-alt1
- [1.7.4]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 1.5.0-alt1
- Built for Sisyphus

