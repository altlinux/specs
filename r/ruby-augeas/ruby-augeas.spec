%define        pkgname ruby-augeas
%define        gemname ruby-augeas

Name:          %pkgname
Version:       0.5.0
Release:       alt3
Epoch:         1
Summary:       Provides bindings for augeas
License:       LGPLv2
Group:         Development/Ruby
Url:           http://augeas.net
# VCS:         https://github.com/hercules-team/ruby-augeas.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(rdoc)
BuildRequires: libaugeas-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig
#Requires: augeas-libs >= 0.8.0
Obsoletes:     ruby-augeas-new

%description
The class Augeas provides bindings to Augeas library.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

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
%gem_build --alias=augeas:ruby-augeas

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspecdir/%gemname-%version.gemspec
%ruby_gemslibdir/%gemname-%version
%ruby_gemsextdir/%gemname-%version

%files         -n gem-%pkgname-doc
%ruby_gemsdocdir/%gemname-%version

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%changelog
* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.5.0-alt3
- Use Ruby Policy 2.0

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.5
- Rebuild for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.1
- Rebuild with Ruby 2.4.1

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2
- Use original gem in Sisyphus (ALT #33345)

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1
- Initial build in Sisyphus
