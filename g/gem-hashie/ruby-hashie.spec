%define        gemname hashie

Name:          gem-hashie
Version:       4.1.0
Release:       alt1
Summary:       Hashie is a simple collection of useful Hash extensions
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/intridea/hashie
Vcs:           https://github.com/hashie/hashie.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names elasticsearch,rails,omniauth-oauth2,rails-without-dependency,omniauth,active_support
Obsoletes:     ruby-hashie < %EVR
Provides:      ruby-hashie = %EVR
Provides:      gem(hashie) = 4.1.0


%description
Hashie is a growing collection of tools that extend Hashes and make them more
useful.


%package       -n gem-hashie-doc
Version:       4.1.0
Release:       alt1
Summary:       Hashie is a simple collection of useful Hash extensions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hashie
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hashie) = 4.1.0

%description   -n gem-hashie-doc
Hashie is a simple collection of useful Hash extensions documentation
files.

Hashie is a growing collection of tools that extend Hashes and make them more
useful.

%description   -n gem-hashie-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hashie.


%package       -n gem-hashie-devel
Version:       4.1.0
Release:       alt1
Summary:       Hashie is a simple collection of useful Hash extensions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hashie
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hashie) = 4.1.0
Requires:      gem(bundler) >= 0 gem(bundler) < 3

%description   -n gem-hashie-devel
Hashie is a simple collection of useful Hash extensions development
package.

Hashie is a growing collection of tools that extend Hashes and make them more
useful.

%description   -n gem-hashie-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hashie.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-hashie-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hashie-devel
%doc README.md


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 4.1.0-alt1
- ^ 3.6.0 -> 4.1.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.7-alt1
- New version.

* Wed Jul 12 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt1
- New version

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.5-alt1
- New version

* Thu Feb 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.4-alt1
- new version 3.5.4

* Mon Feb 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.3-alt1
- new version 3.5.3

* Sat Feb 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.2-alt1
- new version 3.5.2

* Wed Feb 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- new version 3.5.1

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.6-alt1
- new version 3.4.6

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.4-alt1
- New version

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- Initial build for ALT Linux
