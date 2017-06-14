%define  pkgname mustermann

Name: 	 ruby-%pkgname
Version: 1.0.0 
Release: alt1

Summary: Your personal string matching expert
License: MIT
Group:   Development/Ruby
Url:     https://github.com/sinatra/mustermann

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
cd %pkgname
%update_setup_rb

%build
cd %pkgname
%ruby_config
%ruby_build

%install
cd %pkgname
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
* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
