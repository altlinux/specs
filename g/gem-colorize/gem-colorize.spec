%define        gemname colorize

Name:          gem-colorize
Version:       0.8.1
Release:       alt1
Summary:       Ruby gem for colorizing text using ANSI escape sequences
License:       GPL-2.0
Group:         Development/Ruby
Url:           https://github.com/fazibear/colorize
Vcs:           https://github.com/fazibear/colorize.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(codeclimate-test-reporter) >= 0.4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(codeclimate-test-reporter) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency codeclimate-test-reporter >= 1.0.9,codeclimate-test-reporter < 2
Provides:      gem(colorize) = 0.8.1


%description
Extends String class or add a ColorizedString with methods to set text color,
background color and text effects.


%package       -n gem-colorize-doc
Version:       0.8.1
Release:       alt1
Summary:       Ruby gem for colorizing text using ANSI escape sequences documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета colorize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(colorize) = 0.8.1

%description   -n gem-colorize-doc
Ruby gem for colorizing text using ANSI escape sequences documentation
files.

Extends String class or add a ColorizedString with methods to set text color,
background color and text effects.

%description   -n gem-colorize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета colorize.


%package       -n gem-colorize-devel
Version:       0.8.1
Release:       alt1
Summary:       Ruby gem for colorizing text using ANSI escape sequences development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета colorize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(colorize) = 0.8.1
Requires:      gem(rake) >= 10.0
Requires:      gem(minitest) >= 5.0
Requires:      gem(codeclimate-test-reporter) >= 0.4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(codeclimate-test-reporter) >= 2

%description   -n gem-colorize-devel
Ruby gem for colorizing text using ANSI escape sequences development
package.

Extends String class or add a ColorizedString with methods to set text color,
background color and text effects.

%description   -n gem-colorize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета colorize.


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

%files         -n gem-colorize-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-colorize-devel
%doc README.md


%changelog
* Sun Feb 05 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.1-alt1
- + packaged gem with Ruby Policy 2.0
