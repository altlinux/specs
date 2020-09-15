%define        pkgname thor

Name: 	       gem-%pkgname
Version:       1.0.1
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces.
License:       MIT
Group:         Development/Ruby
Url:           http://whatisthor.com/
Vcs:           https://github.com/erikhuda/thor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Thor is a simple and efficient tool for building self-documenting
command line utilities. It removes the pain of parsing command line
options, writing "USAGE:" banners, and can also be used as an
alternative to the Rake build tool. The syntax is Rake-like, so it
should be familiar to most Rake users.


%package       -n %pkgname
Summary:       %summary
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
Thor is a simple and efficient tool for building self-documenting
command line utilities. It removes the pain of parsing command line
options, writing "USAGE:" banners, and can also be used as an
alternative to the Rake build tool. The syntax is Rake-like, so it
should be familiar to most Rake users.

Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%pkgname

%files         doc
%ruby_gemdocdir


%changelog
* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 0.20.3 -> 1.0.1
- ! spec tags

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 0.20.3-alt2
- > Ruby Policy 2.0.

* Mon Nov 12 2018 Andrey Cherepanov <cas@altlinux.org> 0.20.3-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- Initial build for ALT Linux
