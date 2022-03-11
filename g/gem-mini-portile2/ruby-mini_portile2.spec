%define        gemname mini_portile2

Name:          gem-mini-portile2
Version:       2.8.0
Release:       alt1
Summary:       Simple autoconf builder for developers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/mini_portile
Vcs:           https://github.com/flavorjones/mini_portile.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.1.4 gem(bundler) < 3
BuildRequires: gem(minitar) >= 0.9 gem(minitar) < 1
BuildRequires: gem(minitest) >= 5.15 gem(minitest) < 6
BuildRequires: gem(minitest-hooks) >= 1.5 gem(minitest-hooks) < 2
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(webrick) >= 1.7 gem(webrick) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names mini_portile2,mini-portile2
Obsoletes:     ruby-mini_portile2 < %EVR
Provides:      ruby-mini_portile2 = %EVR
Provides:      gem(mini_portile2) = 2.8.0


%description
It's intended primarily to make sure that you, as the developer of a library,
can reproduce a user's dependencies and environment by specifying a specific
version of an underlying dependency that you'd like to use.


%package       -n gem-mini-portile2-doc
Version:       2.8.0
Release:       alt1
Summary:       Simple autoconf builder for developers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mini_portile2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mini_portile2) = 2.8.0

%description   -n gem-mini-portile2-doc
Simple autoconf builder for developers documentation files.

It's intended primarily to make sure that you, as the developer of a library,
can reproduce a user's dependencies and environment by specifying a specific
version of an underlying dependency that you'd like to use.

%description   -n gem-mini-portile2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mini_portile2.


%package       -n gem-mini-portile2-devel
Version:       2.8.0
Release:       alt1
Summary:       Simple autoconf builder for developers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mini_portile2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mini_portile2) = 2.8.0
Requires:      gem(bundler) >= 2.1.4 gem(bundler) < 3
Requires:      gem(minitar) >= 0.9 gem(minitar) < 1
Requires:      gem(minitest) >= 5.15 gem(minitest) < 6
Requires:      gem(minitest-hooks) >= 1.5 gem(minitest-hooks) < 2
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(webrick) >= 1.7 gem(webrick) < 2

%description   -n gem-mini-portile2-devel
Simple autoconf builder for developers development package.

It's intended primarily to make sure that you, as the developer of a library,
can reproduce a user's dependencies and environment by specifying a specific
version of an underlying dependency that you'd like to use.

%description   -n gem-mini-portile2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mini_portile2.


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

%files         -n gem-mini-portile2-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mini-portile2-devel
%doc README.md


%changelog
* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.8.0-alt1
- ^ 2.7.0 -> 2.8.0

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- ^ 2.5.0 -> 2.7.0

* Tue Jun 09 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.4.0 -> 2.5.0
- ! spec tags

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt2
- > Ruby Policy 2.0

* Wed Jan 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Bump to 2.4.0;
- Place library into proper ruby gem folder.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2.1
- Rebuild for new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Package as gem.
- Disable tests.

* Thu Sep 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux
