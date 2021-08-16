%define        gemname sys-uname

Name:          gem-sys-uname
Version:       1.2.2
Release:       alt1
Summary:       An interface for returning uname (platform) information
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/djberg96/sys-uname
Vcs:           https://github.com/djberg96/sys-uname.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi) >= 1.1 gem(ffi) < 2
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.1 gem(ffi) < 2
Provides:      gem(sys-uname) = 1.2.2

%description
The sys-uname library provides an interface for gathering information about your
current platform. The library is named after the Unix 'uname' command but also
works on MS Windows. Available information includes OS name, OS version, system
name and so on. Additional information is available for certain platforms.


%package       -n gem-sys-uname-doc
Version:       1.2.2
Release:       alt1
Summary:       An interface for returning uname (platform) information documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sys-uname
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sys-uname) = 1.2.2

%description   -n gem-sys-uname-doc
An interface for returning uname (platform) information documentation files.

The sys-uname library provides an interface for gathering information about your
current platform. The library is named after the Unix 'uname' command but also
works on MS Windows. Available information includes OS name, OS version, system
name and so on. Additional information is available for certain platforms.

%description   -n gem-sys-uname-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sys-uname.


%package       -n gem-sys-uname-devel
Version:       1.2.2
Release:       alt1
Summary:       An interface for returning uname (platform) information development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sys-uname
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sys-uname) = 1.2.2
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(rake) >= 0

%description   -n gem-sys-uname-devel
An interface for returning uname (platform) information development package.

The sys-uname library provides an interface for gathering information about your
current platform. The library is named after the Unix 'uname' command but also
works on MS Windows. Available information includes OS name, OS version, system
name and so on. Additional information is available for certain platforms.

%description   -n gem-sys-uname-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sys-uname.


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

%files         -n gem-sys-uname-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sys-uname-devel
%doc README.md


%changelog
* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with Ruby Policy 2.0
