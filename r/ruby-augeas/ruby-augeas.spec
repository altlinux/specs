%define  pkgname augeas
 
Name: 	 ruby-%pkgname
Version: 0.5.0 
Release: alt1
 
Summary: Ruby bindings for Augeas
License: LGPL2 
Group:   Development/Ruby
Url:     https://github.com/dotdoom/augeas
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby libruby-devel
BuildRequires: ruby-tool-setup ruby-stdlibs libaugeas-devel
 
%description
The class Augeas provides bindings to augeas [augeas.net] library.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
 
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
* Fri Mar 31 2017 Denis Medvedev <nbr@altlinux.org> 0.5.0-alt1
- Initial sisyphus release
