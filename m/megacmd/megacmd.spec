Name: megacmd
Version: 0.9.7
Release: alt1

Summary: Command Line Interactive and Scriptable Application to access MEGA

License: BSD 2-clause Simplified License
Group: Other
Url: https://github.com/meganz/MEGAcmd

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/meganz/MEGAcmd/archive/%version.tar.gz
Source: %name-%version.tar

Patch1: 0001-build-with-external-libmegasdk.patch

# optimized out: glibc-kernheaders-x86 libcares-devel libcom_err-devel libcryptopp-devel libcurl-devel libfreeimage-devel libkrb5-devel libpcre-devel libsodium-devel libsqlite3-devel libssl-devel libstdc++-devel perl python-base python-module-google python-modules python3 python3-base sssd-client
BuildRequires: gcc-c++ libmegasdk-devel libpcrecpp-devel libreadline-devel libuv-devel

%description
MEGAcmd provides non UI access to MEGA services.
It intends to offer all the functionality with your MEGA account via commands.

Available packages for MEGAcmd in all supported platforms should be found here.

It supports 2 modes of interaction:

interactive. A shell to query your actions
scriptable. A way to execute commands from a shell/a script/another program.
In order to provide those 2 modes, it features one server (MEGAcmdServer),
an interactive shell (MEGAcmdShell) and several commands that will launch
the non-interactive client (MEGAcmdClient).

%prep
%setup
%patch1 -p2
cp -a %_datadir/libmegasdk/m4/ sdk/

# hack against missed --tag=CXX during linking
%__subst 's|ANDROID|TRUE|' Makefile.am

# hack against pcre checking
%__subst 's|with_pcre/include|with_pcre|' configure.ac

%build
%autoreconf
%configure --with-pcre=%_includedir/pcre
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
/etc/bash_completion.d/megacmd_completion.sh
%_bindir/mega-*
%doc README.md LICENSE

%changelog
* Sat Dec 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- Initial build for Sisyphus
