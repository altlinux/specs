%define  pkgname licensee

Name:    ruby-%pkgname
Version: 9.9.4
Release: alt1

Summary: A Ruby Gem to detect under what license a project is distributed.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/benbalter/licensee

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
%doc docs/README*
%_bindir/%pkgname
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 9.9.4-alt1
- New version.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 9.9.1-alt1
- New version.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 9.8.0-alt1
- Initial build for Sisyphus
