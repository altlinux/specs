%define        gemname daemons

Name:          gem-daemons
Version:       1.4.1
Release:       alt1
Summary:       A toolkit to create and control daemons in different ways
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thuehlinger/daemons
Vcs:           https://github.com/thuehlinger/daemons.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 12.3
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(pry-byebug) >= 3.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(pry-byebug) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Obsoletes:     ruby-daemons < %EVR
Provides:      ruby-daemons = %EVR
Provides:      gem(daemons) = 1.4.1


%description
Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server) to be run as a daemon and to be controlled by simple
start/stop/restart commands.

You can also call blocks as daemons and control them from the parent or just
daemonize the current process.

Besides this basic functionality, daemons offers many advanced features like
exception backtracing and logging (in case your ruby script crashes) and
monitoring and automatic restarting of your processes if they crash.


%package       -n gem-daemons-doc
Version:       1.4.1
Release:       alt1
Summary:       A toolkit to create and control daemons in different ways documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета daemons
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(daemons) = 1.4.1

%description   -n gem-daemons-doc
A toolkit to create and control daemons in different ways documentation
files.

Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server) to be run as a daemon and to be controlled by simple
start/stop/restart commands.

You can also call blocks as daemons and control them from the parent or just
daemonize the current process.

Besides this basic functionality, daemons offers many advanced features like
exception backtracing and logging (in case your ruby script crashes) and
monitoring and automatic restarting of your processes if they crash.

%description   -n gem-daemons-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета daemons.


%package       -n gem-daemons-devel
Version:       1.4.1
Release:       alt1
Summary:       A toolkit to create and control daemons in different ways development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета daemons
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(daemons) = 1.4.1
Requires:      gem(rake) >= 12.3
Requires:      gem(rspec) >= 3.1
Requires:      gem(simplecov) >= 0
Requires:      gem(pry-byebug) >= 3.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(pry-byebug) >= 4

%description   -n gem-daemons-devel
A toolkit to create and control daemons in different ways development
package.

Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server) to be run as a daemon and to be controlled by simple
start/stop/restart commands.

You can also call blocks as daemons and control them from the parent or just
daemonize the current process.

Besides this basic functionality, daemons offers many advanced features like
exception backtracing and logging (in case your ruby script crashes) and
monitoring and automatic restarting of your processes if they crash.

%description   -n gem-daemons-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета daemons.


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

%files         -n gem-daemons-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-daemons-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.4.0 -> 1.4.1

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.1 -> 1.4.0

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- ^ 1.2.6 -> 1.3.1
- > Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.1.0-alt1
- [1.1.0]

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.10-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 1.0.10-alt1
- Built for Sisyphus
