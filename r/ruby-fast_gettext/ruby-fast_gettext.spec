%define  pkgname fast_gettext
 
Name: 	 ruby-%pkgname
Version: 1.1.0
Release: alt2.1
 
Summary: GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34) and threadsafe!
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/grosser/fast_gettext
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
Patch1:  alt-gemspec.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(mathn)$/d

%description
GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7
vs 34) and threadsafe!

It supports multiple backends (.mo, .po, .yml files,
Database(ActiveRecord + any other), Chain, Loggers) and can easily be
extended.

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
%doc Readme*
%ruby_sitelibdir/*
%ruby_libdir/gems/*/specifications/*.gemspec
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Rebuild with Ruby 2.4.2

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build in Sisyphus
