%define  pkgname google-auth-library-ruby

Name:    ruby-google-auth
Version: 0.7.0
Release: alt1

Summary: Google Auth Library for Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/google/google-auth-library-ruby

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
* Wed Oct 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- bump to 0.7.0

* Tue Sep 04 2018 Pavel Skrylev <majioa@altlinux.org> 0.6.6-alt1
- bump to 0.6.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
