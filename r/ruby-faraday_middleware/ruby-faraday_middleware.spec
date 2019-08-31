%define        pkgname faraday_middleware
%define        gemname faraday_middleware

Name: 	       ruby-%pkgname
Version:       0.13.1
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday_middleware
%vcs           https://github.com/lostisland/faraday_middleware.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description doc
Documentation files for %gemname gem.

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
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- Bump to 0.13.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1
- Initial build for Sisyphus
