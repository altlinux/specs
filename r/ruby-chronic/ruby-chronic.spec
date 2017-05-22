%define  pkgname chronic
 
Name: 	 ruby-%pkgname
Version: 0.10.2 
Release: alt1
 
Summary: Chronic is a pure Ruby natural language date parser
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/mojombo/chronic
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Chronic is a natural language date/time parser written in pure Ruby. See
below for the wide variety of formats Chronic will parse.

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
* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1
- Initial build in Sisyphus
