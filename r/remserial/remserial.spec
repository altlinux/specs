Name: remserial
License: GPL
Group: System/Kernel and hardware
Summary: Serial and Network Communication Software Package
Version: 1.4
Release: alt1.qa1
Url: http://lpccomp.bc.ca/remserial/
Source: %name.tar
Packager: Boris Savelev <boris@altlinux.org>

%description
The remserial program acts as a communications bridge 
between a TCP/IP network port and a Linux device 
such as a serial port. Any character-oriented Linux /dev device will work.

%prep
%setup -n %name

%build
export CFLAGS='%optflags'
%make_build

%install
install -Dp -m 755 %name %buildroot%_bindir/%name

%files
%doc README.txt
%_bindir/%name

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jan 31 2010 Boris Savelev <boris@altlinux.org> 1.4-alt1
- new verison
- build with optflags
- fix permission on created dev

* Wed Aug 20 2008 Boris Savelev <boris@altlinux.org> 0.1-alt1
- initial build

