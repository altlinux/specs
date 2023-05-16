Name: clusterssh
Version: 4.16
Release: alt1

Summary: Run commands on multiple servers over ssh
Group: Networking/Remote access
License: %gpl2plus
Url: https://github.com/duncs/clusterssh
Source: %name-%version.tar
BuildRequires: rpm-build-licenses

BuildPreReq: perl-base perl(Config/Simple.pm) perl(Fcntl.pm) perl-devel
BuildPreReq: perl(File/Basename.pm), perl(File/Temp.pm), perl(FindBin.pm), perl(Getopt/Std.pm)
BuildPreReq: perl(POSIX.pm), perl(Sys/Hostname.pm), perl(Term/Cap.pm), perl(Tk.pm) >= 0:800.022
BuildPreReq: perl(Tk/Dialog.pm), perl(Tk/LabEntry.pm), perl-X11-Protocol
BuildRequires: perl(Module/Build.pm), perl(Locale/Maketext.pm), perl(Exception/Class.pm)
BuildRequires: perl(Try/Tiny.pm), perl(Net/Domain.pm), perl(X11/Protocol/WM.pm)

BuildRequires: perl(Test/Trap.pm), perl(File/Which.pm), perl(Test/Differences.pm), perl(Readonly.pm)

BuildArch: noarch
BuildRequires: perl-Pod-Parser perl-Pod-Checker

Requires: perl-podlators

%description
ClusterSSH controls a number of xterm windows via
a single graphical console window to allow commands
to be interactively run on multiple servers over
an ssh connection.

%prep
%setup -q

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0

mkdir -p %buildroot/%_datadir/bash-completion/completions
mv  %buildroot/%_bindir/clusterssh_bash_completion.dist \
        %buildroot/%_datadir/bash-completion/completions/clusterssh

%files
%doc AUTHORS README THANKS Changes
%_bindir/*
%_man1dir/*.*
%perl_vendor_privlib/*
%_datadir/bash-completion/completions/*

%changelog
* Tue May 16 2023 Anton Farygin <rider@altlinux.ru> 4.16-alt1
- 3.28 -> 4.16

* Tue Nov 18 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.28-alt2
- Added perl-podlators to Requires
- Used rpm-build-licenses

* Fri Dec 20 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.28-alt1
- 3.28 release.
- Added perl-Pod-Checker to BuildRequires

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 3.24-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Mar 13 2009 Pavlov Konstantin <thresh@altlinux.ru> 3.24-alt2
- Provide crsh and ctel symlinks (fixes #15713).
- Provide desktop file and icons (fixes #15533).

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 3.24-alt1
- 3.24 release.

* Thu Mar 13 2008 Pavlov Konstantin <thresh@altlinux.ru> 3.22-alt1
- 3.22 release.

* Mon Dec 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 3.21-alt1
- 3.21 release.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 3.19.1-alt1
- 3.19.1 release.

* Tue Nov 09 2004 Leonid Shalupov <shalupov@altlinux.ru> 2.17-alt1
- Initial build
