%define        gemname paint

Name:          gem-paint
Version:       2.2.1
Release:       alt1
Summary:       Ruby gem for ANSI terminal colors
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/paint
Vcs:           https://github.com/janlelis/paint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.2 gem(rspec) < 4
BuildRequires: gem(rake) >= 12.3 gem(rake) < 14
BuildRequires: gem(benchmark-ips) >= 2.7 gem(benchmark-ips) < 3
BuildRequires: gem(rainbow) >= 3.0 gem(rainbow) < 4
BuildRequires: gem(term-ansicolor) >= 1.7 gem(term-ansicolor) < 2
BuildRequires: gem(ansi) >= 1.5 gem(ansi) < 2
BuildRequires: gem(hansi) >= 0.2 gem(hansi) < 1
BuildRequires: gem(pastel) >= 0.7 gem(pastel) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_ignore_names standalone_cookbook,omnibus,kitchen-tests,win32-eventlog,paint-shortcuts
Obsoletes:     ruby-paint < %EVR
Provides:      ruby-paint = %EVR
Provides:      gem(paint) = 2.2.1


%description
Paint creates terminal colors and effects for you. It combines the strengths of
term-ansicolor, rainbow, and similar projects into a simple to use, however
still flexible terminal colors gem with no core extensions by default.


#%package       -n gem-paint-shortcuts
#Version:       2.2.1
#Release:       alt1
#Summary:       Extends the paint gem to support custom color shortcuts
#Group:         Development/Ruby
#BuildArch:     noarch
#
#Requires:      gem(paint) >= 1.0 gem(paint) < 3.0
#Provides:      gem(paint-shortcuts) = 2.2.1
#
#%description   -n gem-paint-shortcuts
#Extends the paint gem to support custom color shortcuts.
#
#
#%package       -n gem-paint-shortcuts-doc
#Version:       2.2.1
#Release:       alt1
#Summary:       Extends the paint gem to support custom color shortcuts documentation files
#Summary(ru_RU.UTF-8): Файлы сведений для самоцвета paint-shortcuts
#Group:         Development/Documentation
#BuildArch:     noarch
#
#Requires:      gem(paint-shortcuts) = 2.2.1
#
#%description   -n gem-paint-shortcuts-doc
#Extends the paint gem to support custom color shortcuts documentation files.
#
#%description   -n gem-paint-shortcuts-doc -l ru_RU.UTF-8
#Файлы сведений для самоцвета paint-shortcuts.
#
#
#%package       -n gem-paint-shortcuts-devel
#Version:       2.2.1
#Release:       alt1
#Summary:       Extends the paint gem to support custom color shortcuts development package
#Summary(ru_RU.UTF-8): Файлы для разработки самоцвета paint-shortcuts
#Group:         Development/Ruby
#BuildArch:     noarch
#
#Requires:      gem(paint-shortcuts) = 2.2.1
#
#%description   -n gem-paint-shortcuts-devel
#Extends the paint gem to support custom color shortcuts development package.
#
#%description   -n gem-paint-shortcuts-devel -l ru_RU.UTF-8
#Файлы для разработки самоцвета paint-shortcuts.
#
#
%package       -n gem-paint-doc
Version:       2.2.1
Release:       alt1
Summary:       Ruby gem for ANSI terminal colors documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета paint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(paint) = 2.2.1

%description   -n gem-paint-doc
Ruby gem for ANSI terminal colors documentation files.

Paint creates terminal colors and effects for you. It combines the strengths of
term-ansicolor, rainbow, and similar projects into a simple to use, however
still flexible terminal colors gem with no core extensions by default.

%description   -n gem-paint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета paint.


%package       -n gem-paint-devel
Version:       2.2.1
Release:       alt1
Summary:       Ruby gem for ANSI terminal colors development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета paint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(paint) = 2.2.1
Requires:      gem(rspec) >= 3.2 gem(rspec) < 4
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(benchmark-ips) >= 2.7 gem(benchmark-ips) < 3
Requires:      gem(rainbow) >= 3.0 gem(rainbow) < 4
Requires:      gem(term-ansicolor) >= 1.7 gem(term-ansicolor) < 2
Requires:      gem(ansi) >= 1.5 gem(ansi) < 2
Requires:      gem(hansi) >= 0.2 gem(hansi) < 1
Requires:      gem(pastel) >= 0.7 gem(pastel) < 1

%description   -n gem-paint-devel
Ruby gem for ANSI terminal colors development package.

Paint creates terminal colors and effects for you. It combines the strengths of
term-ansicolor, rainbow, and similar projects into a simple to use, however
still flexible terminal colors gem with no core extensions by default.

%description   -n gem-paint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета paint.


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

#%files         -n gem-paint-shortcuts
#%doc README.md
#%ruby_gemspecdir/paint-shortcuts-2.2.1.gemspec
#%ruby_gemslibdir/paint-shortcuts-2.2.1
#
#%files         -n gem-paint-shortcuts-doc
#%doc README.md
#%ruby_gemsdocdir/paint-shortcuts-2.2.1
#
#%files         -n gem-paint-shortcuts-devel
#%doc README.md
#
%files         -n gem-paint-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-paint-devel
%doc README.md


%changelog
* Fri Jul 16 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- ^ 2.1.1 -> 2.2.1

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- update (^) 2.1.0 -> v2.1.1
- fix (!) spec

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Bump to 2.1.0
- Use Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
