%define        gemname sys-proctable

Name:          gem-sys-proctable
Version:       1.2.6
Release:       alt1
Summary:       A Ruby interface for gathering process information
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/djberg96/sys-proctable
Vcs:           https://github.com/djberg96/sys-proctable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 0
Obsoletes:     ruby-sys-proctable < %EVR
Provides:      ruby-sys-proctable = %EVR
Provides:      gem(sys-proctable) = 1.2.6


%description
A cross-platform Ruby interface for gathering process information on your
operating system.


%package       -n gem-sys-proctable-doc
Version:       1.2.6
Release:       alt1
Summary:       A Ruby interface for gathering process information documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sys-proctable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sys-proctable) = 1.2.6

%description   -n gem-sys-proctable-doc
A Ruby interface for gathering process information documentation files.

A cross-platform Ruby interface for gathering process information on your
operating system.

%description   -n gem-sys-proctable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sys-proctable.


%package       -n gem-sys-proctable-devel
Version:       1.2.6
Release:       alt1
Summary:       A Ruby interface for gathering process information development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sys-proctable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sys-proctable) = 1.2.6
Requires:      gem(rspec) >= 0 gem(rspec) < 4
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-sys-proctable-devel
A Ruby interface for gathering process information development package.

A cross-platform Ruby interface for gathering process information on your
operating system.

%description   -n gem-sys-proctable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sys-proctable.


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

%files         -n gem-sys-proctable-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sys-proctable-devel
%doc README.md


%changelog
* Fri Jul 16 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.6-alt1
- ^ 1.2.1 -> 1.2.6

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
