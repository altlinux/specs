%define  pkgname hirb-unicode-steakknife

Name:    ruby-%pkgname
Version: 0.0.8
Release: alt1

Summary: Unicode support for hirb
License: MIT
Group:   Development/Ruby
Url:     https://rubygems.org/gems/hirb-unicode-steakknife

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
hirb-unicode fixes the problem that full-width unicode characters is
aligned incorrectly.

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

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.8-alt1
- Initial build in Sisyphus
