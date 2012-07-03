%def_with exec
%def_without mrsh
%def_without qshell
%def_without mqshell
%def_with readline
%def_without nodeupdown
%def_without genders
%def_with pam
%def_without slurm
%def_with ssh
%def_with rsh
%def_with machines

Name: pdsh
Version: 2.26
Release: alt2

Summary: Parallel remote shell program
License: GPL
Group: System/Base

Url: http://sourceforge.net/projects/pdsh
Source0: http://dl.sourceforge.net/sourceforge/pdsh/%name-%version.tar.bz2
Source1: dshdir.pl
Source2: dshdir.1
Source100: pdsh.watch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: pdsh-rcmd

%{?_with_mrsh:BuildRequires: munge-devel}
%{?_with_qshell:BuildRequires: qsnetlibs}
%{?_with_mqshell:BuildRequires: qsnetlibs}
%{?_with_readline:BuildRequires: readline-devel}
%{?_with_readline:BuildRequires: libncurses-devel}
%{?_with_nodeupdown:BuildRequires: whatsup}
%{?_with_genders:BuildRequires: genders > 1.0}
%{?_with_pam:BuildRequires: libpam-devel}
%{?_with_slurm:BuildRequires: libslurm-devel}

##############################################################################
# Pdsh description

# Automatically added by buildreq on Wed Jan 13 2010
BuildRequires: gcc-c++

%description
Pdsh is a multithreaded remote shell client which executes commands
on multiple remote hosts in parallel.  Pdsh can use several different
remote shell services, including standard "rsh", Kerberos IV, and ssh.
##############################################################################

%package qshd
Summary: Remote shell daemon for pdsh/qshell/Quadrics QsNet
Group: System/Base
Requires: xinetd
%description qshd
Remote shell service for running Quadrics QsNet jobs under pdsh.
Sets up Elan capabilities and environment variables needed by Quadrics
MPICH executables.
##############################################################################

%package mqshd
Summary: Remote shell daemon for pdsh/mqshell/Quadrics QsNet
Group: System/Base
Requires: xinetd
%description mqshd
Remote shell service for running Quadrics QsNet jobs under pdsh with
mrsh authentication.  Sets up Elan capabilities and environment variables
needed by Quadrics MPICH executables.
##############################################################################

#
# Module packages:
#
%package rcmd-rsh
Summary: Provides bsd rcmd capability to pdsh
Group: System/Base
Provides: pdsh-rcmd
Autoreq: yes, noruby
%description rcmd-rsh
Pdsh module for bsd rcmd functionality. Note: This module
requires that the pdsh binary be installed setuid root.

%package rcmd-ssh
Summary: Provides ssh rcmd capability to pdsh
Group: System/Base
Provides: pdsh-rcmd
Autoreq: yes, noruby

%description rcmd-ssh
Pdsh module for ssh rcmd functionality.

%package rcmd-qshell
Summary: Provides qshell rcmd capability to pdsh
Group: System/Base
Provides: pdsh-rcmd
Conflicts: pdsh-rcmd-mqshell
%description rcmd-qshell
Pdsh module for running QsNet MPI jobs. Note: This module
requires that the pdsh binary be installed setuid root.

%package rcmd-mrsh
Summary: Provides mrsh rcmd capability to pdsh
Group: System/Base
Provides: pdsh-rcmd
%description rcmd-mrsh
Pdsh module for mrsh rcmd functionality.

%package rcmd-mqshell
Summary: Provides mqshell rcmd capability to pdsh
Group: System/Base
Provides: pdsh-rcmd
Conflicts: pdsh-rcmd-qshell
%description rcmd-mqshell
Pdsh module for mqshell rcmd functionality.

%package rcmd-xcpu
Summary: Provides xcpu rcmd capability to pdsh
Group: System/Base
Provides: pdsh-xcpu
%description rcmd-xcpu
Pdsh module for xcpu rcmd functionality.

%package rcmd-exec
Summary: Provides arbitrary command execution "rcmd" method to pdsh
Group: System/Base
Provides: pdsh-rcmd
Autoreq: yes, noruby
%description rcmd-exec
Pdsh module for generic exec capability. This module allows
execution of an arbitrary command line for each target host in
place of a more specific rcmd connect method (i.e. ssh, rsh, etc.).
The command executed for each host is built from the pdsh
"remote" command line: The first remote argument is the command
to execute, followed by any arguments including "%%h", "%%u", and
"%%n", which are the remote target, username, and rank respectively.

%package mod-genders
Summary: Provides libgenders support for pdsh
Group: System/Base
Requires: genders >= 1.1
Conflicts: pdsh-mod-nodeattr
Conflicts: pdsh-mod-machines
%description mod-genders
Pdsh module for libgenders functionality.

%package mod-nodeattr
Summary: Provides genders support for pdsh using the nodeattr program
Group: System/Base
Requires: genders
Conflicts: pdsh-mod-genders
Conflicts: pdsh-mod-machines
%description mod-nodeattr
Pdsh module for genders functionality using the nodeattr program.

%package mod-nodeupdown
Summary: Provides libnodeupdown support for pdsh
Group: System/Base
Requires: whatsup
%description mod-nodeupdown
Pdsh module providing -v functionality using libnodeupdown.

%package mod-rms
Summary: Provides RMS support for pdsh
Group: System/Base
Requires: qsrmslibs
%description mod-rms
Pdsh module providing support for gathering the list of target nodes
from an allocated RMS resource.

%package mod-machines
Summary: Pdsh module for gathering list of target nodes from a machines file
Group: System/Base
Autoreq: yes, noruby
%description mod-machines
Pdsh module for gathering list of all target nodes from a machines file.

%package mod-dshgroup
Summary: Provides dsh-style group file support for pdsh
Group: System/Base
%description mod-dshgroup
Pdsh module providing dsh (Dancer's shell) style "group" file support.
Provides -g groupname and -X groupname options to pdsh.

%package mod-netgroup
Summary: Provides netgroup support for pdsh
Group: System/Base
%description mod-netgroup
Pdsh module providing support for targeting hosts based on netgroup.
Provides -g groupname and -X groupname options to pdsh.

%package mod-slurm
Summary: Provides support for running pdsh under SLURM allocations
Group: System/Base
Requires: slurm
Autoreq: yes, noruby
%description mod-slurm
Pdsh module providing support for gathering the list of target nodes
from an allocated SLURM job.

##############################################################################

%prep
%setup
##############################################################################

%build
%configure --program-prefix=%{?_program_prefix:%_program_prefix} \
%{?_enable_debug}       \
%{?_with_pam}           \
%{?_without_pam}        \
%{?_with_rsh}           \
%{?_without_rsh}        \
%{?_with_ssh}           \
%{?_without_ssh}        \
%{?_with_exec}          \
%{?_without_exec}       \
%{?_with_qshell}        \
%{?_without_qshell}     \
%{?_with_readline}      \
%{?_without_readline}   \
%{?_with_machines}      \
%{?_without_machines}   \
%{?_with_genders}       \
%{?_without_genders}    \
%{?_with_rms}           \
%{?_without_rms}        \
%{?_with_nodeupdown}    \
%{?_without_nodeupdown} \
%{?_with_nodeattr}      \
%{?_without_nodeattr}   \
%{?_with_mrsh}          \
%{?_without_mrsh}       \
%{?_with_mqshell}       \
%{?_without_mqshell}    \
%{?_with_xcpu}       \
%{?_without_xcpu}    \
%{?_with_slurm}         \
%{?_without_slurm}      \
%{?_with_dshgroups}     \
%{?_without_dshgroups}  \
%{?_with_netgroup}      \
%{?_without_netgroup}

# FIXME: build fails when trying to build with _smp_mflags if qsnet is enabled
# make %_smp_mflags CFLAGS="$RPM_OPT_FLAGS"
%make CFLAGS="%optflags"
##############################################################################

%install
%makeinstall_std
if [ -x %buildroot%_sbindir/in.qshd ]; then
   install -pDm644 etc/qshell.xinetd %buildroot%_sysconfdir/xinetd.d/qshell
fi
if [ -x %buildroot%_sbindir/in.mqshd ]; then
   install -pDm644 etc/mqshell.xinetd %buildroot%_sysconfdir/xinetd.d/mqshell
fi

#
# Remove all module .a's as they are not needed on any known RPM platform.
rm %buildroot%_libdir/pdsh/*.a
rm %buildroot%_libdir/pdsh/*.la

# add dshdir script/manpage
install -pDm755 %SOURCE1 %buildroot%_bindir/dshdir
install -pDm644 %SOURCE1 %buildroot%_man1dir/dshdir.1

##############################################################################

##############################################################################

%files
%doc COPYING README ChangeLog NEWS DISCLAIMER
%doc README.KRB4 README.modules README.QsNet
%_bindir/pdsh
%_bindir/pdcp
%_bindir/rpdcp
%_bindir/dshbak
%_bindir/dshdir
%_man1dir/*
##############################################################################

%if %{?_with_exec:1}%{!?_with_exec:0}
%files rcmd-exec
%_libdir/pdsh/execcmd.*
%endif
##############################################################################

%if %{?_with_rsh:1}%{!?_with_rsh:0}
%files rcmd-rsh
%_libdir/pdsh/xrcmd.*
%endif
##############################################################################

%if %{?_with_ssh:1}%{!?_with_ssh:0}
%files rcmd-ssh
%_libdir/pdsh/sshcmd.*
%endif
##############################################################################

%if %{?_with_qshell:1}%{!?_with_qshell:0}
%files rcmd-qshell
%_libdir/pdsh/qcmd.*
%endif
##############################################################################

%if %{?_with_mrsh:1}%{!?_with_mrsh:0}
%files rcmd-mrsh
%_libdir/pdsh/mcmd.*
%endif
##############################################################################

%if %{?_with_mqshell:1}%{!?_with_mqshell:0}
%files rcmd-mqshell
%_libdir/pdsh/mqcmd.*
%endif
##############################################################################

%if %{?_with_xcpu:1}%{!?_with_xcpu:0}
%files rcmd-xcpu
%_libdir/pdsh/xcpucmd.*
%endif
##############################################################################

%if %{?_with_genders:1}%{!?_with_genders:0}
%files mod-genders
%_libdir/pdsh/genders.*
%endif
##############################################################################

%if %{?_with_nodeattr:1}%{!?_with_nodeattr:0}
%files mod-nodeattr
%_libdir/pdsh/nodeattr.*
%endif
##############################################################################

%if %{?_with_nodeupdown:1}%{!?_with_nodeupdown:0}
%files mod-nodeupdown
%_libdir/pdsh/nodeupdown.*
%endif
##############################################################################

%if %{?_with_rms:1}%{!?_with_rms:0}
%files mod-rms
%_libdir/pdsh/rms.*
%endif
##############################################################################

%if %{?_with_machines:1}%{!?_with_machines:0}
%files mod-machines
%_libdir/pdsh/machines.*
%endif
##############################################################################

%if %{?_with_dshgroups:1}%{!?_with_dshgroups:0}
%files mod-dshgroup
%_libdir/pdsh/dshgroup.*
%endif
##############################################################################

%if %{?_with_netgroup:1}%{!?_with_netgroup:0}
%files mod-netgroup
%_libdir/pdsh/netgroup.*
%endif
##############################################################################

%if %{?_with_slurm:1}%{!?_with_slurm:0}
%files mod-slurm
%_libdir/pdsh/slurm.*
%endif
##############################################################################

%if %{?_with_qshell:1}%{!?_with_qshell:0}
%files qshd
%_sbindir/in.qshd
%_sysconfdir/xinetd.d/qshell

%post qshd
if ! grep "^qshell" %_sysconfdir/services >/dev/null; then
  echo "qshell            523/tcp                  # pdsh/qshell/Quadrics QsNet" >>%_sysconfdir/services
fi
%_initdir/xinetd reload

%endif
##############################################################################

%if %{?_with_mqshell:1}%{!?_with_mqshell:0}
%files mqshd
%_sbindir/in.mqshd
%_sysconfdir/xinetd.d/mqshell

%post mqshd
if ! grep "^mqshell" %_sysconfdir/services >/dev/null; then
  echo "mqshell         21234/tcp                  # pdsh/mqshell/Quadrics QsNet" >>%_sysconfdir/services
fi
%_initdir/xinetd reload

%endif
##############################################################################

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 2.26-alt2
- added watch file

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 2.26-alt1
- 2.26

* Thu Mar 10 2011 Michael Shigorin <mike@altlinux.org> 2.25-alt1
- 2.25

* Tue Mar 1 2011 Michael Shigorin <mike@altlinux.org> 2.24-alt1
- 2.24 (our contribs merged upstream)

* Fri Feb 25 2011 Michael Shigorin <mike@altlinux.org> 2.22-alt2
- added dshdir output processing script by Alexander Bandura
  (splits it into node-specific files in a directory)

* Sun Sep 19 2010 Michael Shigorin <mike@altlinux.org> 2.22-alt1
- 2.22

* Fri Jul 09 2010 Michael Shigorin <mike@altlinux.org> 2.18-alt1
- TMC package rebuilt for Sisyphus
- minor spec cleanup
- disabled slurm subpackage in the meanwhile
