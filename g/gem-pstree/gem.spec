%define        gemname pstree

Name:          gem-pstree
Version:       0.3.0
Release:       alt1
Summary:       Ruby library that builds a process tree of this host
License:       GPL-2
Group:         Development/Ruby
Url:           http://flori.github.com/pstree
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
BuildRequires: gem(simplecov) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Provides:      gem(pstree) = 0.3.0


%description
This library uses the output of the ps command to creaste process tree data
structure for the current host.


%package       -n ruby-pstree
Version:       0.3.0
Release:       alt1
Summary:       Ruby library that builds a process tree of this host executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pstree
Group:         Other
BuildArch:     noarch

Requires:      gem(pstree) = 0.3.0

%description   -n ruby-pstree
Ruby library that builds a process tree of this host executable(s).

This library uses the output of the ps command to creaste process tree data
structure for the current host.

%description   -n ruby-pstree -l ru_RU.UTF-8
Исполнямка для самоцвета pstree.


%package       -n gem-pstree-doc
Version:       0.3.0
Release:       alt1
Summary:       Ruby library that builds a process tree of this host documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pstree
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pstree) = 0.3.0

%description   -n gem-pstree-doc
Ruby library that builds a process tree of this host documentation files.

This library uses the output of the ps command to creaste process tree data
structure for the current host.

%description   -n gem-pstree-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pstree.


%package       -n gem-pstree-devel
Version:       0.3.0
Release:       alt1
Summary:       Ruby library that builds a process tree of this host development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pstree
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pstree) = 0.3.0
Requires:      gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
Requires:      gem(simplecov) >= 0

%description   -n gem-pstree-devel
Ruby library that builds a process tree of this host development package.

This library uses the output of the ps command to creaste process tree data
structure for the current host.

%description   -n gem-pstree-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pstree.


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

%files         -n ruby-pstree
%doc README.md
%_bindir/ruby-pstree

%files         -n gem-pstree-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pstree-devel
%doc README.md


%changelog
* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
