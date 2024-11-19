%define _unpackaged_files_terminate_build 1
#Change verify method because info file cannot pass verify-info check
%set_verify_info_method relaxed

Name: netmask
Version: 2.4.4
Release: alt1
Summary: Utility for determining network masks
License: GPLv2+
Group: Networking/Other
Url: https://github.com/tlby/netmask

Source0: %name-%version.tar

BuildRequires: texinfo

%description
This is a handy tool for generating terse netmasks in several common
formats.  If you've ever maintained a firewall with more than a few
rules in it, you might use netmask to clean up and generalize sloppy
rules left by the network administrator before you.  It will also
convert netmasks from one format to another for the day you change
your firewall software.

%prep
%setup
%autoreconf

%build
%configure
%make_build CFLAGS="%optflags"


%install
%makeinstall_std

%check
%make check

%files
%doc README
%_bindir/%name
%_man1dir/%name.1*
%_infodir/%name.info.*

%changelog
* Mon Nov 18 2024 Pavel Shilov <zerospirit@altlinux.org> 2.4.4-alt1
- initial build for Sisyphus

