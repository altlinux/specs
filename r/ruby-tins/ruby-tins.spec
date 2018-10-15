%define  pkgname tins

Name:    ruby-%pkgname
Version: 1.17.0
Release: alt1

Summary: This Is Not Spruz
License: MIT
Group:   Development/Ruby
Url:     https://github.com/flori/tins

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
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- New version.

* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.3-alt1
- Initial build for Sisyphus
