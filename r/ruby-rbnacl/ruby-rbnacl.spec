%define  pkgname rbnacl

Name: 	 ruby-%pkgname
Version: 5.0.0 
Release: alt1

Summary: Ruby binding to the Networking and Cryptography (NaCl) library
License: MIT
Group:   Development/Ruby
Url:     https://github.com/cryptosphere/rbnacl

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
