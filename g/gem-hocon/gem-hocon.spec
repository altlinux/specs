%define  pkgname hocon
 
Name: 	 gem-%pkgname
Version: 1.3.1
Release: alt1
 
Summary: This is a port of the Typesafe Config library to Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/ruby-hocon
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source: ruby-hocon-%version.tar
 
BuildRequires(pre): rpm-build-ruby
 
Provides: ruby-%pkgname = %EVR
Obsoletes: ruby-%pkgname < %EVR

%description
The library provides Ruby support for the HOCON configuration file format.

%package doc
Summary: Documentation files for %name
Group: Documentation
Provides: ruby-%pkgname-doc = %EVR
Obsoletes: ruby-%pkgname-doc < %EVR
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n ruby-hocon-%version
 
%build
%ruby_build
 
%install
%ruby_install
 
%files
%doc README*
%_bindir/hocon
%ruby_gemspec
%ruby_gemlibdir
 
%files doc
%ruby_gemdocdir
 
%changelog
* Thu Jun 17 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.
- Rename to gem-hocon and build as gem.
- Fix License tag.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Apr 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Initial build in Sisyphus
