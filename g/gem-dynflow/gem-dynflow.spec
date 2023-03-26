%define        _unpackaged_files_terminate_build 1
%define        gemname dynflow

Name:          gem-dynflow
Version:       1.6.10
Release:       alt1
Summary:       DYNamic workFLOW orchestration engine
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Dynflow/dynflow
Vcs:           https://github.com/dynflow/dynflow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       dynflow
Source2:       dynflow.sysconfig
Source3:       dynflow.service
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(minitest-stub-const) >= 0
BuildRequires: gem(activerecord) >= 0
BuildRequires: gem(activejob) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(concurrent-ruby-ext) >= 1.1.3
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(sidekiq) >= 0
BuildRequires: gem(gitlab-sidekiq-fetcher) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(mysql2) >= 0
BuildRequires: gem(rubocop) >= 0.39.0
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(daemons) >= 0
BuildRequires: gem(rails) >= 4.2.9
BuildRequires: gem(logging) >= 0
BuildRequires: gem(statsd-instrument) >= 0
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(msgpack) >= 1.3.3
BuildRequires: gem(apipie-params) >= 0
BuildRequires: gem(algebrick) >= 0.7.0
BuildRequires: gem(concurrent-ruby) >= 1.1.3
BuildRequires: gem(concurrent-ruby-edge) >= 0.6.0
BuildRequires: gem(sequel) >= 4.0.0
BuildConflicts: gem(concurrent-ruby-ext) >= 1.2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rails) >= 7
BuildConflicts: gem(msgpack) >= 2
BuildConflicts: gem(algebrick) >= 0.8
BuildConflicts: gem(concurrent-ruby) >= 1.2
BuildConflicts: gem(concurrent-ruby-edge) >= 0.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(multi_json) >= 0
Requires:      gem(msgpack) >= 1.3.3
Requires:      gem(apipie-params) >= 0
Requires:      gem(algebrick) >= 0.7.0
Requires:      gem(concurrent-ruby) >= 1.1.3
Requires:      gem(concurrent-ruby-edge) >= 0.6.0
Requires:      gem(sequel) >= 4.0.0
Conflicts:     gem(msgpack) >= 2
Conflicts:     gem(algebrick) >= 0.8
Conflicts:     gem(concurrent-ruby) >= 1.2
Conflicts:     gem(concurrent-ruby-edge) >= 0.7
Obsoletes:     ruby-dynflow < %EVR
Provides:      ruby-dynflow = %EVR
Provides:      gem(dynflow) = 1.6.10


%description
Dynflow [DYN(amic work)FLOW] is a workflow engine written in Ruby that allows
to:
* keep track of the progress of running process
* run the code asynchronously
* resume the process when something goes wrong, skip some steps when needed
* detect independent parts and run them concurrently
* compose simple actions into more complex scenarios
* extend the workflows from third-party libraries
* keep consistency between local transactional database and external services
* suspend the long-running steps, not blocking the thread pool
* cancel steps when possible
* extend the actions behavior with middlewares
* define the input/output interface between the building blocks (planned)
* define rollback for the workflow (planned)
* have multiple workers for distributing the load (planned)

Dynflow doesn't try to choose the best tool for the jobs, as the right tool
depends on the context. Instead, it provides interfaces for persistence,
transaction layer or executor implementation, giving you the last word in
choosing the right one (providing default implementations as well).


%package       -n gem-dynflow-doc
Version:       1.6.10
Release:       alt1
Summary:       DYNamic workFLOW orchestration engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dynflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dynflow) = 1.6.10

%description   -n gem-dynflow-doc
DYNamic workFLOW orchestration engine documentation files.

Dynflow [DYN(amic work)FLOW] is a workflow engine written in Ruby that allows
to:
* keep track of the progress of running process
* run the code asynchronously
* resume the process when something goes wrong, skip some steps when needed
* detect independent parts and run them concurrently
* compose simple actions into more complex scenarios
* extend the workflows from third-party libraries
* keep consistency between local transactional database and external services
* suspend the long-running steps, not blocking the thread pool
* cancel steps when possible
* extend the actions behavior with middlewares
* define the input/output interface between the building blocks (planned)
* define rollback for the workflow (planned)
* have multiple workers for distributing the load (planned)

Dynflow doesn't try to choose the best tool for the jobs, as the right tool
depends on the context. Instead, it provides interfaces for persistence,
transaction layer or executor implementation, giving you the last word in
choosing the right one (providing default implementations as well).

%description   -n gem-dynflow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dynflow.


%package       -n gem-dynflow-devel
Version:       1.6.10
Release:       alt1
Summary:       DYNamic workFLOW orchestration engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dynflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dynflow) = 1.6.10
Requires:      gem(rake) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(minitest-stub-const) >= 0
Requires:      gem(activerecord) >= 0
Requires:      gem(activejob) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(sinatra) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(concurrent-ruby-ext) >= 1.1.3
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(sidekiq) >= 0
Requires:      gem(gitlab-sidekiq-fetcher) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(mysql2) >= 0
Requires:      gem(rubocop) >= 0.39.0
Requires:      gem(get_process_mem) >= 0
Requires:      gem(daemons) >= 0
Requires:      gem(rails) >= 4.2.9
Requires:      gem(logging) >= 0
Requires:      gem(statsd-instrument) >= 0
Conflicts:     gem(concurrent-ruby-ext) >= 1.2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rails) >= 7

%description   -n gem-dynflow-devel
DYNamic workFLOW orchestration engine development package.

Dynflow [DYN(amic work)FLOW] is a workflow engine written in Ruby that allows
to:
* keep track of the progress of running process
* run the code asynchronously
* resume the process when something goes wrong, skip some steps when needed
* detect independent parts and run them concurrently
* compose simple actions into more complex scenarios
* extend the workflows from third-party libraries
* keep consistency between local transactional database and external services
* suspend the long-running steps, not blocking the thread pool
* cancel steps when possible
* extend the actions behavior with middlewares
* define the input/output interface between the building blocks (planned)
* define rollback for the workflow (planned)
* have multiple workers for distributing the load (planned)

Dynflow doesn't try to choose the best tool for the jobs, as the right tool
depends on the context. Instead, it provides interfaces for persistence,
transaction layer or executor implementation, giving you the last word in
choosing the right one (providing default implementations as well).

%description   -n gem-dynflow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dynflow.


%package       -n dynflow
Version:       1.6.10
Release:       alt1
Summary:       DYNamic workFLOW engine executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета dynflow
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(dynflow) = 1.6.10
Requires:      gem-dynflow = %EVR

%description   -n dynflow
Ruby workflow/orchestration engine


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0755 %SOURCE1 %buildroot%_sbindir/dynflow
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/dynflow
install -Dm0644 %SOURCE3 %buildroot%_unitdir/dynflow.service
mkdir -p %buildroot%_sharedstatedir/dynflow %buildroot%_logdir/dynflow %buildroot/run/dynflow

%check
%ruby_test

%pre           -n dynflow
# Add the "dynflow" user and group
getent group dynflow >/dev/null || %_sbindir/groupadd -r dynflow
getent passwd _dynflow >/dev/null || \
   %_sbindir/useradd -r -g dynflow -d %_sharedstatedir/dynflow -s /bin/bash -c "Dynflow service" _dynflow
exit 0

%post          -n dynflow
%post_service dynflow

%preun         -n dynflow
%preun_service dynflow

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-dynflow-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-dynflow-devel
%doc README.md

%files         -n dynflow
%doc README.md
%_sbindir/dynflow
%_unitdir/dynflow.service
%config(noreplace) %_sysconfdir/sysconfig/dynflow
%attr(770,_dynflow,dynflow) %_sharedstatedir/dynflow
%attr(770,_dynflow,dynflow) %_logdir/dynflow
%attr(770,_dynflow,dynflow) /run/dynflow


%changelog
* Sun Mar 26 2023 Pavel Skrylev <majioa@altlinux.org> 1.6.10-alt1
- ^ 1.6.7 -> 1.6.10

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 1.6.7-alt1
- ^ 1.6.5 -> 1.6.7

* Fri Apr 01 2022 Pavel Skrylev <majioa@altlinux.org> 1.6.5-alt1
- ^ 1.6.1 -> 1.6.5

* Tue Nov 09 2021 Pavel Skrylev <majioa@altlinux.org> 1.6.1-alt1
- ^ 1.4.7 -> 1.6.1
- ! has with indifferent access lost class for rails database env hash

* Wed Feb 10 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.7-alt2
- ! dynflow service to support change of uid during run
- ! spec

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.7-alt1
- ^ 1.4.2 -> 1.4.7
- * policify name
- + dynflow service executable

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- updated (^) 1.3.0 -> 1.4.2

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- v1.2.3-> v1.3.0
- fix spec

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.3-alt1.1
- Fix spec

* Tue Jun 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.3-alt1
- Use Ruby Policy 2.0
- Bump to 1.2.3

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- Initial gemified build for Sisyphus
