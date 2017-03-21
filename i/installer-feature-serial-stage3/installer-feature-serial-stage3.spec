Name: installer-feature-serial-stage3
Version: 0.2
Release: alt1

Summary: serial console support
License: public domain
Group: System/Kernel and hardware

Url: http://altlinux.org/serial
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
Setup %summary:
get what's provided for the boot
and set it for the installed system.

%prep

%post
CMDLINE="$(grep -ow 'console=ttyS[^ ]*' /proc/cmdline | head -1)"
[ -n "$CMDLINE" ] || exit 0
UNIT="${CMDLINE#console=ttyS}"
UNIT="${UNIT%%,*}"	# 0
MODE="${CMDLINE#*,}"	# 115200n8
SPEED="${MODE%%n*}"	# 115200
# TODO: should we add "quiet" to CMDLINE here?

# init
if [ -f /etc/inittab -a -x /sbin/agetty ]; then
	echo "T0:23:respawn:/sbin/agetty -L ttyS$UNIT $SPEED vt100" >> /etc/inittab
	echo "ttyS$UNIT" >> /etc/securetty
fi

# bootloader
if [ -f /etc/sysconfig/grub2 ]; then
	sed -i "s/splash/console=tty0 $CMDLINE/" /etc/sysconfig/grub2
	cat >> /etc/sysconfig/grub2 <<-EOF
	GRUB_TERMINAL_OUTPUT="serial console"
	GRUB_TERMINAL_INPUT="serial console"
	GRUB_SERIAL_COMMAND="serial --unit=$UNIT --speed=$SPEED"
	GRUB_TIMEOUT=10
	EOF
	update-grub
fi

%files

%changelog
* Tue Mar 21 2017 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- get authoritative serial port/speed from kernel cmdline

* Mon Mar 20 2017 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

