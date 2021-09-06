%define        gemname bake-modernize

Name:          gem-bake-modernize
Version:       0.4.10
Release:       alt1
Summary:       Automatically modernize parts of your project/gem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/bake-modernize
Vcs:           https://github.com/ioquatix/bake-modernize.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(async-http) >= 0
BuildRequires: gem(bake) >= 0
BuildRequires: gem(build-files) >= 1.6 gem(build-files) < 2
BuildRequires: gem(markly) >= 0
BuildRequires: gem(rugged) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-http) >= 0
Requires:      gem(bake) >= 0
Requires:      gem(build-files) >= 1.6 gem(build-files) < 2
Requires:      gem(markly) >= 0
Requires:      gem(rugged) >= 0
Provides:      gem(bake-modernize) = 0.4.10


%description
Automatically modernize parts of your project/gem.


%package       -n gem-bake-modernize-doc
Version:       0.4.10
Release:       alt1
Summary:       Automatically modernize parts of your project/gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bake-modernize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bake-modernize) = 0.4.10

%description   -n gem-bake-modernize-doc
Automatically modernize parts of your project/gem documentation files.

%description   -n gem-bake-modernize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bake-modernize.


%package       -n gem-bake-modernize-devel
Version:       0.4.10
Release:       alt1
Summary:       Automatically modernize parts of your project/gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bake-modernize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bake-modernize) = 0.4.10
Requires:      gem(rspec) >= 0 

%description   -n gem-bake-modernize-devel
Automatically modernize parts of your project/gem development package.

%description   -n gem-bake-modernize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bake-modernize.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc template/readme template/readme/. template/readme/README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-bake-modernize-doc
%doc template/readme template/readme/. template/readme/README.md
%ruby_gemdocdir

%files         -n gem-bake-modernize-devel
%doc template/readme template/readme/. template/readme/README.md


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.10-alt1
- + packaged gem with Ruby Policy 2.0
