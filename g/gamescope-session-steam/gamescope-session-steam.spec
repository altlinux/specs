%define _unpackaged_files_terminate_build 1
%define gss_p gamescope-session-plus
%define _libexecdir /usr/libexec
%define commit 015e09825d4f9a2dfdbc20fc2711e2dcee2af68a

Name: gamescope-session-steam
Version: 0.0.1.git015e09
Release: alt1

Summary: Steam Big Picture session based on gamescope

License: MIT
Group: Games/Other
Url: https://github.com/ChimeraOS/gamescope-session-steam

# Source-url: https://github.com/ChimeraOS/%name/archive/%commit.tar.gz?/%name-%commit.tar.gz
Source: %name-%version.tar

Patch1: drop-steamos-functions.patch
Patch2: shebang.patch
Patch3: update-policy.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-python3

%add_findreq_skiplist %_datadir/%gss_p/sessions.d/steam
Requires: gamescope-session-plus

%description
%summary

%prep
%setup
%autopatch -p1

rm -rv usr/share/wayland-sessions/gamescope-session.desktop

%build
%install
mkdir -p %buildroot{%_bindir,%_datadir}
cp -rv usr/bin/* %buildroot%_bindir/
cp -rv usr/share/* %buildroot%_datadir/
mv %buildroot%_bindir/steamos-polkit-helpers %buildroot%_datadir/%gss_p/

%postun
if [[ -d %_bindir/steamos-polkit-helpers ]]
then rm -rvf %_bindir/steamos-polkit-helpers
fi

%files
%doc LICENSE
%_bindir/steamos-cp-polkit-bin
%_bindir/jupiter-biosupdate
%_bindir/steam-http-loader
%_bindir/steamos-select-branch
%_bindir/steamos-session-select
%_bindir/steamos-update
%dir %_datadir/%gss_p/sessions.d
%_datadir/%gss_p/sessions.d/steam
%_datadir/%gss_p/steamos-polkit-helpers
%_datadir/applications/gamescope-mimeapps.list
%_datadir/applications/steam_http_loader.desktop
%_datadir/polkit-1/actions/org.chimeraos.update.policy
%_datadir/wayland-sessions/%name.desktop

%changelog
* Fri Aug 02 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.1.git015e09-alt1
- initial build for ALT Sisyphus

