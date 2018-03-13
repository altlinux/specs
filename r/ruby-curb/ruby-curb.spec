%define  pkgname curb

Name: 	 ruby-%pkgname
Version: 0.9.4
Release: alt1.3

Summary: Ruby bindings for libcurl
License: MIT/ruby
Group:   Development/Ruby
Url:     https://github.com/taf2/curb

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libcurl-devel

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
* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Leonid Krivoshein <klark@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
