%define  pkgname text
 
Name: 	 ruby-%pkgname
Version: 1.3.1 
Release: alt2.2
 
Summary: Collection of text algorithms
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/threedaymonk/text
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
Patch1: alt-gemspec.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Collection of text algorithms: Levenshtein, Soundex, Metaphone, Double
Metaphone, Porter Stemming.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p1
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
# Install gemspec
export rbVersion=`ruby -e "puts RbConfig::CONFIG[\"ruby_version\"]"`
install -Dm 0644 %pkgname.gemspec %buildroot%ruby_libdir/gems/$rbVersion/specifications/%pkgname.gemspec
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
%ruby_libdir/gems/*/specifications/%pkgname.gemspec
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2
- Rebuild with Ruby 2.4.2

* Mon May 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build in Sisyphus
