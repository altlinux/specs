%define  pkgname qunit-selenium

Name:    ruby-%pkgname
Version: 0.0.4
Release: alt1

Summary: QUnit test runner for Selenium WebDriver
License: MIT
Group:   Development/Ruby
Url:     https://github.com/smontanari/qunit-selenium

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
%_bindir/qunit-selenium
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1
- Initial build for Sisyphus
