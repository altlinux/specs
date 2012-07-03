%define Name Framewerk
Name: framewerk
Version: 0.1.30
Release: alt1
Summary: A build system
License: %gpl2only
Group: Development/Tools
URL: http://fwtemplates.googlecode.com
Source: %url/files/%name-%version.tar
BuildArch: noarch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

%description
%Name is a build system. It's designed to allow packaging up common
development patterns (C project, Erlang project, framewerk template,
etc.) and abstract over things like packaging, revision control, etc.


%prep
%setup


%build
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog README TODO
%_bindir/*
%_datadir/fw
%exclude %_datadir/fw/package/deb
%dir %_libexecdir/fw
%_libexecdir/fw/*


%changelog
* Sun Mar 01 2009 Led <led@altlinux.ru> 0.1.30-alt1
- initial build
