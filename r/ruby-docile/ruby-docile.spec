%define  pkgname docile
 
Name: 	 ruby-%pkgname
Version: 1.3.0
Release: alt1
 
Summary: Docile keeps your Ruby DSLs tame and well-behaved
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://ms-ati.github.io/docile/
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Docile is a small, self-contained Ruby library, that let's you map a DSL (domain specific language) to your Ruby objects in a snap.

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
* Thu Feb 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.

* Thu Feb 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt0.M70C.1
- Rebuild with Ruby 2.4.3

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- Initial build in Sisyphus
