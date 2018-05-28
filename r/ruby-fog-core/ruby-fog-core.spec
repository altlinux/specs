%define  pkgname fog-core

Name:    ruby-%pkgname
Version: 2.1.0
Release: alt1

Summary: fog's core, shared behaviors without API and provider specifics
License: MIT
Group:   Development/Ruby
Url:     https://github.com/fog/fog-core

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Shared classes and tests for fog providers and services.

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
* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
