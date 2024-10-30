Name:           jobclient
Version:        2022.6
Release:        alt1
Source:         %name-%version.tar
Source1:        jobclient.1.scd
Source2:        jobcount.1.scd
Source3:        jobforce.1.scd
Source4:        jobserver.1.scd
License:        MIT
URL:            https://github.com/olsner/jobclient
Summary:        GNU Make jobserver and jobclient
Group:          Development/Other

# Automatically added by buildreq on Wed Oct 30 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error python3-base sh5
BuildRequires: python3 scdoc

%description
Primarily, this allows shell scripts and other software to submit jobs
to a running Make job server, waiting for free slots (usually
corresponding to CPUs) to become available before they start.

To submit a job, instead of running your command directly, prepend
jobclient to it and run it in the background. The jobclient utility will
contact the job server, wait for a free job slot (without using CPU),
then launch the command given as its arguments.

%prep
%setup

%build
%make CFLAGS+=-g
for F in %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4; do
  scdoc < $F > $(basename "$F" .scd)
done

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install jobclient jobcount jobforce jobserver %buildroot%_bindir/
install -m644 *.1  %buildroot%_man1dir/

%files
%doc README.md
%_bindir/*
%_man1dir/*

%changelog
* Wed Oct 30 2024 Fr. Br. George <george@altlinux.org> 2022.6-alt1
- Initial build for ALT
