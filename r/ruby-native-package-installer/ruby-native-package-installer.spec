%define  pkgname native-package-installer

Name:          ruby-%pkgname
Version:       1.0.7
Release:       alt1
Summary:       It helps to install native packages on "gem install"
License:       LGPLv3
Group:         Development/Ruby
Url:           https://github.com/ruby-gnome2/native-package-installer
# VCS:         https://github.com/ruby-gnome2/native-package-installer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Users need to install native packages to install an extension library
that depends on native packages. It bores users because users need to
install native packages and an extension library separately.
native-package-installer helps to install native packages on "gem install".
Users can install both native packages and an extension library by one action,
"gem install".

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem

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

%files doc
%ruby_gemdocdir

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1
- Bump to 1.0.7
- Use Ruby Policy 2.0

* Sat Jan 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus
