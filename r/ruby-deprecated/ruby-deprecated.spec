# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname deprecated

Name: ruby-%pkgname
Version: 2.0.1
Release: alt2

Summary: Easy way to handle deprecating and conditionally running deprecated code
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/deprecated/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun Aug 31 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
An easy way to handle deprecating and conditionally running
deprecated code.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib test/deprecated.rb

%install
%ruby_install
%rdoc lib/

%files
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Deprecated*

%changelog
* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.1-alt2
- Rebuilt with Ruby 1.9

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 2.0.1-alt1
- Built for Sisyphus

