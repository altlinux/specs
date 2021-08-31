%define        gemname net-ping

Name:          gem-net-ping
Version:       2.0.8
Release:       alt1
Summary:       A collection of classes that provide different ways to ping computers
License:       Artistic-2.0
Group:         Development/Ruby
Url:           https://github.com/chernesk/net-ping
Vcs:           https://github.com/chernesk/net-ping.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit) >= 0
# BuildRequires: gem(fakeweb) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry-byebug) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
Obsoletes:     ruby-net-ping < %EVR
Provides:      ruby-net-ping = %EVR
Provides:      gem(net-ping) = 2.0.8


%description
A collection of classes that provide different ways to ping computers.


%package       -n gem-net-ping-doc
Version:       2.0.8
Release:       alt1
Summary:       A collection of classes that provide different ways to ping computers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-ping
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-ping) = 2.0.8

%description   -n gem-net-ping-doc
A collection of classes that provide different ways to ping computers
documentation files.

%description   -n gem-net-ping-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-ping.


%package       -n gem-net-ping-devel
Version:       2.0.8
Release:       alt1
Summary:       A collection of classes that provide different ways to ping computers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-ping
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-ping) = 2.0.8
Requires:      gem(test-unit) >= 0 gem(test-unit) < 4
Requires:      gem(fakeweb) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(pry-byebug) >= 0

%description   -n gem-net-ping-devel
A collection of classes that provide different ways to ping computers
development package.

%description   -n gem-net-ping-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-ping.


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

%files         -n gem-net-ping-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-net-ping-devel
%doc README.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.8-alt1
- ^ 2.0.6 -> 2.0.8

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.6-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.6-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.0.5 -> v2.0.6

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
