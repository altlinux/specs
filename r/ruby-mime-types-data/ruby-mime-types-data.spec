%define  pkgname mime-types-data
 
Name: 	 ruby-%pkgname
Version: 3.2016.0521 
Release: alt1
 
Summary: MIME Type registry data
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/mime-types/mime-types-data
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
mime-types-data provides a registry for information about MIME media
type definitions. It can be used with the Ruby mime-types library or
other software to determine defined filename extensions for MIME types,
or to use filename extensions to look up the likely MIME type
definitions.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
subst 's,PATH = .*,PATH = "%_datadir/%name",' lib/mime/types/data.rb
%update_setup_rb
 
%build
%ruby_config --datadir=%_datadir/%name
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
%_datadir/%name
 
%files doc
%ruby_ri_sitedir/MIME/Types/Data
 
%changelog
* Fri Mar 31 2017 Andrey Cherepanov <cas@altlinux.org> 3.2016.0521-alt1
- Initial build in Sisyphus
