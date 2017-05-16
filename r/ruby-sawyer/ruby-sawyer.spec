%define  pkgname sawyer

Name: 	 ruby-%pkgname
Version: 0.8.1 
Release: alt1

Summary: Secret User Agent of HTTP
License: MIT
Group:   Development/Ruby
Url:     https://github.com/lostisland/sawyer

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Sawyer is an experimental hypermedia agent for Ruby built on top of Faraday.

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
* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.8.1-alt1
- Initial build in Sisyphus
