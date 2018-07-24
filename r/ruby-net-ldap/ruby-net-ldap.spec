# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname ruby-net-ldap

Name: %pkgname
Version: 0.16.1
Release: alt1
Epoch: 1

Summary: Pure Ruby LDAP library
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/roryo/ruby-net-ldap/

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Pure Ruby LDAP library

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
#%%ruby_test_unit -Ilib:test test/

%files
%doc *.rdoc
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/Net/LD*
%ruby_ri_sitedir/Net/BER

%changelog
* Thu Jul 19 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.16.1-alt1
- New version.
- Disable tests.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 21 2014 Led <led@altlinux.ru> 1.1.0-alt1.2
- fixed tests

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Sep 13 2010 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- Built for Sisyphus

