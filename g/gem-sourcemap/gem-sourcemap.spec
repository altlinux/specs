%define        gemname sourcemap

Name:          gem-sourcemap
Version:       0.1.1
Release:       alt1
Summary:       Ruby source maps
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/maccman/sourcemap
Vcs:           https://github.com/maccman/sourcemap.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(sourcemap) = 0.1.1


%description
A Ruby library to read, create and manipulate Source Maps.


%package       -n gem-sourcemap-doc
Version:       0.1.1
Release:       alt1
Summary:       Ruby source maps documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sourcemap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sourcemap) = 0.1.1

%description   -n gem-sourcemap-doc
Ruby source maps documentation files.

A Ruby library to read, create and manipulate Source Maps.

%description   -n gem-sourcemap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sourcemap.


%package       -n gem-sourcemap-devel
Version:       0.1.1
Release:       alt1
Summary:       Ruby source maps development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sourcemap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sourcemap) = 0.1.1
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Conflicts:     gem(bundler) >= 3

%description   -n gem-sourcemap-devel
Ruby source maps development package.

A Ruby library to read, create and manipulate Source Maps.

%description   -n gem-sourcemap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sourcemap.


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

%files         -n gem-sourcemap-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sourcemap-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
