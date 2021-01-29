%define        pkgname parallel

Name:          gem-%pkgname
Version:       1.20.1
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

%description
Run any code in parallel Processes(> use all CPUs) or Threads(> speedup
blocking operations).
Best suited for map-reduce or e.g. parallel downloads/uploads.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jan 28 2021 Pavel Skrylev <majioa@altlinux.org> 1.20.1-alt1
- ^ 1.17.0 -> 1.20.1

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.17.0-alt1
- ^ 1.14.0 -> 1.17.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.14.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
