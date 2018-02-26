%define pkgname ruby-aggregate

Name: %pkgname 
Version: 0.2.2
Release: alt2

Summary: Aggregate is a Ruby class for accumulating aggregate statistics and includes histogram support.
Group: Development/Ruby 
License: MIT
Url: https://github.com/josephruscio/aggregate

Packager: Anton Gorlov <stalker at altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar

# Automatically added by buildreq on Wed Aug 10 2011
# optimized out: ruby ruby-stdlibs ruby-tool-rdoc
BuildRequires: libruby-devel ruby-tool-setup ruby-test-unit

%description 
Aggregate is an intuitive ruby implementation of a statistics aggregator including both default and configurable histogram support. It does this
without recording/storing any of the actual sample values, making it suitable for tracking statistics across millions/billions of sample
without any impact on performance or memory footprint. Originally inspired by the Aggregate support in SystemTap.

%package doc 
Summary: Documentation files for %name 
Group: Documentation

%description doc 
Documentation files for %name

%prep
%setup -q -n %pkgname-%version 
%update_setup_rb

%build 
%ruby_config
%ruby_build
#for t in test/test_*.rb; do
%ruby_test_unit -I./  test/ts_aggregate.rb
#done


%install 
%ruby_install 
%rdoc lib/

%files 
%doc README.textile 
%ruby_sitelibdir/*

%files doc 
%doc LICENSE
%ruby_ri_sitedir/Aggregate*

%changelog 
* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 0.2.2-alt2
- fix wrong url and license

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 0.2.2-alt1
-  initial build for ALTLinux




