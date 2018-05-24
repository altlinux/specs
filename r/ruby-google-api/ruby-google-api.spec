%define  pkgname google-api-ruby-client

Name:    ruby-google-api
Version: 0.21.2
Release: alt1

Summary: Google API Client for Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/google/google-api-ruby-client

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(java\|rails/d

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
cp -a generated/* %buildroot%ruby_sitelibdir/
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md
%_bindir/generate-api
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.21.2-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt1
- Initial build for Sisyphus
