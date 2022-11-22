%define        gemname all_images

Name:          gem-all-images
Version:       0.2.1
Release:       alt1
Summary:       Runs a script in all of the docker images
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/flori/all_images
Vcs:           https://github.com/flori/all_images.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(tins) >= 1.0 gem(tins) < 2
BuildRequires: gem(term-ansicolor) >= 0
BuildRequires: gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(tins) >= 1.0 gem(tins) < 2
BuildRequires: gem(term-ansicolor) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
%ruby_alias_names all_images,all-images
Requires:      gem(tins) >= 1.0 gem(tins) < 2
Requires:      gem(term-ansicolor) >= 0
Provides:      gem(all_images) = 0.2.1


%description
A script that runs a script in all of the configured docker images


%package       -n all-images
Version:       0.2.1
Release:       alt1
Summary:       Runs a script in all of the docker images executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета all_images
Group:         Other
BuildArch:     noarch

Requires:      gem(all_images) = 0.2.1

%description   -n all-images
Runs a script in all of the docker images executable(s).

A script that runs a script in all of the configured docker images

%description   -n all-images -l ru_RU.UTF-8
Исполнямка для самоцвета all_images.


%package       -n gem-all-images-doc
Version:       0.2.1
Release:       alt1
Summary:       Runs a script in all of the docker images documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета all_images
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(all_images) = 0.2.1

%description   -n gem-all-images-doc
Runs a script in all of the docker images documentation files.

A script that runs a script in all of the configured docker images

%description   -n gem-all-images-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета all_images.


%package       -n gem-all-images-devel
Version:       0.2.1
Release:       alt1
Summary:       Runs a script in all of the docker images development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета all_images
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(all_images) = 0.2.1
Requires:      gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(debug) >= 0

%description   -n gem-all-images-devel
Runs a script in all of the docker images development package.

A script that runs a script in all of the configured docker images

%description   -n gem-all-images-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета all_images.


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

%files         -n all-images
%doc README.md
%_bindir/all_images

%files         -n gem-all-images-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-all-images-devel
%doc README.md


%changelog
* Tue Nov 22 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- ^ 0.0.1 -> 0.2.1

* Tue Jul 05 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + packaged gem with Ruby Policy 2.0
