%define  pkgname chef-sugar

Name: 	 ruby-%pkgname
Version: 3.4.0 
Release: alt1

Summary: Chef Sugar is a Gem & Chef Recipe that includes series of helpful sugar of the Chef core and other resources
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/sethvargo/chef-sugar

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Chef Sugar is a Gem & Chef Recipe that includes series of helpful sugar of the
Chef core and other resources to make a cleaner, more lean recipe DSL, enforce
DRY principles, and make writing Chef recipes an awesome experience!

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
* Tue Jun 27 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus
