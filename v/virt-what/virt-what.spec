Name: virt-what
Version: 1.12
Release: alt1

Summary: Detect if we are running in a virtual machine
License: GPLv2+
Group: Emulators

# http://git.annexia.org/?p=virt-what.git;a=summary
Url: http://et.redhat.com/~rjones/virt-what/
Source: %url/files/%name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Sep 22 2010
BuildRequires: libdb4-devel
BuildRequires: perl-podlators

%description
virt-what is a shell script which can be used to detect if the program
is running in a virtual machine.

The program prints out a list of "facts" about the virtual machine,
derived from heuristics.  One fact is printed per line.

If nothing is printed and the script exits with code 0 (no error),
then it can mean either that the program is running on bare-metal or
the program is running inside a type of virtual machine which we don't
know about or cannot detect.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README COPYING
%_libexecdir/%name-cpuid-helper
%_sbindir/%name
%_man1dir/*

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 1.12-alt1
- 1.12

* Wed May 18 2011 Anton Protopopov <aspsk@altlinux.org> 1.9-alt1
- Switch to upstream git and update to 1.9

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 22 2010 Michael Shigorin <mike@altlinux.org> 1.2-alt1
- 1.2
- spec cleanup

* Thu Aug 28 2008 Anton Protopopov <aspsk@altlinux.org> 1.0-alt1
- Initial build
