%define        pkgname rack-openid

Name:          gem-%pkgname
Version:       1.4.2
Release:       alt2.1
Summary:       Provides a more HTTPish API around the ruby-openid library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/rack-openid
Vcs:           https://github.com/grosser/rack-openid.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

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
%doc Readme*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt2.1
- fixed (!) spec

* Wed Sep 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt2
- used (>) Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus (without tests).
