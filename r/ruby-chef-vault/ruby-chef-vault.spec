%define  pkgname chef-vault

Name:    ruby-%pkgname
Version: 3.4.2
Release: alt1

Summary: Securely manage passwords, certs, and other secrets in Chef
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/chef/chef-vault

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

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
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus
