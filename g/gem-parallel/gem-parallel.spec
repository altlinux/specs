%define        gemname parallel

Name:          gem-parallel
Version:       1.20.2
Release:       alt1
Summary:       Run any kind of code in parallel processes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/parallel
Vcs:           https://github.com/grosser/parallel.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(parallel) = 1.20.2


%description
Run any code in parallel Processes(> use all CPUs) or Threads(> speedup blocking
operations). Best suited for map-reduce or e.g. parallel downloads/uploads.


%package       -n gem-parallel-doc
Version:       1.20.2
Release:       alt1
Summary:       Run any kind of code in parallel processes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета parallel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(parallel) = 1.20.2

%description   -n gem-parallel-doc
Run any kind of code in parallel processes documentation files.

Run any code in parallel Processes(> use all CPUs) or Threads(> speedup blocking
operations). Best suited for map-reduce or e.g. parallel downloads/uploads.

%description   -n gem-parallel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета parallel.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-parallel-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.20.2-alt1
- ^ 1.20.1 -> 1.20.2

* Thu Jan 28 2021 Pavel Skrylev <majioa@altlinux.org> 1.20.1-alt1
- ^ 1.17.0 -> 1.20.1

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.17.0-alt1
- ^ 1.14.0 -> 1.17.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.14.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
