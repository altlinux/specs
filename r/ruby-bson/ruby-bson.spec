%define        pkgname bson

Name: 	       ruby-%pkgname
Version:       4.4.2
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+)
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://bsonspec.org
# VCS:         https://github.com/mongodb/bson-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%changelog
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 4.4.2-alt1
- Bump to 4.4.2
- Use Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.1
- Rebuild with Ruby 2.5.0

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
