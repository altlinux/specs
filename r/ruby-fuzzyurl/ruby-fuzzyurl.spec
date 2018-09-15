%define  pkgname fuzzyurl.rb

Name:    ruby-fuzzyurl
Version: 0.9.0
Release: alt2.1

Summary: A Ruby Gem for non-strict parsing, manipulation, and wildcard matching of URLs.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/gamache/fuzzyurl.rb

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
#%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt2.1
- Rebuild for new Ruby autorequirements.

* Wed Jul 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.9.0-alt2
- Tests disabled because "coveralls" is not available

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
