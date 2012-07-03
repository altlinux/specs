# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname marc

Name: ruby-%pkgname
Version: 0.2.2
Release: alt1

Summary: Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/marc/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun May 10 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

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
for t in test/tc_*.rb; do
  ruby -Ilib -rmarc -rtest/unit "$t"
done

%install
%ruby_install
%rdoc lib/

%files
%doc README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/MARC*

%changelog
* Sun May 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.2-alt1
- Built for Sisyphus

