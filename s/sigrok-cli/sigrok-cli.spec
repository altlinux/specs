Name: sigrok-cli
Version: 0.7.0
Release: alt1

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
%_man1dir/sigrok-cli.1*

%changelog
* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- initial
