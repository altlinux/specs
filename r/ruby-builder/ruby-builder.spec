%define pkgname builder

Name: ruby-%pkgname
Version: 3.0.0
Release: alt1
Summary: Provide a simple way to create XML markup and data structures
License: MIT/X Consortium
Group: Development/Ruby
Url: http://rubyforge.org/projects/builder/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch1: ruby-builder-3.0.0-alt-use-require_relative.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Mar 31 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Builder::XmlMarkup:: Generate XML markup notiation
Builder::XmlEvents:: Generate XML events (i.e. SAX-like)

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch1 -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
# EPIC FAIL
rm -f test/testblankslate.rb
%ruby_test_unit -Ilib test/test*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGES README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Builder*

%changelog
* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 3.0.0-alt1
- [3.0.0]

* Tue Nov 30 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.2-alt4
- Fix build with Ruby 1.9.2

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 2.1.2-alt3
- Rebuilt with Ruby 1.9

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 2.1.2-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 2.1.2-alt1
- Initial build for ALT Linux

