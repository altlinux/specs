%define  pkgname loofah

Name:    ruby-%pkgname
Version: 2.2.3
Release: alt1

Summary: HTML/XML manipulation and sanitization based on Nokogiri
License: MIT
Group:   Development/Ruby
Url:     https://github.com/flavorjones/loofah

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

# Adapt gemspec for package
subst 's,\(s\.version\s*=\).*,\1 "%version",' %pkgname.gemspec

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
* Wed Mar 27 2019 Ivan A. Melnikov <iv@altlinux.org> 2.2.3-alt1
- 2.2.3 (CVE-2018-16468);
- fix version in gamespec for packaging (closes: #36441).

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus
