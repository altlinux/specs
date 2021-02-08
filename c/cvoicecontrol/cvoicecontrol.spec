Name: cvoicecontrol
Version: 0.9.1
Release: alt1
%define beta %nil

Group: Sound
Summary: CVoiceControl is a speech recognition system enabling to use spoken commands
Url: http://www.kiecza.de/daniel/linux/
#https://github.com/Sound-Linux-More/cvoicecontrol
License: GPL-2.0

Source0: %name-%version%beta.tar
Patch0: %name-make.patch

# Automatically added by buildreq on Mon Aug 19 2002
BuildRequires: libncurses-devel libtinfo-devel

%description
CVoiceControl is a speech recognition system that enables a user to
connect spoken commands to unix commands.  It automagically detects
speech input from a microphone, performs recognition on this input and
in case of successful recognition - executes the associated unix
command.

%prep
%setup -q -n %name-%version%beta
#%patch0 -p1
%autoreconf

%build
%add_optflags -fcommon
%configure
#make CFLAGS="%optflags " CC="%__cc"
%make

%install
%make install DESTDIR=%buildroot prefix=%buildroot%prefix

%files
%doc AUTHORS BUGS FAQ README src/docs/en/*.html
%_bindir/*

%changelog
* Mon Feb 08 2021 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- new version

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9-alt2.alpha.qa1
- NMU: rebuilt for debuginfo.

* Mon Oct 28 2002 Sergey V Turchin <zerg@altlinux.ru> 0.9-alt2.alpha
- rebuild with gcc3.2

* Mon Aug 19 2002 Sergey V Turchin <zerg@altlinux.ru> 0.9-alt1.alpha
- build for ALT
