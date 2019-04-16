%define        pkgname strptime

Name:          ruby-%pkgname
Version:       0.2.3
Release:       alt3
Summary:       A fast strpitme engine
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/nurse/strptime/
# VCS:         https://github.com/nurse/strptime.git
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
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt3
- Use Ruby Policy 2.0

* Fri Feb 22 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.3-alt2
- Fix license

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
