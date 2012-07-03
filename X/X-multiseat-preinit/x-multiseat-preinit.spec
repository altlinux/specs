Summary:  Preinitialize multiple video cards before dm service.
Name: X-multiseat-preinit
Version: 0.02
Release: alt1
License: GPL2+ or Artistic
Group: System/X11
Url: http://www.altlinux.org/X11/DualSeat
Packager: Igor Vlasenko <viy@altlinux.org>

Source0: %{name}-%{version}.tar

BuildArch: noarch

%description
Preinitializer of video cards in multiseat environment. 
Due to bugs/features in video drivers, nvidia among others, 
first simultaneous launch of multiple X servers can cause X to freeze. 
Calling X in multihead but oneseat configuration (with a unique X server) 
before the dm service seems to solve this problem.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_initdir/
install -m 755 x-multiseat-preinit.init %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig/
cat > %buildroot%_sysconfdir/sysconfig/x-multiseat-preinit <<EOF
# xserver used
# XSERVER=/usr/bin/Xorg

# layout where both cards are used (if not default)
# XARGS="-layout dualhead"

# application run on server startup. Note, it should terminate quickly!
# XCLIENT="sleep 1"
# you may also specify a wrapper for something fancy like
# xli -display 0 -fullscreen -onroot /usr/share/wallpapers/soft-green.jpg
EOF

%files
%doc xorg.conf.multiseat
%config %_initdir/%name
%config(missingok,noreplace) %_sysconfdir/sysconfig/x-multiseat-preinit

%changelog
* Wed Jan 28 2009 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added minimal documentation

* Mon Feb 11 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build

