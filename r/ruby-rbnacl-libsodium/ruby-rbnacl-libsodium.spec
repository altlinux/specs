%define  pkgname rbnacl-libsodium

Name: 	 ruby-%pkgname
Version: 1.0.16
Release: alt1

Summary: RbNaCl + libsodium packaged as a gem
License: MIT
Group:   Development/Ruby
Url:     https://github.com/cryptosphere/rbnacl-libsodium

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Patch:   dont-rebuild-libsodium.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libsodium-devel

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
%patch -p1
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
* Thu Dec 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.16-alt1
- New version.

* Thu Nov 09 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.15.1-alt1
- New version

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.13-alt1
- Initial build for Sisyphus.
