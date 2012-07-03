%define ruby_major 1.8
%define pkgname memcache-client

Name: ruby%{ruby_major}-%pkgname
Version: 1.7.4
Release: alt2
Summary: Ruby client for Danga Interactive's memcached
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/seattlerb/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jul 08 2008 (-bi)
BuildRequires: ruby%{ruby_major} rpm-build-ruby ruby%{ruby_major}-flexmock ruby%{ruby_major}-tool-rdoc ruby-tool-setup

%description
memcache-client is a client for Danga Interactive's memcached.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb
# Useless crap.
rm -f lib/continuum_native.rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib test/

%install
%ruby_install
%rdoc lib/

%files
%doc History.rdoc README.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/MemCache*

%changelog
* Wed Apr 13 2011 Timur Aitov <timonbl4@altlinux.org> 1.7.4-alt2
- Rebuild for ruby1.8

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.7.4-alt1
- [1.7.4]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 1.5.0-alt1
- Built for Sisyphus

