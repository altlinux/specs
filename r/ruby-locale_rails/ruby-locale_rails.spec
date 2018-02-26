# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname locale_rails

Name: ruby-%pkgname
Version: 2.0.5
Release: alt1

Summary: Ruby-Locale for Ruby on Rails
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/locale/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Wed Oct 14 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-activerecord-sqlite3-adapter ruby-locale ruby-racc-runtime ruby-rails ruby-tool-setup

%description
This library provides some Rails localized functions.

This is useful with Rails i18n backends which doesn't have
auto-detection and some other features includes this library.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb
cp %_datadir/rails/environments/boot.rb test/config/boot.rb

%build
%ruby_config
%ruby_build
pushd test
%rake -I../lib test
popd

%install
%ruby_install

%files
%doc README.rdoc
%ruby_sitelibdir/*

%changelog
* Sun Apr 18 2010 Alexey I. Froloff <raorn@altlinux.org> 2.0.5-alt1
- [2.0.5]

* Wed Oct 14 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt1
- Built for Sisyphus

