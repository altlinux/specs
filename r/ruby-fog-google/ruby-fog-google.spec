%define        pkgname fog-google

Name:          ruby-%pkgname
Version:       1.8.2
Release:       alt1
Epoch:         1
Summary:       Fog for Google Cloud Platform
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-google
# VCS:         https://github.com/fog/fog-google.git

Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%gem_replace_version google-api-client ~> 0.24

%description
%summary

%package       doc
Summary:       Documentation files for %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname.

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

%files doc
%ruby_gemdocdir

%changelog
* Fri Mar 08 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.8.2-alt1
- Bump to 1.8.2;
- Use Ruby Policy 2.0.

* Tue Nov 13 2018 Pavel Skrylev <majioa@altlinux.org> 1:1.8.1-alt1
- Bump to 1.8.1.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.0.9-alt1
- Use old version for fog.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.
- Package as gem.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus
