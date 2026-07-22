%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sys-uname

Name:          gem-sys-uname
Version:       1.5.1
Release:       alt1
Summary:       An interface for returning uname (platform) information
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/djberg96/sys-uname
Vcs:           https://github.com/djberg96/sys-uname.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ffi) >= 1.1
BuildRequires: gem(memoist3) >= 1.0.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(memoist3) >= 1.1
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.1
Requires:      gem(memoist3) >= 1.0.0
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(memoist3) >= 1.1
Provides:      gem(sys-uname) = 1.5.1

%description
The sys-uname library provides an interface for gathering information about your
current platform. The library is named after the Unix 'uname' command but also
works on MS Windows. Available information includes OS name, OS version, system
name and so on. Additional information is available for certain platforms.


%if_enabled    doc
%package       -n gem-sys-uname-doc
Version:       1.5.1
Release:       alt1
Summary:       An interface for returning uname (platform) information documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sys-uname
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(sys-uname) = 1.5.1

%description   -n gem-sys-uname-doc
An interface for returning uname (platform) information documentation
files.

The sys-uname library provides an interface for gathering information about your
current platform. The library is named after the Unix 'uname' command but also
works on MS Windows. Available information includes OS name, OS version, system
name and so on. Additional information is available for certain platforms.

%description   -n gem-sys-uname-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sys-uname.
%endif


%if_enabled    devel
%package       -n gem-sys-uname-devel
Version:       1.5.1
Release:       alt1
Summary:       An interface for returning uname (platform) information development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sys-uname
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(sys-uname) = 1.5.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.9
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-rspec) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-sys-uname-devel
An interface for returning uname (platform) information development
package.

The sys-uname library provides an interface for gathering information about your
current platform. The library is named after the Unix 'uname' command but also
works on MS Windows. Available information includes OS name, OS version, system
name and so on. Additional information is available for certain platforms.

%description   -n gem-sys-uname-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sys-uname.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-sys-uname-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sys-uname-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.1-alt1
- ^ 1.2.2 -> 1.5.1

* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with Ruby Policy 2.0
