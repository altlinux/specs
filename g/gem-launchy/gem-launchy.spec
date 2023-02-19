%define        gemname launchy

Name:          gem-launchy
Version:       2.5.2
Release:       alt1
Summary:       A helper for launching cross-platform applications in a fire and forget manner
License:       ISC
Group:         Development/Ruby
Url:           https://github.com/copiousfreetime/launchy
Vcs:           https://github.com/copiousfreetime/launchy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(minitest) >= 5.15
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(addressable) >= 2.8
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(addressable) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(addressable) >= 2.8
Conflicts:     gem(addressable) >= 3
Obsoletes:     ruby-launchy < %EVR
Provides:      ruby-launchy = %EVR
Provides:      gem(launchy) = 2.5.2


%description
Launchy is helper class for launching cross-platform applications in a fire and
forget manner.

There are application concepts (browser, email client, etc) that are common
across all platforms, and they may be launched differently on each platform.
Launchy is here to make a common approach to launching external application from
within ruby programs.


%package       -n launchy
Version:       2.5.2
Release:       alt1
Summary:       A helper for launching cross-platform applications in a fire and forget manner executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета launchy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(launchy) = 2.5.2

%description   -n launchy
A helper for launching cross-platform applications in a fire and forget manner
executable(s).

Launchy is helper class for launching cross-platform applications in a fire and
forget manner.

There are application concepts (browser, email client, etc) that are common
across all platforms, and they may be launched differently on each platform.
Launchy is here to make a common approach to launching external application from
within ruby programs.

%description   -n launchy -l ru_RU.UTF-8
Исполнямка для самоцвета launchy.


%package       -n gem-launchy-doc
Version:       2.5.2
Release:       alt1
Summary:       A helper for launching cross-platform applications in a fire and forget manner documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета launchy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(launchy) = 2.5.2

%description   -n gem-launchy-doc
A helper for launching cross-platform applications in a fire and forget manner
documentation files.

Launchy is helper class for launching cross-platform applications in a fire and
forget manner.

There are application concepts (browser, email client, etc) that are common
across all platforms, and they may be launched differently on each platform.
Launchy is here to make a common approach to launching external application from
within ruby programs.

%description   -n gem-launchy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета launchy.


%package       -n gem-launchy-devel
Version:       2.5.2
Release:       alt1
Summary:       A helper for launching cross-platform applications in a fire and forget manner development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета launchy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(launchy) = 2.5.2
Requires:      gem(rake) >= 13.0
Requires:      gem(minitest) >= 5.15
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(simplecov) >= 1

%description   -n gem-launchy-devel
A helper for launching cross-platform applications in a fire and forget manner
development package.

Launchy is helper class for launching cross-platform applications in a fire and
forget manner.

There are application concepts (browser, email client, etc) that are common
across all platforms, and they may be launched differently on each platform.
Launchy is here to make a common approach to launching external application from
within ruby programs.

%description   -n gem-launchy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета launchy.


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

%files         -n launchy
%doc README.md
%_bindir/launchy

%files         -n gem-launchy-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-launchy-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- ^ 2.5.0 -> 2.5.2

* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.4.3 -> 2.5.0

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.3-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1.1
- Rebuild with new Ruby autorequirements.
- Package as gem.
- Package executable.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- Initial build for Sisyphus
