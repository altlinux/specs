%define        pkgname excon

Name:          ruby-%pkgname
Version:       0.66.0
Release:       alt1
Summary:       Usable, fast, simple HTTP 1.1 for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/excon/excon
%vcs           https://github.com/excon/excon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Usable, fast, simple Ruby HTTP 1.1

Excon was designed to be simple, fast and performant. It works great as
a general HTTP(s) client and is particularly well suited to usage in API
clients.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
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

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.66.0-alt1
- ^ v0.66.0
- ^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.62.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.62.0-alt1
- Initial build for Sisyphus
