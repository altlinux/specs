%define  pkgname rack-test

Name: 	 ruby-%pkgname
Version: 0.6.3 
Release: alt1

Summary: Rack::Test is a layer on top of Rack's MockRequest similar to Merb's RequestHelper
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rack-test/rack-test

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
* Tue Jun 13 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus
