%define        pkgname thor

Name: 	       %pkgname
Version:       0.20.3
Release:       alt2
Summary:       Thor is a toolkit for building powerful command-line interfaces.
License:       MIT
Group:         Development/Ruby
Url:           http://whatisthor.com/
# VCS:	       https://github.com/erikhuda/thor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Thor is a simple and efficient tool for building self-documenting
command line utilities. It removes the pain of parsing command line
options, writing "USAGE:" banners, and can also be used as an
alternative to the Rake build tool. The syntax is Rake-like, so it
should be familiar to most Rake users.


%package       -n gem-%pkgname
Summary:       %summary
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname
Thor is a simple and efficient tool for building self-documenting
command line utilities. It removes the pain of parsing command line
options, writing "USAGE:" banners, and can also be used as an
alternative to the Rake build tool. The syntax is Rake-like, so it
should be familiar to most Rake users.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %pkgname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %pkgname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%_bindir/%name

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 0.20.3-alt2
- Use Ruby Policy 2.0.

* Mon Nov 12 2018 Andrey Cherepanov <cas@altlinux.org> 0.20.3-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- Initial build for ALT Linux
