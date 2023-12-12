%define        _unpackaged_files_terminate_build 1
%define        gemname gem_plugin

Name:          gem-gem-plugin
Version:       0.2.3
Release:       alt3.1
Summary:       Gem Based Plugin System
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/genki/gem_plugin
Vcs:           https://github.com/genki/gem_plugin.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gem_plugin) = 0.2.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names gem_plugin,gem-plugin
%ruby_ignore_names <%= project %>
Obsoletes:     ruby-gem_plugin < %EVR
Provides:      ruby-gem_plugin = %EVR
Provides:      gem(gem_plugin) = 0.2.3

%ruby_bindir_to %ruby_bindir

%description
GemPlugin is a system that lets your users install gems and lets you load them
as additional features to use in your software. It originated from the Mongrel
project but proved useful enough to break out into a separate project.


%package       -n gpgen
Version:       0.2.3
Release:       alt3.1
Summary:       Gem Based Plugin System executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gem_plugin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gem_plugin) = 0.2.3

%description   -n gpgen
Gem Based Plugin System executable(s).

GemPlugin is a system that lets your users install gems and lets you load them
as additional features to use in your software. It originated from the Mongrel
project but proved useful enough to break out into a separate project.

%description   -n gpgen -l ru_RU.UTF-8
Исполнямка для самоцвета gem_plugin.


%package       -n gem-gem-plugin-doc
Version:       0.2.3
Release:       alt3.1
Summary:       Gem Based Plugin System documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem_plugin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem_plugin) = 0.2.3

%description   -n gem-gem-plugin-doc
Gem Based Plugin System documentation files.

GemPlugin is a system that lets your users install gems and lets you load them
as additional features to use in your software. It originated from the Mongrel
project but proved useful enough to break out into a separate project.

%description   -n gem-gem-plugin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem_plugin.


%package       -n gem-gem-plugin-devel
Version:       0.2.3
Release:       alt3.1
Summary:       Gem Based Plugin System development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gem_plugin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gem_plugin) = 0.2.3

%description   -n gem-gem-plugin-devel
Gem Based Plugin System development package.

GemPlugin is a system that lets your users install gems and lets you load them
as additional features to use in your software. It originated from the Mongrel
project but proved useful enough to break out into a separate project.

%description   -n gem-gem-plugin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gem_plugin.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gpgen
%doc README
%ruby_bindir/gpgen

%files         -n gem-gem-plugin-doc
%doc README
%ruby_gemdocdir

%files         -n gem-gem-plugin-devel
%doc README


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt3.1
- ! spec for %%ruby_bindir

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt3
- > Ruby Policy 2.0
- ! spec tags
- - sources

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt2.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 21 2014 Led <led@altlinux.ru> 0.2.3-alt2.2
- disabled %%ruby_test

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.2.3-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.3-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 0.2.3-alt1
- Built for Sisyphus
