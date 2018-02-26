Name: fw-template-c
Version: 0.0.4
Release: alt1
Summary: C development template for Framewerk
License: %gpl2plus
Group: Development/C
URL: http://fwtemplates.googlecode.com
Source: %url/files/%name-%version.tar
BuildArch: noarch
Requires: framewerk
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

%description
fw-template-C ia a C development template for Framewerk.


%prep
%setup


%build
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog README TODO
%_datadir/fw/m4/*
%_datadir/fw/template/*
%_libexecdir/fw/*


%changelog
* Mon Mar 02 2009 Led <led@altlinux.ru> 0.0.4-alt1
- initial build
