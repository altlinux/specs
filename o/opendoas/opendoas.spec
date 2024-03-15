%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

Name:           opendoas
Version:        6.8.2
Release:        alt1
Summary:        Portable fork of the OpenBSDs doas command
Summary(ru_RU.UTF-8): Портативная версия команды doas из OpenBSD

# ISC: main program
# BSD-3-Clause: libopenbsd
License:        ISC and BSD-3-Clause
Group:          System/Base
URL:            https://github.com/Duncaen/OpenDoas
VCS:            https://github.com/Duncaen/OpenDoas

Source0:        %name-%version.tar
Patch0:         opendoas-6.8.2-fedora-remove-chown-in-makefile.patch

BuildRequires:  byacc
BuildRequires:  pam-devel

Provides:       doas = %EVR

%description
doas is a minimal replacement for the venerable sudo. It was initially written
by Ted Unangst of the OpenBSD project to provide 95%% of the features of sudo
with a fraction of the codebase

%description -l ru_RU.UTF-8
doas — это минимальная замена почтенного sudo. Первоначально она была написана
Тедом Унангстом из проекта OpenBSD, чтобы обеспечить 95%% функций sudo
с частью кодовой базы

%prep
%setup
%patch0 -p1

%build
# Non standard build script
./configure --prefix=%prefix --with-timestamp --with-pam
export CFLAGS="%optflags"
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir
cat > %buildroot%_sysconfdir/doas.conf << EOF
# Allow wheel by default
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

%files
%doc README.md LICENSE
%_bindir/doas
%config(noreplace) %_sysconfdir/doas.conf
%config(noreplace) %_sysconfdir/pam.d/doas
%_man1dir/doas.1*
%_man5dir/doas.conf.5*

%changelog
* Fri Mar 15 2024 Alexey Volkov <qualimock@altlinux.org> 6.8.2-alt1
- Initial build for ALT (closes: #49706)
