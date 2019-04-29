%define        pkgname hoe

Name:          ruby-%pkgname
Version:       3.17.2
Release:       alt1
Summary:       Hoe is a rake/rubygems helper for project Rakefiles
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/hoe
# VCS:         https://github.com/seattlerb/hoe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build --shebang=auto

%install
%gem_install

%check
%gem_test

%files
%_bindir/sow
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Thu Apr 25 2019 Pavel Skrylev <majioa@altlinux.org> 3.17.2-alt1
- Bump to 3.17.2
- Use Ruby Policy 2.0

* Mon Oct 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt2.1
- Rebuild with new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt2
- Clarify ignored modules.
- Package as gem.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt1
- Initial build for Sisyphus
