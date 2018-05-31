%define  pkgname rack-openid

Name:    ruby-%pkgname
Version: 1.4.2
Release: alt1

Summary: Provides a more HTTPish API around the ruby-openid library
License: MIT
Group:   Development/Ruby
Url:     https://github.com/grosser/rack-openid

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
%doc Readme.md
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus (without tests).
