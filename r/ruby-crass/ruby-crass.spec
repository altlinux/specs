%define  pkgname crass

Name:    ruby-%pkgname
Version: 1.0.4
Release: alt2

Summary: A Ruby CSS parser that's fully compliant with the CSS Syntax Level 3 specification.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rgrove/crass/

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-build-python3
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%add_python3_path %rubygem_gemdir/%pkgname-%version/test/css-parsing-tests/

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
* Tue May 04 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- FTBFS: Set correct python3 library directory for python scripts.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
