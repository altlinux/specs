%define        pkgname hoe

Name:          ruby-%pkgname
Version:       3.18.0
Release:       alt1
Summary:       Hoe is a rake/rubygems helper for project Rakefiles
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/hoe
%vcs           https://github.com/seattlerb/hoe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --shebang=auto

%install
%ruby_install

%check
%ruby_test

%files
%_bindir/sow
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Mon Jul 29 2019 Pavel Skrylev <majioa@altlinux.org> 3.18.0-alt1
! v3.18.0
! spec

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
