%define        pkgname gem-plugin
%define        gemname gem_plugin

Name:          gem-%pkgname
Version:       0.2.3
Release:       alt3
Summary:       Gem Based Plugin System
Group:         Development/Ruby
License:       GPLv2
Url:           https://github.com/genki/gem_plugin
Vcs:           https://github.com/genki/gem_plugin.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ruby
Provides:      ruby-%gemname
Obsoletes:     ruby-%gemname

%description
GemPlugin is a system that lets your users install gems and
lets you load them as additional features to use in your
software.  It originated from the Mongrel project but proved
useful enough to break out into a separate project.


%package       -n gpgen
Summary:       Gem Based Plugin System executable file
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gpgen
Executable file for %gemname gem.

%description   -n gpgen -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n gpgen
%_bindir/gpgen


%changelog
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt3
- > Ruby Policy 2.0
- ! spec tags
- - sources

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt2.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 21 2014 Led <led@altlinux.ru> 0.2.3-alt2.2
- disabled %%check

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.2.3-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.3-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 0.2.3-alt1
- Built for Sisyphus

