Name: clusterssh
Version: 3.24
Release: alt2.1

Summary: Run commands on multiple servers over ssh
Group: Networking/Remote access
License: GPL
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Url: http://clusterssh.sourceforge.net/
Source: clusterssh-%version.tar.gz

# make findrequires happy
# BuildPreReq: perl-base, perl(Config/Simple.pm) >= 0:4.55, perl(Fcntl.pm)
BuildPreReq: perl-base perl(Config/Simple.pm) perl(Fcntl.pm) perl-devel
BuildPreReq: perl(File/Basename.pm), perl(File/Temp.pm), perl(FindBin.pm), perl(Getopt/Std.pm)
BuildPreReq: perl(POSIX.pm), perl(Sys/Hostname.pm), perl(Term/Cap.pm), perl(Tk.pm) >= 0:800.022
BuildPreReq: perl(Tk/Dialog.pm), perl(Tk/LabEntry.pm), perl-X11-Protocol

BuildArch: noarch
BuildRequires: perl-Pod-Parser

%description
ClusterSSH controls a number of xterm windows via
a single graphical console window to allow commands
to be interactively run on multiple servers over
an ssh connection.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

for i in crsh ctel; do
	ln -sf %_bindir/cssh %buildroot%_bindir/$i
done

mkdir -p %buildroot%_datadir/applications
install -pm 644 clusterssh.desktop %buildroot%_datadir/applications/

for i in 24x24 32x32 48x48; do
	mkdir -p %buildroot%_datadir/icons/hicolor/$i/apps/
	install -p -m 644 %name-$i.png %buildroot%_datadir/icons/hicolor/$i/apps/%name.png
done

%files
%doc COPYING AUTHORS README NEWS THANKS ChangeLog
%_bindir/*
%_man1dir/cssh.*
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/applications/%name.desktop

%changelog
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
