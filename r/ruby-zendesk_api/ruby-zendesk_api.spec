%define  pkgname zendesk_api

Name: 	 ruby-%pkgname
Version: 1.17.0
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
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Nov 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.15.0-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 1.14.4-alt1
- Initial build for Sisyphus.
