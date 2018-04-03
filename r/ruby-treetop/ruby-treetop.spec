%define  pkgname treetop
 
Name: 	 ruby-%pkgname
Version: 1.6.10
Release: alt1
 
Summary: A Ruby-based text parsing and interpretation DSL
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://treetop.rubyforge.org/
# VCS:   git://github.com/cjheath/treetop

Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-polyglot
 
%description
Treetop is a language for describing languages. Combining the elegance
of Ruby with cutting-edge parsing expression grammars, it helps you
analyze syntax with revolutionary ease.

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
%_bindir/tt
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.10-alt1
- New version.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.5-alt1
- New version

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux
