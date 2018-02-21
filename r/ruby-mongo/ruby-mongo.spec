%define  pkgname mongo-ruby-driver

Name: 	 ruby-mongo
Version: 2.5.1
Release: alt1

Summary: Ruby driver for MongoDB
License: Apache-2.0
Group:   Development/Ruby
Url:     http://www.mongodb.org/

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
%_bindir/mongo_console
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Feb 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- New version.

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- Initial build for Sisyphus
