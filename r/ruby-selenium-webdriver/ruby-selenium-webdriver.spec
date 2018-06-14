%define  pkgname selenium-webdriver

Name:    ruby-%pkgname
Version: 3.12.0
Release: alt1

Summary: WebDriver is a tool for writing automated tests of websites
License: Apache 2.0
Group:   Development/Ruby
Url:     https://github.com/SeleniumHQ/selenium

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(win32/d

%description
WebDriver is a tool for writing automated tests of websites. It aims to
mimic the behaviour of a real user, and as such interacts with the HTML
of the application.

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

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.12.0-alt1
- Initial build for Sisyphus
