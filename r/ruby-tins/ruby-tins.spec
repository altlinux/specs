%define        pkgname tins

Name:          ruby-%pkgname
Version:       1.20.2
Release:       alt1
Summary:       All the stuff that isn't good/big enough for a real library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flori/tins
# VCS:         https://github.com/flori/tins.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.


%package       doc
Summary:       Documentation files for %pkgname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{pkgname}.


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

%changelog
* Fri Mar 01 2019 Pavel Skrylev <majioa@altlinux.org> 1.20.2-alt1
- Bump to 1.20.2;
- Use Ruby Policy 2.0.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- New version.

* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.3-alt1
- Initial build for Sisyphus
