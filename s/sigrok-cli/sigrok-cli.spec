Name: sigrok-cli
Version: 0.7.2
Release: alt3

Summary: sigrok -- signal analysis software suite
License: GPLv3
Group: Development/Other
Url: https://sigrok.org/

Source: %name-%version-%release.tar

BuildRequires: glib2-devel
BuildRequires: libsigrok-devel >= 0.5.0 libsigrokdecode >= 0.5.0

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

sigrok-cli is a command-line tool written in C, which uses both libsigrok
and libsigrokdecode to provide the basic sigrok functionality from the
command-line. Among other things, it is useful for scripting purposes.

Visit http://sigrok.org/wiki/Sigrok-cli for more.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/sigrok-cli
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_man1dir/sigrok-cli.1*

%changelog
* Thu May 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.2-alt3
- sigrok-cli-unreleased-94-g9d9f7b8

* Thu Apr 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt2
- sigrok-cli-unreleased-89-g394fd9b

* Wed Mar 17 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt1
- 0.7.2 released

* Tue Oct 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.1-alt1
- 0.7.1 released

* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- initial
