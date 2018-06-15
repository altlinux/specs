%define  pkgname sucker_punch

Name:    ruby-sucker-punch
Version: 2.0.4
Release: alt1

Summary: Sucker Punch is a Ruby asynchronous processing library using concurrent-ruby, heavily influenced by Sidekiq and girl_friday.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/brandonhilkert/sucker_punch

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
# For tests
BuildRequires: ruby-concurrent-ruby
BuildRequires: ruby-pry

Provides: ruby-%pkgname = %EVR

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
* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
