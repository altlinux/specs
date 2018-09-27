%define  pkgname secure_headers

Name:    ruby-secure-headers
Version: 6.0.0
Release: alt2

Summary: Manages application of security headers with many safe defaults
License: MIT
Group:   Development/Ruby
Url:     https://github.com/twitter/secureheaders

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
* Wed Sep 26 2018 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt2
- Bump to v6.0.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.0.5-alt1
- Downgrade to 5.0.5 for foreman.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- Initial build for Sisyphus
