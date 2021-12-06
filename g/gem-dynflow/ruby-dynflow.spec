%define        gemname dynflow

Name:          gem-dynflow
Version:       1.6.1
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
Patch:         1.4.7.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(msgpack) >= 1.3.3 gem(msgpack) < 1.4
BuildRequires: gem(apipie-params) >= 0
BuildRequires: gem(algebrick) >= 0.7.0 gem(algebrick) < 0.8
BuildRequires: gem(concurrent-ruby) >= 1.1.3 gem(concurrent-ruby) < 1.2
BuildRequires: gem(concurrent-ruby-edge) >= 0.6.0 gem(concurrent-ruby-edge) < 0.7
BuildRequires: gem(sequel) >= 4.0.0
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names pages
Requires:      gem(multi_json) >= 0
Requires:      gem(msgpack) >= 1.3.3 gem(msgpack) < 1.4
Requires:      gem(apipie-params) >= 0
Requires:      gem(algebrick) >= 0.7.0 gem(algebrick) < 0.8
Requires:      gem(concurrent-ruby) >= 1.1.3 gem(concurrent-ruby) < 1.2
Requires:      gem(concurrent-ruby-edge) >= 0.6.0 gem(concurrent-ruby-edge) < 0.7
Requires:      gem(sequel) >= 4.0.0
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR
Provides:      gem(dynflow) = 1.6.1


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
Version:       1.6.1
Release:       alt1
Summary:       DYNamic workFLOW orchestration engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dynflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dynflow) = 1.6.1

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
Version:       1.6.1
Release:       alt1
Summary:       DYNamic workFLOW orchestration engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dynflow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dynflow) = 1.6.1
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
Version:       1.6.1
Release:       alt1
Summary:       DYNamic workFLOW engine executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета dynflow
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(dynflow) = 1.6.1
Requires:      gem-dynflow = %EVR

%description   -n dynflow
Ruby workflow/orchestration engine


%prep
%setup
%patch

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
