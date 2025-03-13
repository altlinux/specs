%def_with check

%global descr These small utilities allow creating very lightweight job queue\
systems which require no setup, maintenance, supervision, or any\
long-running processes.\
\
The intended purpose is ad-hoc queuing of command lines (e.g., for\
building several targets of a Makefile, downloading multiple files one\
at a time, running benchmarks in several configurations, or simply as\
a glorified nohup). But as any good Unix tool, it can be abused for\
whatever you like.\
\
Job order is enforced by a timestamp nq gets immediately when\
started.  Synchronization happens on file-system level.  Timer\
resolution is milliseconds.  No sub-second file system time stamps are\
required.  Polling is not used.  Exclusive execution is maintained\
strictly.\
\
Enforcing job order works like this:\
- every job has a flock(2)ed output file, ala ,TIMESTAMP.PID\
- every job starts only after all earlier flock(2)ed files are unlocked\
- Why flock(2)? Because it locks the file handle, which is shared\
  across exec(2) with the child process (the actual job), and it will\
  unlock when the file is closed (usually when the job terminates).\
\
You enqueue (get it?) new jobs using nq CMDLINE....  The job ID is\
output (unless suppressed using -q) and nq detaches immediately,\
running the job in the background.  STDOUT and STDERR are redirected\
into the log file.\
\
nq tries hard (but does not guarantee) to ensure the log file of the\
currently running job has +x bit set.  Thus you can use ls -F to get\
a quick overview of the state of your queue.\
\
The "file extension" of the log file is actually the PID, so you can\
kill jobs easily.  Before the job is started, it is the PID of nq,\
so you can cancel a queued job by killing it as well.\
\
Due to the initial exec line in the log files, you can resubmit a\
job by executing it as a shell command file (i.e. running sh $jobid).\
\
You can wait for jobs to finish using nq -w, possibly listing job\
IDs you want to wait for; the default is all of them.  Likewise, you\
can test if there are jobs which need to be waited upon using -t.\
\
By default, job IDs are per-directory, but you can set $NQDIR to put\
them elsewhere.  Creating nq wrappers setting $NQDIR to provide\
different queues for different purposes is encouraged.\
\
All these operations take worst-case quadratic time in the amount of\
lock files produced, so you should clean them regularly.

Name: nq
Version: 1.0
Release: alt1

Summary: UNIX command line queue utility
License: CC0-1.0
Group: Other
Url: https://github.com/leahneukirchen/nq
Vcs: https://github.com/leahneukirchen/nq

Source: %name-%version.tar

%if_with check
BuildRequires: perl-devel
%endif

%description
%descr

%package scripts
Summary: Two helper scripts for nq
Group: Other
Requires: nq = %EVR
%filter_from_requires /screen/d
%filter_from_requires /tmux/d

%description scripts
Two helper programs are provided:

nqtail outputs the log of the currently running jobs, exiting
when the jobs are done.  If no job is running, the output of the last
job is shown.  nqtail -a shows the output of all jobs, nqtail -q
only shows one line per job.  nqtail uses inotify on Linux and
falls back to polling for size change else.  (nqtail.sh is a similar
tool, not quite as robust, implemented as shell-script calling
tail.)

nqterm wraps nq and displays the nqtail output in a new
tmux or screen window.

%prep
%setup

%build
%make_build CC=gcc
xz -k %name.1 %{name}tail.1 %{name}term.1

%install
%makeinstall_std \
	PREFIX=%prefix \
	BINDIR=%_bindir \
	MANDIR=%_mandir
install -Dpm 0644 %name.1.xz %buildroot%_man1dir
install -Dpm 0644 %{name}tail.1.xz %buildroot%_man1dir
install -Dpm 0644 %{name}term.1.xz %buildroot%_man1dir

%check
%make check

%files
%_bindir/%name
%_man1dir/%name.1.xz

%files scripts
%_bindir/%{name}tail
%_bindir/%{name}term
%_man1dir/%{name}tail.1.xz
%_man1dir/%{name}term.1.xz

%changelog
* Fri Feb 21 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0-alt1
- Initial build for Siyphus.
