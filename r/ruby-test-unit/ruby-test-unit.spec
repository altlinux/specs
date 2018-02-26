# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname test-unit

Name: ruby-%pkgname
Version: 2.2.0
Release: alt1

Summary: Ruby unit testing framework
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/test-unit/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Obsoletes: ruby-module-test-unit
Provides: ruby-module-test-unit = %version-%release

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Tue May 12 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Test::Unit 2.x - Improved version of Test::Unit bundled in
Ruby 1.8.x.

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
ruby test/run-test.rb

%install
%ruby_install
%rdoc --debug lib/

%files
%doc README.txt History.txt
%_bindir/testrb
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Test*

%changelog
* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 2.2.0-alt1
- [2.2.0]

* Sat Sep 25 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.1-alt1
- [2.1.1]

* Mon Mar 08 2010 Alexey I. Froloff <raorn@altlinux.org> 2.0.6-alt2
- Do not apply excluded conditions to top-level files

* Fri Feb 26 2010 Alexey I. Froloff <raorn@altlinux.org> 2.0.6-alt1
- [2.0.6]

* Mon Jul 06 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.2-alt1.1
- Built for Sisyphus

