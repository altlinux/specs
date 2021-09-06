%define        gemname compass

Name:          gem-compass
Version:       1.0.3
Release:       alt1
Summary:       A Real Stylesheet Framework
License:       MIT
Group:         Development/Ruby
Url:           http://compass-style.org
Vcs:           https://github.com/Compass/compass.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(multi_json) >= 1.0 gem(multi_json) < 2
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sass) >= 3.3.13 gem(sass) < 4
BuildRequires: gem(chunky_png) >= 1.2 gem(chunky_png) < 2
BuildRequires: gem(rb-fsevent) >= 0.9.3
BuildRequires: gem(rb-inotify) >= 0.9
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(diff-lcs) >= 0
BuildRequires: gem(sass-globbing) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency bundler >= 3.7.4,sass < 4
%ruby_use_gem_version compass:1.0.3
%ruby_use_gem_version compass-core:1.0.3
%ruby_ignore_names compass-style.org
Requires:      gem(sass) >= 3.3.13 gem(sass) < 4
Requires:      gem(compass-core) = 1.0.3
Requires:      gem(compass-import-once) = 1.0.5
Requires:      gem(chunky_png) >= 1.2 gem(chunky_png) < 2
Requires:      gem(rb-fsevent) >= 0.9.3
Requires:      gem(rb-inotify) >= 0.9
Provides:      gem(compass) = 1.0.3


%description
Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintenance of CSS.


%package       -n gem-compass-core
Version:       1.0.3
Release:       alt1
Summary:       The Compass core stylesheet library
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass) >= 3.3.0 gem(sass) < 4
Requires:      gem(multi_json) >= 1.0 gem(multi_json) < 2
Provides:      gem(compass-core) = 1.0.3

%description   -n gem-compass-core
The Compass core stylesheet library and minimum required ruby extensions. This
library can be used stand-alone without the compass ruby configuration file or
compass command line tools.


%package       -n gem-compass-core-doc
Version:       1.0.3
Release:       alt1
Summary:       The Compass core stylesheet library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета compass-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(compass-core) = 1.0.3

%description   -n gem-compass-core-doc
The Compass core stylesheet library documentation files.

The Compass core stylesheet library and minimum required ruby extensions. This
library can be used stand-alone without the compass ruby configuration file or
compass command line tools.

%description   -n gem-compass-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета compass-core.


%package       -n gem-compass-core-devel
Version:       1.0.3
Release:       alt1
Summary:       The Compass core stylesheet library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета compass-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(compass-core) = 1.0.3
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-compass-core-devel
The Compass core stylesheet library development package.

The Compass core stylesheet library and minimum required ruby extensions. This
library can be used stand-alone without the compass ruby configuration file or
compass command line tools.

%description   -n gem-compass-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета compass-core.


%package       -n gem-compass-import-once
Version:       1.0.5
Release:       alt1
Summary:       Speed up your Sass compilation by making @import only import each file once
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass) >= 3.2 gem(sass) < 4
Provides:      gem(compass-import-once) = 1.0.5

%description   -n gem-compass-import-once
Changes the behavior of Sass's @import directive to only import a file once.


%package       -n gem-compass-import-once-doc
Version:       1.0.5
Release:       alt1
Summary:       Speed up your Sass compilation by making @import only import each file once documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета compass-import-once
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(compass-import-once) = 1.0.5

%description   -n gem-compass-import-once-doc
Speed up your Sass compilation by making @import only import each file once
documentation files.

Changes the behavior of Sass's @import directive to only import a file once.

%description   -n gem-compass-import-once-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета compass-import-once.


%package       -n gem-compass-import-once-devel
Version:       1.0.5
Release:       alt1
Summary:       Speed up your Sass compilation by making @import only import each file once development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета compass-import-once
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(compass-import-once) = 1.0.5
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(diff-lcs) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(sass-globbing) >= 0

%description   -n gem-compass-import-once-devel
Speed up your Sass compilation by making @import only import each file once
development package.

Changes the behavior of Sass's @import directive to only import a file once.

%description   -n gem-compass-import-once-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета compass-import-once.


%package       -n compass
Version:       1.0.3
Release:       alt1
Summary:       A Real Stylesheet Framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета compass
Group:         Other
BuildArch:     noarch

Requires:      gem(compass) = 1.0.3

%description   -n compass
A Real Stylesheet Framework executable(s).

Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintenance of CSS.

%description   -n compass -l ru_RU.UTF-8
Исполнямка для самоцвета compass.


%package       -n gem-compass-doc
Version:       1.0.3
Release:       alt1
Summary:       A Real Stylesheet Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета compass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(compass) = 1.0.3

%description   -n gem-compass-doc
A Real Stylesheet Framework documentation files.

Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintenance of CSS.

%description   -n gem-compass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета compass.


%package       -n gem-compass-devel
Version:       1.0.3
Release:       alt1
Summary:       A Real Stylesheet Framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета compass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(compass) = 1.0.3

%description   -n gem-compass-devel
A Real Stylesheet Framework development package.

Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintenance of CSS.

%description   -n gem-compass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета compass.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-compass-core
%doc README.markdown
%ruby_gemspecdir/compass-core-1.0.3.gemspec
%ruby_gemslibdir/compass-core-1.0.3

%files         -n gem-compass-core-doc
%doc README.markdown
%ruby_gemsdocdir/compass-core-1.0.3

%files         -n gem-compass-core-devel
%doc README.markdown

%files         -n gem-compass-import-once
%doc README.markdown
%ruby_gemspecdir/compass-import-once-1.0.5.gemspec
%ruby_gemslibdir/compass-import-once-1.0.5

%files         -n gem-compass-import-once-doc
%doc README.markdown
%ruby_gemsdocdir/compass-import-once-1.0.5

%files         -n gem-compass-import-once-devel
%doc README.markdown

%files         -n compass
%doc README.markdown
%_bindir/compass

%files         -n gem-compass-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-compass-devel
%doc README.markdown


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- + packaged gem with Ruby Policy 2.0
