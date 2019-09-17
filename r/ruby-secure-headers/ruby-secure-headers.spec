%define        pkgname secure-headers
%define        gemname secure_headers

Name:          ruby-%pkgname
Version:       6.1.1
Release:       alt1
Summary:       Manages application of security headers with many safe defaults
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/twitter/secureheaders
%vcs           https://github.com/twitter/secureheaders.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
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
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- ^ v6.1.1
- ^ Ruby Policy 2.0

* Wed Sep 26 2018 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt2
- ^ v6.0.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.0.5-alt1
- v v5.0.5 for foreman.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- Initial build for Sisyphus
