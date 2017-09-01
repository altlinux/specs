%define  pkgname zendesk_api

Name: 	 ruby-%pkgname
Version: 1.14.4 
Release: alt1

Summary: Official Ruby Zendesk API Client
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/zendesk/zendesk_api_client_rb

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
* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 1.14.4-alt1
- Initial build for Sisyphus.
