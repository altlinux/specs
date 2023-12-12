%define        _unpackaged_files_terminate_build 1
%define        gemname childprocess

Name:          gem-childprocess
Version:       4.1.0
Release:       alt1
Summary:       Cross-platform Ruby library for managing child processes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/enkessler/childprocess
Vcs:           https://github.com/enkessler/childprocess.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard) >= 0.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(coveralls) >= 1.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-childprocess < %EVR
Provides:      ruby-childprocess = %EVR
Provides:      gem(childprocess) = 4.1.0


%description
Cross-platform Ruby library for managing child processes.


%package       -n gem-childprocess-doc
Version:       4.1.0
Release:       alt1
Summary:       Cross-platform Ruby library for managing child processes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета childprocess
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(childprocess) = 4.1.0

%description   -n gem-childprocess-doc
Cross-platform Ruby library for managing child processes documentation files.

%description   -n gem-childprocess-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета childprocess.


%package       -n gem-childprocess-devel
Version:       4.1.0
Release:       alt1
Summary:       Cross-platform Ruby library for managing child processes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета childprocess
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(childprocess) = 4.1.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(yard) >= 0.0
Requires:      gem(rake) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1
Conflicts:     gem(coveralls) >= 1.0

%description   -n gem-childprocess-devel
Cross-platform Ruby library for managing child processes development package.

%description   -n gem-childprocess-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета childprocess.


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

%files         -n gem-childprocess-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-childprocess-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 4.1.0-alt1
- ^ 3.0.0 -> 4.1.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- updated (^) 2.0.0 -> 3.0.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- updated (^) 0.9.0 -> 2.0.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus
