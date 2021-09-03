%define        gemname tty-color

Name:          gem-tty-color
Version:       0.6.0
Release:       alt1
Summary:       Terminal color capabilities detection
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
Vcs:           https://github.com/piotrmurach/tty-color.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(tty-color) = 0.6.0


%description
TTY::Color provides independent color support detection component for TTY
toolkit.


%package       -n gem-tty-color-doc
Version:       0.6.0
Release:       alt1
Summary:       Terminal color capabilities detection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tty-color
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tty-color) = 0.6.0

%description   -n gem-tty-color-doc
Terminal color capabilities detection documentation
files.

TTY::Color provides independent color support detection component for TTY
toolkit.

%description   -n gem-tty-color-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tty-color.


%package       -n gem-tty-color-devel
Version:       0.6.0
Release:       alt1
Summary:       Terminal color capabilities detection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tty-color
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tty-color) = 0.6.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-tty-color-devel
Terminal color capabilities detection development
package.

TTY::Color provides independent color support detection component for TTY
toolkit.

%description   -n gem-tty-color-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tty-color.


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

%files         -n gem-tty-color-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tty-color-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- ^ 0.5.0 -> 0.6.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with usage Ruby Policy 2.0
