Name: cvoicecontrol
Version: 0.9
Release: alt2.alpha
%define beta alpha

Group: Sound
Summary: CVoiceControl is a speech recognition system enabling to use spoken commands
Url: http://www.kiecza.de/daniel/linux/
License: GPL

Source0: http://www.kiecza.de/daniel/linux/%name-%version%beta.tar.gz
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
%patch0 -p1

%build
#aclocal-1.6
#autoconf_2.5
#automake-1.6
%configure

%make CFLAGS="%optflags " CC="%__cc"

%install
mkdir -p %buildroot/%_bindir
install cvoicecontrol/cvoicecontrol  %buildroot/%_bindir
install cvoicecontrol/model_editor  %buildroot/%_bindir
install cvoicecontrol/microphone_config  %buildroot/%_bindir

%files
%doc AUTHORS BUGS FAQ README cvoicecontrol/docs/en/index*.html
%attr(755,root,root) %_bindir/*

%changelog
* Mon Oct 28 2002 Sergey V Turchin <zerg@altlinux.ru> 0.9-alt2.alpha
- rebuild with gcc3.2

* Mon Aug 19 2002 Sergey V Turchin <zerg@altlinux.ru> 0.9-alt1.alpha
- build for ALT
