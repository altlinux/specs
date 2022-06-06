%define        gemname sys-filesystem

Name:          gem-sys-filesystem
Version:       1.4.3
Release:       alt1
Summary:       A Ruby interface for getting file system information
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/djberg96/sys-filesystem
Vcs:           https://github.com/djberg96/sys-filesystem.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi) >= 1.1 gem(ffi) < 2
BuildRequires: gem(mkmf-lite) >= 0.5 gem(mkmf-lite) < 1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.1 gem(ffi) < 2
Provides:      gem(sys-filesystem) = 1.4.3


%description
The sys-filesystem library provides a cross-platform interface for gathering
filesystem information, such as disk space and mount point data.


%package       -n gem-sys-filesystem-doc
Version:       1.4.3
Release:       alt1
Summary:       A Ruby interface for getting file system information documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sys-filesystem
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sys-filesystem) = 1.4.3

%description   -n gem-sys-filesystem-doc
A Ruby interface for getting file system information documentation files.

The sys-filesystem library provides a cross-platform interface for gathering
filesystem information, such as disk space and mount point data.

%description   -n gem-sys-filesystem-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sys-filesystem.


%package       -n gem-sys-filesystem-devel
Version:       1.4.3
Release:       alt1
Summary:       A Ruby interface for getting file system information development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sys-filesystem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sys-filesystem) = 1.4.3
Requires:      gem(mkmf-lite) >= 0.5 gem(mkmf-lite) < 1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4

%description   -n gem-sys-filesystem-devel
A Ruby interface for getting file system information development package.

The sys-filesystem library provides a cross-platform interface for gathering
filesystem information, such as disk space and mount point data.

%description   -n gem-sys-filesystem-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sys-filesystem.


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

%files         -n gem-sys-filesystem-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sys-filesystem-devel
%doc README.md


%changelog
* Sun Apr 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.3-alt1
- + packaged gem with Ruby Policy 2.0
