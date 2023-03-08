%define  pkgname backports
 
Name: 	 gem-%pkgname
Version: 3.24.0
Release: alt1
 
Summary: The latest features of Ruby backported to older versions

License: Ruby
Group:   Development/Ruby
Url:     https://github.com/marcandre/backports
Vcs:     https://github.com/marcandre/backports
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel 

Provides: ruby-%pkgname = %EVR
Obsoletes: ruby-%pkgname < %EVR
 
%description
The goal of 'backports' is to make it easier to write ruby code that runs across
different versions of Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation
Provides: ruby-%pkgname-doc = %EVR
Obsoletes: ruby-%pkgname-doc < %EVR
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
 
%build
%ruby_build
 
%install
%ruby_install
 
%check
%ruby_test
 
%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
 
%files doc
%ruby_gemdocdir
 
%changelog
* Wed Mar 08 2023 Andrey Cherepanov <cas@altlinux.org> 3.24.0-alt1
- New version.

* Sat Jan 01 2022 Andrey Cherepanov <cas@altlinux.org> 3.23.0-alt1
- New version.

* Fri Apr 02 2021 Andrey Cherepanov <cas@altlinux.org> 3.21.0-alt1
- New version.

* Thu Jan 28 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.2-alt1
- New version.

* Mon Jan 04 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.1-alt1
- New version.

* Thu Dec 31 2020 Andrey Cherepanov <cas@altlinux.org> 3.20.0-alt1
- New version.

* Mon Dec 28 2020 Andrey Cherepanov <cas@altlinux.org> 3.19.0-alt1
- New version.

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.18.2-alt1
- New version.
- Rename to gem-%pkgname according to Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 3.7.0-alt1
- Initial build in sisyphus
