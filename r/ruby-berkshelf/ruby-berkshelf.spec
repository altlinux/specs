%define        pkgname berkshelf

Name:          ruby-%pkgname
Version:       7.0.8
Release:       alt1
Summary:       A Chef Cookbook manager
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/berkshelf/berkshelf
# VCS:         https://github.com/berkshelf/berkshelf.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary

%package       -n berks
Summary:       A Chef Cookbook manager executable
Group:         Documentation
BuildArch:     noarch

%description   -n berks
%summary called "berks".

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

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

%files         -n berks
%_bindir/*

%files         doc
%ruby_gemdocdir

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 7.0.8-alt1
- Bump to 7.0.8

* Tue Feb 19 2019 Pavel Skrylev <majioa@altlinux.org> 7.0.7-alt1
- Bump to 7.0.7;
- Use Ruby Policy 2.0.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.4-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- Initial build for Sisyphus
