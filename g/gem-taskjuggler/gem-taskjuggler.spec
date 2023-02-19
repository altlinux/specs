%define        gemname taskjuggler

Name:          gem-taskjuggler
Version:       3.7.1.19
Release:       alt0.1
Summary:       TaskJuggler - Project Management beyond Gantt chart drawing
License:       GPL-2.0
Group:         Office
Url:           http://www.taskjuggler.org
Vcs:           https://github.com/taskjuggler/taskjuggler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       taskjuggler.rc
Source2:       tj3d.service
Source3:       tj3webd.service
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(mail) >= 2.7.1
BuildRequires: gem(term-ansicolor) >= 1.7.1
BuildRequires: gem(rspec) >= 2.5
BuildConflicts: gem(mail) >= 3
BuildConflicts: gem(term-ansicolor) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(mail) >= 2.7.1
Requires:      gem(term-ansicolor) >= 1.7.1
Conflicts:     gem(mail) >= 3
Conflicts:     gem(term-ansicolor) >= 2
Obsoletes:     taskjuggler < %EVR
Provides:      taskjuggler = %EVR
Provides:      gem(taskjuggler) = 3.7.1.19

%ruby_use_gem_version taskjuggler:3.7.1.19

%description
TaskJuggler is a modern and powerful project management tool. Its new approach
to project planning and tracking is far superior to the commonly used Gantt
chart editing tools. It has already been successfully used in many projects and
scales easily to projects with hundreds of resources and thousands of tasks. It
covers the complete spectrum of project management tasks from the first idea to
the completion of the project. It assists you during project scoping, resource
assignment, cost and revenue planning, and risk and communication management.


%package       -n taskjuggler
Version:       3.7.1.19
Release:       alt0.1
Summary:       TaskJuggler - Project Management beyond Gantt chart drawing executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета taskjuggler
Group:         Other
BuildArch:     noarch

Requires:      gem(taskjuggler) = 3.7.1.19

%description   -n taskjuggler
TaskJuggler - Project Management beyond Gantt chart drawing
executable(s).

TaskJuggler is a modern and powerful project management tool. Its new approach
to project planning and tracking is far superior to the commonly used Gantt
chart editing tools. It has already been successfully used in many projects and
scales easily to projects with hundreds of resources and thousands of tasks. It
covers the complete spectrum of project management tasks from the first idea to
the completion of the project. It assists you during project scoping, resource
assignment, cost and revenue planning, and risk and communication management.

%description   -n taskjuggler -l ru_RU.UTF-8
Исполнямка для самоцвета taskjuggler.


%package       -n gem-taskjuggler-doc
Version:       3.7.1.19
Release:       alt0.1
Summary:       TaskJuggler - Project Management beyond Gantt chart drawing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета taskjuggler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(taskjuggler) = 3.7.1.19

%description   -n gem-taskjuggler-doc
TaskJuggler - Project Management beyond Gantt chart drawing documentation
files.

TaskJuggler is a modern and powerful project management tool. Its new approach
to project planning and tracking is far superior to the commonly used Gantt
chart editing tools. It has already been successfully used in many projects and
scales easily to projects with hundreds of resources and thousands of tasks. It
covers the complete spectrum of project management tasks from the first idea to
the completion of the project. It assists you during project scoping, resource
assignment, cost and revenue planning, and risk and communication management.

%description   -n gem-taskjuggler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета taskjuggler.


%package       -n gem-taskjuggler-devel
Version:       3.7.1.19
Release:       alt0.1
Summary:       TaskJuggler - Project Management beyond Gantt chart drawing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета taskjuggler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(taskjuggler) = 3.7.1.19
Requires:      gem(rspec) >= 2.5

%description   -n gem-taskjuggler-devel
TaskJuggler - Project Management beyond Gantt chart drawing development
package.

TaskJuggler is a modern and powerful project management tool. Its new approach
to project planning and tracking is far superior to the commonly used Gantt
chart editing tools. It has already been successfully used in many projects and
scales easily to projects with hundreds of resources and thousands of tasks. It
covers the complete spectrum of project management tasks from the first idea to
the completion of the project. It assists you during project scoping, resource
assignment, cost and revenue planning, and risk and communication management.

%description   -n gem-taskjuggler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета taskjuggler.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n taskjuggler
%doc README.rdoc
%_bindir/tj3
%_bindir/tj3client
%_bindir/tj3d
%_bindir/tj3man
%_bindir/tj3ss_receiver
%_bindir/tj3ss_sender
%_bindir/tj3ts_receiver
%_bindir/tj3ts_sender
%_bindir/tj3ts_summary
%_bindir/tj3webd

%files         -n gem-taskjuggler-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-taskjuggler-devel
%doc README.rdoc


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 3.7.1.19-alt0.1
- ^ 3.7.1[1] -> 3.7.1p19

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
