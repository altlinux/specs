%define  pkgname solve

Name:    ruby-%pkgname
Version: 4.0.0
Release: alt1

Summary: A constraint solver for Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/berkshelf/solve

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(dep_selector)/d

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

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
