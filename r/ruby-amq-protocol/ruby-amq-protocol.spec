%define  pkgname amq-protocol

Name: 	 ruby-%pkgname
Version: 2.3.0
Release: alt1

Summary: AMQP 0.9.1 protocol serialization and deserialization implementation for Ruby (2.0+)
License: MIT
Group:   Development/Ruby
Url:     http://github.com/ruby-amqp/amq-protocol

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

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
Initial build for Sisyphus
