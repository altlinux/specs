%define  pkgname cheffish

Name:    ruby-%pkgname
Version: 14.0.1
Release: alt1

Summary: Resources and tools for testing and interacting with Chef and Chef Server.
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/chef/cheffish

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(openssl_pkcs8)/d

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
* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- Initial build for Sisyphus
