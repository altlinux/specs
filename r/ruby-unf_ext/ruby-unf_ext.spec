Name: 	 ruby-unf_ext
Version: 0.0.7.5
Release: alt1

Summary: Unicode Normalization Form support library for CRuby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/knu/ruby-unf_ext

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: gcc-c++

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup
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
%doc README* CHANGELOG*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.0.M80P.1
- Rebuild with Ruby 2.4.2

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.1
- Rebuild with Ruby 2.4.2

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1
- Initial build for Sisyphus.
