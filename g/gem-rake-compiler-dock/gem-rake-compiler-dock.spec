%define        gemname rake-compiler-dock

Name:          gem-rake-compiler-dock
Version:       1.1.0
Release:       alt1
Summary:       Easy to use and reliable cross compiler environment for building Windows, Linux and JRuby binary gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rake-compiler/rake-compiler-dock
Vcs:           https://github.com/rake-compiler/rake-compiler-dock.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.7 gem(bundler) < 3
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(test-unit) >= 3.0 gem(test-unit) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(rake-compiler-dock) = 1.1.0


%description
Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems.

It provides cross compilers and Ruby environments for 2.2 and newer versions of
the RubyInstaller and Linux runtime environments. They are prepared for use with
rake-compiler. It is used by many gems with C or JRuby extentions.

This is kind of successor of rake-compiler-dev-box. It is wrapped as a gem for
easier setup, usage and integration and is based on lightweight Docker
containers. It is also more reliable, since the underlying docker images are
versioned and immutable.


%package       -n rake-compiler-dock
Version:       1.1.0
Release:       alt1
Summary:       Easy to use and reliable cross compiler environment for building Windows, Linux and JRuby binary gems executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rake-compiler-dock
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rake-compiler-dock) = 1.1.0

%description   -n rake-compiler-dock
Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems executable(s).

Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems.

It provides cross compilers and Ruby environments for 2.2 and newer versions of
the RubyInstaller and Linux runtime environments. They are prepared for use with
rake-compiler. It is used by many gems with C or JRuby extentions.

This is kind of successor of rake-compiler-dev-box. It is wrapped as a gem for
easier setup, usage and integration and is based on lightweight Docker
containers. It is also more reliable, since the underlying docker images are
versioned and immutable.

%description   -n rake-compiler-dock -l ru_RU.UTF-8
Исполнямка для самоцвета rake-compiler-dock.


%package       -n gem-rake-compiler-dock-doc
Version:       1.1.0
Release:       alt1
Summary:       Easy to use and reliable cross compiler environment for building Windows, Linux and JRuby binary gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rake-compiler-dock
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rake-compiler-dock) = 1.1.0

%description   -n gem-rake-compiler-dock-doc
Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems documentation files.

Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems.

It provides cross compilers and Ruby environments for 2.2 and newer versions of
the RubyInstaller and Linux runtime environments. They are prepared for use with
rake-compiler. It is used by many gems with C or JRuby extentions.

This is kind of successor of rake-compiler-dev-box. It is wrapped as a gem for
easier setup, usage and integration and is based on lightweight Docker
containers. It is also more reliable, since the underlying docker images are
versioned and immutable.

%description   -n gem-rake-compiler-dock-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rake-compiler-dock.


%package       -n gem-rake-compiler-dock-devel
Version:       1.1.0
Release:       alt1
Summary:       Easy to use and reliable cross compiler environment for building Windows, Linux and JRuby binary gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rake-compiler-dock
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rake-compiler-dock) = 1.1.0
Requires:      gem(bundler) >= 1.7 gem(bundler) < 3
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(test-unit) >= 3.0 gem(test-unit) < 4

%description   -n gem-rake-compiler-dock-devel
Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems development package.

Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems.

It provides cross compilers and Ruby environments for 2.2 and newer versions of
the RubyInstaller and Linux runtime environments. They are prepared for use with
rake-compiler. It is used by many gems with C or JRuby extentions.

This is kind of successor of rake-compiler-dev-box. It is wrapped as a gem for
easier setup, usage and integration and is based on lightweight Docker
containers. It is also more reliable, since the underlying docker images are
versioned and immutable.

%description   -n gem-rake-compiler-dock-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rake-compiler-dock.


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

%files         -n rake-compiler-dock
%doc README.md
%_bindir/rake-compiler-dock

%files         -n gem-rake-compiler-dock-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rake-compiler-dock-devel
%doc README.md


%changelog
* Tue Jun 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 0.7.2 -> 1.1.0

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.2-alt1
- ^ 0.7.1 -> 0.7.2

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
