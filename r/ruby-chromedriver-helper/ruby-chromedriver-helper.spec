%define  pkgname chromedriver-helper

Name:    ruby-%pkgname
Version: 2.1.0
Release: alt1

Summary: Easy installation and use of chromedriver, the Chromium project's selenium webdriver adapter. 
License: MIT
Group:   Development/Ruby
Url:     https://github.com/flavorjones/chromedriver-helper

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
* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
