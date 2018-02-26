# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname warden_strategies

Name: ruby-%pkgname
Version: 0.0.0.0.20100301
Release: alt1

Summary: A collection of strategies for Warden
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/tundraghost/warden_strategies

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: ruby-%pkgname-%version.tar

# Automatically added by buildreq on Mon Mar 01 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup ruby-warden

%description
A collection of warden strategies.

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


%files
%doc README.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/WardenStrategies

%changelog
* Mon Mar 01 2010 Timur Batyrshin <erthad@altlinux.org> 0.0.0.0.20100301-alt1
- Built for Sisyphus

