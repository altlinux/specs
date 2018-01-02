%define  pkgname amqp

Name: 	 ruby-%pkgname
Version: 1.8.0
Release: alt1

Summary: EventMachine-based RabbitMQ client. Prefer Bunny: http://rubybunny.info. See documentation guides at http://rubyamqp.info.
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://rubyamqp.info

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
rm -rf %buildroot%_bindir

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jan 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
Initial build for Sisyphus
