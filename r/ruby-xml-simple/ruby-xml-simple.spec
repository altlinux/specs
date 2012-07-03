%define pkgname xml-simple

Name: ruby-%pkgname
Version: 1.0.12
Release: alt1
Summary: A very simple API for XML processing
License: Ruby license
Group: Development/Ruby
Url: http://rubyforge.org/projects/xml-simple/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Mar 31 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Class XmlSimple offers an easy API to read and write XML. It is
a Ruby translation of Grant McLean's Perl module XML::Simple.
Simply put, it automatically converts XML documents into a Ruby
Hash.

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

%install
%ruby_install
%rdoc lib/

%files
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/XmlSimple*

%changelog
* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.12-alt1
- [1.0.12]

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 1.0.11-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 1.0.11-alt1
- Initial build for ALT Linux

