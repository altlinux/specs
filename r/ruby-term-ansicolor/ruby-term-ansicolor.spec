%define        pkgname term-ansicolor

Name:          ruby-%pkgname
Version:       1.7.1
Release:       alt1
Summary:       Ruby library that colors strings using ANSI escape sequences
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://flori.github.io/term-ansicolor/
# VCS:         https://github.com/flori/term-ansicolor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
This library can be used to color/decolor strings using ANSI escape sequences.


%package       doc
Summary:       Documentation files for %pkgname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %pkgname.


%package       -n %pkgname
Summary:       Executable files for %pkgname
Group:         Text tools
BuildArch:     noarch

%description   -n %pkgname
Executable files for %pkgname.

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*

%changelog
* Fri Mar 01 2019 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- Bump to 1.7.1;
- Use Ruby Policy 2.0.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1.2
- Rebuild for new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.4-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 25 2009 Igor Zubkov <icesik@altlinux.org> 1.0.4-alt1
- build for Sisyphus

