%define        pkgname rpam-ruby19

Name: 	       ruby-%pkgname
Version:       1.2.2
Release:       alt1.gitbc66d5e.8
Summary:       PAM auth for Ruby - 1.9 compat version
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/canweriotnow/rpam-ruby19
# VCS:         https://github.com/canweriotnow/rpam-ruby19.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libpam0-devel

%description
This extension provides PAM (Pluggable Authentication Modules) integration. The
library provides a stable API for applications to defer to for authentication
tasks.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


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
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1.gitbc66d5e.8
- Use Ruby Policy 2.0

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.7
- Fix package as gem.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.6
- Rebuild for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.5
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.4
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.3
- Rebuild for really put gemspec to correct place with Ruby 2.4.2

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.1
- Rebuild with Ruby 2.4.1

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e
- Initial build in Sisyphus
