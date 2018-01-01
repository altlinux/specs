%define  pkgname azure-core

Name: 	 ruby-%pkgname
Version: 0.1.14
Release: alt1

Summary: Azure Ruby SDK Service Management Core HTTP
License: Apache 2.0
Group:   Development/Ruby
Url:     https://github.com/Azure/azure-ruby-asm-core

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  azure-ruby-asm-core-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
This project provides a Ruby package with core functionality consumed by
Azure SDK gems.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n azure-ruby-asm-core-%version
rm -f lib/azure/core/auth/authorizer.rb
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
* Mon Jan 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.14-alt1
- New version.

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.12-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.11-alt1
- Initial build for Sisyphus
