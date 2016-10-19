Name: samplicator
Version: 1.3.6
Release: alt1
Summary: Send copies of (UDP) datagrams to multiple receivers, with optional sampling and spoofing
License: GPLv2+
Group: Networking/Other
Url: https://github.com/sleinen/samplicator
Source0: %name-%version.tar
Buildrequires: gcc

%description
Send copies of (UDP) datagrams to multiple receivers, with optional sampling and spoofing

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/samplicate

%changelog
* Wed Oct 19 2016 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt1
- Initial build for Alt Linux Sisyphus.
