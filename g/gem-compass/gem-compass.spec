%define        gemname compass

Name:          gem-compass
Version:       1.1.0
Release:       alt1
Summary:       A Real Stylesheet Framework
License:       MIT
Group:         Development/Ruby
Url:           http://compass-style.org
Vcs:           https://github.com/compass/compass.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(sass) >= 3.3.13
BuildRequires: gem(sass-globbing) >= 1.1.1
BuildRequires: gem(cucumber) >= 1.2.1
BuildRequires: gem(rspec) >= 2.0.0
BuildRequires: gem(compass-validator) = 3.0.1
BuildRequires: gem(css_parser) >= 1.0.1
BuildRequires: gem(rubyzip) = 0.9.9
BuildRequires: gem(mocha) >= 0.11.4
BuildRequires: gem(minitest) >= 2.12.1
BuildRequires: gem(diff-lcs) >= 1.1.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(json) >= 1.7.7
BuildRequires: gem(true) >= 0.2.3
BuildRequires: gem(rb-fsevent) >= 0.9.3
BuildRequires: gem(ruby_gntp) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(rcov) >= 0
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-test) >= 0
BuildRequires: gem(guard-cucumber) >= 0
BuildRequires: gem(colorize) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(chunky_png) >= 1.2
BuildRequires: gem(rb-inotify) >= 0.9
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(timecop) >= 0.5.9.2
BuildRequires: gem(multi_json) >= 1.0
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(diff-lcs) >= 0
BuildRequires: gem(sass-globbing) >= 0
BuildConflicts: gem(sass) >= 4
BuildConflicts: gem(sass-globbing) >= 1.2
BuildConflicts: gem(cucumber) >= 1.3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(css_parser) >= 1.1
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(diff-lcs) >= 1.2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(true) >= 0.3
BuildConflicts: gem(chunky_png) >= 2
BuildConflicts: gem(timecop) >= 0.5.10
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency sass >= 3.7.4,json < 4
%ruby_alias_names gem-compass,compass
%ruby_ignore_names compass-style.org
Requires:      gem(sass) >= 3.3.13
Requires:      gem(rb-fsevent) >= 0.9.3
Requires:      gem(compass-core) >= 1.1.0
Requires:      gem(compass-import-once) >= 1.1.0
Requires:      gem(chunky_png) >= 1.2
Requires:      gem(rb-inotify) >= 0.9
Conflicts:     gem(sass) >= 4
Conflicts:     gem(compass-core) >= 1.2
Conflicts:     gem(chunky_png) >= 2
Provides:      gem(compass) = 1.1.0
Provides:      ruby-gem-compass

%ruby_use_gem_version compass:1.1.0
%ruby_use_gem_version compass-core:1.1.0
%ruby_use_gem_version compass-import-once:1.1.0

%description
Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintenance of CSS.


%package       -n compass
Version:       1.1.0
Release:       alt1
Summary:       A Real Stylesheet Framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета compass
Group:         Other
BuildArch:     noarch

Requires:      gem(compass) = 1.1.0

%description   -n compass
A Real Stylesheet Framework executable(s).

Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintenance of CSS.

%description   -n compass -l ru_RU.UTF-8
Исполнямка для самоцвета compass.


%package       -n gem-compass-doc
Version:       1.1.0
Release:       alt1
Summary:       A Real Stylesheet Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета compass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(compass) = 1.1.0

%description   -n gem-compass-doc
A Real Stylesheet Framework documentation files.

Compass is a Sass-based Stylesheet Framework that streamlines the creation and
maintenance of CSS.

%description   -n gem-compass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета compass.


%package       -n gem-compass-core
Version:       1.1.0
Release:       alt1
Summary:       A Real Stylesheet Framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass) >= 3.3.0
Requires:      gem(multi_json) >= 1.0
Conflicts:     gem(sass) >= 4
Conflicts:     gem(multi_json) >= 2
Provides:      gem(compass-core) = 1.1.0

%description   -n gem-compass-core
The Compass core stylesheet library and minimum required ruby extensions. This
library can be used stand-alone without the compass ruby configuration file or
compass command line tools.


%package       -n gem-compass-core-doc
Version:       1.1.0
Release:       alt1
Summary:       A Real Stylesheet Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета compass-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(compass-core) = 1.1.0

%description   -n gem-compass-core-doc
A Real Stylesheet Framework documentation files.

The Compass core stylesheet library and minimum required ruby extensions. This
library can be used stand-alone without the compass ruby configuration file or
compass command line tools.

%description   -n gem-compass-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета compass-core.


%package       -n gem-compass-import-once
Version:       1.1.0
Release:       alt1
Summary:       A Real Stylesheet Framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass) >= 3.2
Conflicts:     gem(sass) >= 4
Provides:      gem(compass-import-once) = 1.1.0

%description   -n gem-compass-import-once
Changes the behavior of Sass's @import directive to only import a file once.


%package       -n gem-compass-import-once-doc
Version:       1.1.0
Release:       alt1
Summary:       A Real Stylesheet Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета compass-import-once
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(compass-import-once) = 1.1.0

%description   -n gem-compass-import-once-doc
A Real Stylesheet Framework documentation files.

Changes the behavior of Sass's @import directive to only import a file once.

%description   -n gem-compass-import-once-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета compass-import-once.


%prep
%setup
%autopatch

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

%files         -n compass
%doc README.markdown
%_bindir/compass

%files         -n gem-compass-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-compass-core
%doc README.markdown
%ruby_gemspecdir/compass-core-1.1.0.gemspec
%ruby_gemslibdir/compass-core-1.1.0

%files         -n gem-compass-core-doc
%doc README.markdown
%ruby_gemsdocdir/compass-core-1.1.0

%files         -n gem-compass-import-once
%doc README.markdown
%ruby_gemspecdir/compass-import-once-1.1.0.gemspec
%ruby_gemslibdir/compass-import-once-1.1.0

%files         -n gem-compass-import-once-doc
%doc README.markdown
%ruby_gemsdocdir/compass-import-once-1.1.0


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.3 -> 1.1.0 (no devel)

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- + packaged gem with Ruby Policy 2.0
