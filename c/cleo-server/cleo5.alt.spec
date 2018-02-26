Summary: Cleo batch system. Server part.
Name: cleo-server
Version: 5.13a
Release: alt2.1
License: GPL
Group: System/Servers
Source: cleo-%{version}.tgz

%define _perl_lib_path %_libexecdir/cleo

# Automatically added by buildreq on Thu Mar 13 2008 (-bi)
BuildRequires: fakeroot perl-Storable perl4-compat
BuildRequires: perl-Tie-RefHash

%description
  Cleo is the batch system for computing clusters. This package contains
server components, default scheduler and base client programs.
 

%package -n cleo-agent
Summary: Cleo batch system. Agent part.
Group: System/Servers

%description -n cleo-agent
  Cleo is the batch system for computing clusters. This package contains                                                                         
host agent components.

%package -n cleo-common
Summary: Cleo batch system. Common files.
Group: System/Servers

%description -n cleo-common
  Cleo is the batch system for computing clusters. This package contains                                                                         
files, used by all cleo components.

%prep
%setup -q -n cleo-%version
#%patch0 -p1
#%patch1 -p1

%build
make RCDIR=%_initdir

%install
fakeroot make DESTDIR=%buildroot RCDIR=%_initdir install \
	{,MAN}USER=root {,MAN}GROUP=root

%files -n cleo-server
%doc README COPYING
#%doc cleo-%version/man/ant-mon.1
%_sbindir/cleo
/etc/cleo.conf
#/etc/sysconfig/cleo
%_initdir/cleo
%_sbindir/cleo-mode
%_bindir/cleo-autoblock
%_bindir/cleo-blockcpu
%_bindir/cleo-blocktask
%_bindir/cleo-client
%_bindir/cleo-priority
%_bindir/cleo-stat
%_bindir/cleo-terminal
%_bindir/cleo-freeze
%_bindir/empty-cleo
%_docdir/cleo/cleo.conf.example
%_docdir/cleo/cleo.conf.example-mpich
%_docdir/cleo/cleo.conf.example-mvs
%_docdir/cleo/cleo.conf.example-sci
%_docdir/cleo/example-sceduler
%_perl_lib_path/cleosupport.pm
%_perl_lib_path/cleovars.pm
%_perl_lib_path/base_sced
%_bindir/mpirun
%_bindir/tasks
%_mandir/man1/cleo-autoblock.1.gz
%_mandir/man1/cleo-blockcpu.1.gz
%_mandir/man1/cleo-blocktask.1.gz
%_mandir/man1/cleo-mode.1.gz
%_mandir/man1/cleo-freeze.1.gz
%_mandir/man1/cleo-priority.1.gz
%_mandir/man1/mpirun.1.gz
%_mandir/man1/tasks.1.gz

%_docdir/cleo/Admguide.pdf
%_docdir/cleo/CleoOptions.doc
%_docdir/cleo/Extern-shuffle.txt
%_docdir/cleo/LICENSE
%_docdir/cleo/COPYING
%_docdir/cleo/Modules-howto
%_docdir/cleo/README
%_docdir/cleo/README-empty
%_docdir/cleo/README-sceduler-create
%_docdir/cleo/doubler_sced

%files -n cleo-agent
%_initdir/cleo-mon
%_sbindir/cleo-mon

%files -n cleo-common
%_perl_lib_path/Cleo/Conn.pm

%changelog
* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 5.13a-alt2.1
- rebuilt with perl 5.12

* Mon Sep 22 2008 Sergey Zhumatiy <zhum@altlinux.org> 5.13a-alt2
- cleo-blockcpu fixed

* Fri Aug 22 2008 Sergey Zhumatiy <zhum@altlinux.org> 5.13a-alt1
- cpu-per-hour limit added

* Thu Jul 24 2008 Sergey Zhumatiy <zhum@altlinux.org> 5.12c-alt4
- Logrotate added
- Unique task identificators initially added

* Tue Mar 25 2008 Sergey Zhumatiy <zhum@altlinux.org> 5.12-alt3
- Compatibility dependencies added

* Mon Mar 24 2008 Sergey Zhumatiy <zhum@altlinux.org> 5.12-alt2
- Minor optimizations

* Thu Mar 13 2008 Sergey Zhumatiy <zhum@altlinux.org> 5.12-alt1
- Initial build
