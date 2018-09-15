# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname marc

Name: ruby-%pkgname
Version: 1.0.2
Release: alt1

Summary: Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/marc/

BuildArch: noarch

Source: %pkgname-%version.tar

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
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
#for t in test/tc_*.rb; do
#  ruby -Ilib -rmarc -rtest/unit "$t"
#done

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/MARC*

%changelog
* Thu Jul 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version.
- Disable tests.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.2
- Rebuild with new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun May 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.2-alt1
- Built for Sisyphus

