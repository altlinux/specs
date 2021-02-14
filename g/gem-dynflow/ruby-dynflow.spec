%define        pkgname dynflow

Name:          gem-%pkgname
Version:       1.4.7
Release:       alt2
Summary:       DYNamic workFLOW orchestration engine
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Dynflow/dynflow
Vcs:           https://github.com/Dynflow/dynflow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       %{pkgname}
Source2:       %{pkgname}.sysconfig
Source3:       %{pkgname}.service
Patch:         %version.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Dynflow [DYN(amic work)FLOW] is a workflow engine written in Ruby that allows to

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


%description -l ru_RU.UTF8
Движок для управления динамическим рабочим потоком.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n %{pkgname}
Summary:       HTML, XML, SAX, and Reader parser
Group:         Development/Other
BuildArch:     noarch

Requires:      %name = %EVR

%description   -n %{pkgname}
Executable service file for %gemname gem.

%description   -n %{pkgname} -l ru_RU.UTF8
Служебная исполнямка для %gemname самоцвета.


%prep
%setup
%patch

%build
%ruby_build --ignore=pages --use=%gemname

%install
%ruby_install
install -Dm0755 %SOURCE1 %buildroot%_sbindir/%{pkgname}
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/dynflow
install -Dm0644 %SOURCE3 %buildroot%_unitdir/dynflow.service
mkdir -p %buildroot%_sharedstatedir/%pkgname %buildroot%_logdir/%pkgname %buildroot/run/%pkgname

%check
%ruby_test

%pre           -n %{pkgname}
# Add the "dynflow" user and group
getent group dynflow >/dev/null || %_sbindir/groupadd -r dynflow
getent passwd _dynflow >/dev/null || \
   %_sbindir/useradd -r -g dynflow -d %_sharedstatedir/%{pkgname} -s /bin/bash -c "Dynflow service" _dynflow
exit 0

%post          -n %{pkgname}
%post_service dynflow

%preun         -n %{pkgname}
%preun_service dynflow


%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %{pkgname}
%_sbindir/%{pkgname}
%_unitdir/%{pkgname}.service
%config(noreplace) %_sysconfdir/sysconfig/%{pkgname}
%attr(770,_dynflow,dynflow) %_sharedstatedir/%{pkgname}
%attr(770,_dynflow,dynflow) %_logdir/%pkgname
%attr(770,_dynflow,dynflow) /run/%pkgname


%changelog
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
