%define        gemname detroit

Name:          gem-detroit
Version:       0.3.0
Release:       alt1
Summary:       Software Production Mangement
License:       GPL3
Group:         Development/Ruby
Url:           http://rubyworks.github.com/detroit
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(facets) >= 0
BuildRequires: gem(pom) >= 0
BuildRequires: gem(qed) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(facets) >= 0
Requires:      gem(pom) >= 0
Provides:      gem(detroit) = 0.3.0


%description
Detroit is an advanced lifecycle build system. With Detroit, build tasks are
user defined service instances tied to stops along a track. Whenever the detroit
console command is run, a track is followed from beginning to designated
destination.


%package       -n gem-detroit-devel
Version:       0.3.0
Release:       alt1
Summary:       Software Production Mangement development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета detroit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(detroit) = 0.3.0
Requires:      gem(qed) >= 0

%description   -n gem-detroit-devel
Software Production Mangement development package.

Detroit is an advanced lifecycle build system. With Detroit, build tasks are
user defined service instances tied to stops along a track. Whenever the detroit
console command is run, a track is followed from beginning to designated
destination.

%description   -n gem-detroit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета detroit.


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

%files         -n gem-detroit-devel


%changelog
* Wed Oct 06 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
