%define  pkgname text
 
Name: 	 ruby-%pkgname
Version: 1.3.1 
Release: alt4.1
 
Summary: Collection of text algorithms
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/threedaymonk/text
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
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
%rubygem_specdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt4.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt4
- Use system way to package as gem.

* Thu Jun 28 2018 Denis Medvedev <nbr@altlinux.org> 1.3.1-alt3.1
- removed patch from package

* Thu Jun 28 2018 Denis Medvedev <nbr@altlinux.org> 1.3.1-alt3
- fix build: alt-gemspec patch no longer needed

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2
- Rebuild with Ruby 2.4.2

* Mon May 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build in Sisyphus
