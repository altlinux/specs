%define        gemname tty-cursor

Name:          gem-tty-cursor
Version:       0.7.1
Release:       alt1
Summary:       Terminal cursor movement and manipulation of cursor properties such as visibility
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
Vcs:           https://github.com/piotrmurach/tty-cursor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.6 gem(bundler) < 3
BuildRequires: gem(rspec) >= 3.1 gem(rspec) < 4
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(tty-cursor) = 0.7.1


%description
Terminal cursor positioning, visibility and text manipulation.

The purpose of this library is to help move the terminal cursor around and
manipulate text by using intuitive method calls.

TTY::Cursor provides independent cursor movement component for TTY toolkit.


%package       -n gem-tty-cursor-doc
Version:       0.7.1
Release:       alt1
Summary:       Terminal cursor movement and manipulation of cursor properties such as visibility documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tty-cursor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tty-cursor) = 0.7.1

%description   -n gem-tty-cursor-doc
Terminal cursor movement and manipulation of cursor properties such as
visibility documentation files.

Terminal cursor positioning, visibility and text manipulation.

The purpose of this library is to help move the terminal cursor around and
manipulate text by using intuitive method calls.

TTY::Cursor provides independent cursor movement component for TTY toolkit.


%description   -n gem-tty-cursor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tty-cursor.


%package       -n gem-tty-cursor-devel
Version:       0.7.1
Release:       alt1
Summary:       Terminal cursor movement and manipulation of cursor properties such as visibility development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tty-cursor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tty-cursor) = 0.7.1
Requires:      gem(bundler) >= 1.6 gem(bundler) < 3
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-tty-cursor-devel
Terminal cursor movement and manipulation of cursor properties such as
visibility development package.

Terminal cursor positioning, visibility and text manipulation.

The purpose of this library is to help move the terminal cursor around and
manipulate text by using intuitive method calls.

TTY::Cursor provides independent cursor movement component for TTY toolkit.

%description   -n gem-tty-cursor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tty-cursor.


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

%files         -n gem-tty-cursor-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tty-cursor-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- ^ 0.7.0 -> 0.7.1

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with usage Ruby Policy 2.0
