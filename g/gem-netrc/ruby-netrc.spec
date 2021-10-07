%define        gemname netrc

Name:          gem-netrc
Version:       0.11.0
Release:       alt2
Summary:       Library to read and write netrc files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/heroku/netrc
Vcs:           https://github.com/heroku/netrc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         exec-fix.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-netrc
Provides:      ruby-netrc
Provides:      gem(netrc) = 0.11.0


%description
This library can read and update netrc files, preserving formatting including
comments and whitespace.


%package       -n gem-netrc-doc
Version:       0.11.0
Release:       alt2
Summary:       Library to read and write netrc files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета netrc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(netrc) = 0.11.0

%description   -n gem-netrc-doc
Library to read and write netrc files documentation files.

This library can read and update netrc files, preserving formatting including
comments and whitespace.

%description   -n gem-netrc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета netrc.


%package       -n gem-netrc-devel
Version:       0.11.0
Release:       alt2
Summary:       Library to read and write netrc files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета netrc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(netrc) = 0.11.0
Requires:      gem(minitest) >= 0

%description   -n gem-netrc-devel
Library to read and write netrc files development package.

This library can read and update netrc files, preserving formatting including
comments and whitespace.

%description   -n gem-netrc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета netrc.


%prep
%setup
%patch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-netrc-doc
%doc Readme.md
%ruby_gemdocdir

%files         -n gem-netrc-devel
%doc Readme.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt2
- ! spec

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- updated (^) 0.10.3 -> 0.11.0
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 0.10.3-alt1
- Update to last release

* Sat Dec 08 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.7-alt1
- Initial build for Sisyphus
