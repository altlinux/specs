%define  pkgname highline
 
Name: 	 ruby-%pkgname
Version: 1.7.5 
Release: alt1
 
Summary: HighLine is a high-level command-line IO Ruby library
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://highline.rubyforge.org
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
A high-level IO library that provides validation, type conversion, and
more for command-line interfaces. HighLine also includes a complete menu
system that can crank out anything from simple list selection to
complete shells with just minutes of work.

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
#ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.5.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Jan 04 2010 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt2
- fix Url
- fix License

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt1
- build for Sisyphus

