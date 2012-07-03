# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname ruby-net-ldap

Name: %pkgname
Version: 1.1.0
Release: alt1

Summary: Pure Ruby LDAP library
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/roryo/ruby-net-ldap/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar

# Automatically added by buildreq on Mon Sep 13 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Pure Ruby LDAP library

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/


%check
%ruby_test_unit -Ilib:test test/

%files
%doc README.txt Hacking.rdoc History.txt LICENSE
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/net/snmp.rb

%files doc
%ruby_ri_sitedir/Net/LD*
%ruby_ri_sitedir/Net/BER

%changelog
* Mon Sep 13 2010 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- Built for Sisyphus

