Name: cutter
Version: 1.03
Release: alt1

Summary: TCP/IP Connection Cutter
License: GPLv2+
Group: Networking/Other

Url: http://www.lowth.com/cutter/
Source: http://www.lowth.com/cutter/software/cutter-%version.tgz
Patch: cutter-missing_headers.patch

%description
"Cutter" is an open source program that allows Linux firewall
administrators to abort TCP/IP connections routed over the firewall
or router on which it is run.

%prep
%setup
%patch

%build
gcc -o %name %optflags %name.c

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/%name

%changelog
* Thu Mar 27 2014 Michael Shigorin <mike@altlinux.org> 1.03-alt1
- initial build for ALT Linux Sisyphus

* Tue Jan  3 2012 pascal.bleser@opensuse.org
- initial version (1.03)
