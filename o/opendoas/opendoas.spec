%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

Name: opendoas
Version: 6.8.2
Release: alt2
Summary: Portable fork of the OpenBSDs doas command

# ISC: main program
# BSD-3-Clause: libopenbsd
License: ISC and BSD-3-Clause
Group: System/Base
URL: https://github.com/Duncaen/OpenDoas
VCS: https://github.com/Duncaen/OpenDoas

Source: %name-%version.tar
Patch: %name-%version-alt.patch

Provides: doas = %EVR

BuildRequires: byacc
BuildRequires: pam-devel

%description
doas is a minimal replacement for the venerable sudo. It was initially written
by Ted Unangst of the OpenBSD project to provide 95%% of the features of sudo
with a fraction of the codebase.

%prep
%setup
%autopatch -p1

%build
# Use local ./configure script (it's not GNU Autoconf)
./configure --prefix=%prefix --with-timestamp --with-pam
export CFLAGS="%optflags"
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir
cat > %buildroot%_sysconfdir/doas.conf << EOF
# Allow wheel by default.
permit :wheel
EOF

mkdir -p  %buildroot%_sysconfdir/pam.d
cat > %buildroot%_sysconfdir/pam.d/doas << EOF
#%%PAM-1.0
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF

mkdir -p %buildroot%_controldir
cat > %buildroot%_controldir/doas << \EOF
#!/bin/sh

. /etc/control.d/functions

BINARY=/usr/bin/doas

# setuid bit for escalation; restrict who may execute the doas binary
new_fmode public    4711 root root
new_fmode wheelonly 4710 root wheel
new_fmode restricted 700  root root

new_help public    "Any user can execute $BINARY"
new_help wheelonly "Only \"wheel\" group members can execute $BINARY"
new_help restricted "Only root can execute $BINARY"

new_summary 'Execute commands via doas'

control_fmode "$BINARY" "$*" || exit 1
EOF

cat > %buildroot%_controldir/doaswheel << \EOF
#!/bin/sh

. /etc/control.d/functions

CONFIG=/etc/doas.conf

# Comment or uncomment the permit :wheel rule in the doas configuration
new_subst disabled \
    '^\s*permit\s*:wheel\b.*$' \
    's,^[ \t]*\(permit\s*:wheel\b.*\)$,# \1,'
new_subst enabled \
    '^\s*#\s*permit\s*:wheel\b.*$' \
    's,^[ \t]*#\s*\(permit\s*:wheel\b.*\)$,\1,'

new_help enabled  'Enable doas for wheel group members'
new_help disabled 'Disable doas for wheel group members'

new_summary 'doas rule "permit :wheel" for wheel users'

control_subst "$CONFIG" "$*" || exit 1
EOF

%pre
%pre_control doas
if [ -f "%_controldir/doaswheel" ]; then
    %pre_control doaswheel
fi

%post
%post_control -s wheelonly doas

%files
%doc README.md LICENSE
%_bindir/doas
%attr(755,root,root) %config %_controldir/doas*
%config(noreplace) %_sysconfdir/doas.conf
%config(noreplace) %_sysconfdir/pam.d/doas
%_man1dir/doas.1*
%_man5dir/doas.conf.5*

%changelog
* Fri Jul 22 2025 Alexey Volkov <qualimock@altlinux.org> 6.8.2-alt2
- add configuration files for control
- remove poor russian translation
- remove lookup in /bin and /sbin

* Fri Mar 15 2024 Alexey Volkov <qualimock@altlinux.org> 6.8.2-alt1
- Initial build for ALT (closes: #49706)
