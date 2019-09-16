%define        pkgname net-ping

Name:          ruby-%pkgname
Version:       2.0.6
Release:       alt1
Summary:       A collection of classes that provide different ways to ping computers.
License:       Artistic 2.0
Group:         Development/Ruby
Url:           https://github.com/chernesk/net-ping
%vcs           https://github.com/chernesk/net-ping.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.


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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.6-alt1
- ^ v2.0.6
- ^ Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
