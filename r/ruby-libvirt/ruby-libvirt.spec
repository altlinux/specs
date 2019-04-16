%define        pkgname ruby-libvirt
%define        gemname ruby-libvirt

Name:          %pkgname
Version:       0.7.1
Release:       alt2
Summary:       Ruby bindings for libvirt
License:       LGPLv2+
Group:         Development/Ruby
Url:           http://libvirt.org/ruby/
# VCS:         git://libvirt.org/ruby-libvirt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libvirt-devel >= 0.4.0

%description
The module Libvirt provides bindings to libvirt.


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
%gem_build --alias=ruby-libvirt:libvirt --join=lib:bin

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
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt2
- Use Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1.2
- Rebuild for new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1.1
- Rebuild for aarch64.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
Initial build for Sisyphus.
