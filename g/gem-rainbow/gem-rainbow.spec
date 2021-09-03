%define        gemname rainbow

Name:          gem-rainbow
Version:       3.1.0
Release:       alt1
Summary:       Colorize printed text on ANSI terminals
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sickill/rainbow
Vcs:           https://github.com/sickill/rainbow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(rainbow) = 3.1.0


%description
Rainbow is a ruby gem for colorizing printed text on ANSI terminals.

It provides a string presenter object, which adds several methods to your
strings for wrapping them in ANSI escape codes. These codes when printed in a
terminal change text attributes like text color, background color, intensity
etc.


%package       -n gem-rainbow-doc
Version:       3.1.0
Release:       alt1
Summary:       Colorize printed text on ANSI terminals documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rainbow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rainbow) = 3.1.0

%description   -n gem-rainbow-doc
Colorize printed text on ANSI terminals documentation files.

Rainbow is a ruby gem for colorizing printed text on ANSI terminals.

It provides a string presenter object, which adds several methods to your
strings for wrapping them in ANSI escape codes. These codes when printed in a
terminal change text attributes like text color, background color, intensity
etc.

%description   -n gem-rainbow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rainbow.


%package       -n gem-rainbow-devel
Version:       3.1.0
Release:       alt1
Summary:       Colorize printed text on ANSI terminals development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rainbow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rainbow) = 3.1.0
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3

%description   -n gem-rainbow-devel
Colorize printed text on ANSI terminals development package.

Rainbow is a ruby gem for colorizing printed text on ANSI terminals.

It provides a string presenter object, which adds several methods to your
strings for wrapping them in ANSI escape codes. These codes when printed in a
terminal change text attributes like text color, background color, intensity
etc.

%description   -n gem-rainbow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rainbow.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rainbow-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-rainbow-devel
%doc README.markdown


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.0 -> 3.1.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
