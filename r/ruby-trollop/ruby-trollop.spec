%define  pkgname trollop
 
Name: 	 ruby-%pkgname
Version: 2.1.2 
Release: alt1
 
Summary: Trollop is a commandline option parser for Ruby that just gets out of your wa
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://manageiq.github.io/trollop/
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Trollop is a commandline option parser for Ruby that just gets out of
your way. One line of code per option is all you need to write. For
that, you get a nice automatically-generated help page, robust option
parsing, and sensible defaults for everything you don't specify.

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
* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- Initial build in Sisyphus
