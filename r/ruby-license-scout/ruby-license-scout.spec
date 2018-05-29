%define  pkgname license_scout

Name: 	 ruby-license-scout
Version: 1.0.10
Release: alt1

Summary: Discovers license information of the dependencies of a project.
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/chef/license_scout

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
%_bindir/%pkgname
%_bindir/rebar_lock_json
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.10-alt1
- Initial build for Sisyphus
