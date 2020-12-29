%define        pkgname taskjuggler

Name:          gem-%pkgname
Version:       3.7.1.1
Release:       alt0.1
Summary:       TaskJuggler - Project Management beyond Gantt chart drawing
License:       GPL-2.0
Group:         Office
Url:           http://www.taskjuggler.org
Vcs:           https://github.com/taskjuggler/TaskJuggler.git
BuildArch:     noarch
Autoreq:       yes,noshebang

Source:        %name-%version.tar
Source1:       %{pkgname}.rc
Source2:       tj3d.service
Source3:       tj3webd.service
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(term-ansicolor)
BuildRequires: /usr/bin/md5sum

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %gemname < %EVR

%description
TaskJuggler is a modern and powerful project management tool. Its new
approach to project planning and tracking is far superior to the
commonly used Gantt chart editing tools. It has already been
successfully used in many projects and scales easily to projects with
hundreds of resources and thousands of tasks. It covers the complete
spectrum of project management tasks from the first idea to the
completion of the project. It assists you during project scoping,
resource assignment, cost and revenue planning, and risk and
communication management.


%package       -n %pkgname
Summary:       Executables for TaskJuggler the Project Management beyond Gantt chart drawing
Summary(ru_RU.UTF-8): Библиотечные файлы для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Library for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Библиотечные файлы для %gemname самоцвета.


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
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install
mkdir -p %buildroot%_sysconfdir %buildroot%_logdir/%pkgname
cat %SOURCE1 | sed "s,<hash>,$(md5sum <<< $(tj3d --help) | sed "s/  -.*//")," > %buildroot%_sysconfdir/%{pkgname}.rc
install -Dm755 %SOURCE2 %buildroot%_unitdir/tj3d.service
install -Dm755 %SOURCE3 %buildroot%_unitdir/tj3webd.service

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%doc README*
%_bindir/*
%_sysconfdir/%{pkgname}.rc
%_unitdir/*.service
%_logdir/%pkgname

%files         doc
%ruby_gemdocdir


%changelog
* Thu Dec 29 2020 Pavel Skrylev <majioa@altlinux.org> 3.7.1.1-alt0.1
- ^ 3.7.1 -> 3.7.1[1]
- + services and config
- ! spec

* Thu Dec 24 2020 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.
- Package complete gem.

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Wed Feb 06 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version 3.4.0

* Wed Feb 06 2013 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt2
- Fix build in Sisyphus
- Apply Fedora patches

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.1
- Fixed build

* Sat Mar 05 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- Return to Sisyphus

