%define  pkgname sprockets-rails

Name:    ruby-%pkgname
Version: 3.2.1
Release: alt2.1

Summary: Sprockets Rails integration
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/sprockets-rails

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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt2.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt2
- Package as gem.
- Disable tests.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus
