%define        _unpackaged_files_terminate_build 1
%define        gemname e2mmap

Name:          gem-e2mmap
Version:       0.1.0
Release:       alt1
Summary:       Module for defining custom exceptions with specific messages
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/e2mmap
Vcs:           https://github.com/ruby/e2mmap.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(rake) >= 10.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(e2mmap) = 0.1.0


%description
Module for defining custom exceptions with specific messages.


%package       -n gem-e2mmap-doc
Version:       0.1.0
Release:       alt1
Summary:       Module for defining custom exceptions with specific messages documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета e2mmap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(e2mmap) = 0.1.0

%description   -n gem-e2mmap-doc
Module for defining custom exceptions with specific messages documentation
files.

%description   -n gem-e2mmap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета e2mmap.


%package       -n gem-e2mmap-devel
Version:       0.1.0
Release:       alt1
Summary:       Module for defining custom exceptions with specific messages development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета e2mmap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(e2mmap) = 0.1.0
Requires:      gem(bundler) >= 1.16
Requires:      gem(rake) >= 10.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-e2mmap-devel
Module for defining custom exceptions with specific messages development
package.

%description   -n gem-e2mmap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета e2mmap.


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

%files         -n gem-e2mmap-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-e2mmap-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with Ruby Policy 2.0
