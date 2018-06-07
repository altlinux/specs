Name: ruby-java
Version: 0.0.2
Release: alt2%ubt

Summary: The caffeine boost you need for your late-night coding sprints.
Group: Development/Ruby
License: BSD
Url: https://github.com/vanruby/java

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ruby rpm-build-ubt
BuildRequires: ruby-tool-setup

%description
The caffeine boost you need for your late-night coding sprints.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

#Disabled because of not existed bundler/setup
#%check
#%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jun 07 2018 Maxim Voronov <mvoronov@altlinux.org> 0.0.2-alt2%ubt
- Disable tests because of not existed bundler/setup

* Wed May 30 2018 Maxim Voronov <mvoronov@altlinux.org> 0.0.2-alt1%ubt
- initial build for ALT

