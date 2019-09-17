%define        pkgname netrc

Summary:       Library to read and write netrc files
Name:          ruby-%pkgname
Version:       0.11.0
Release:       alt1
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/heroku/netrc
%vcs           https://github.com/heroku/netrc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
This library can read and update netrc files, preserving formatting including
comments and whitespace.


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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- ^ v0.11.0
- ^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 0.10.3-alt1
- Update to last release

* Sat Dec 08 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.7-alt1
- Initial build for Sisyphus

